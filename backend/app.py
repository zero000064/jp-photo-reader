from __future__ import annotations

import asyncio
import json
import base64
import io
import os
import re
import sqlite3
from pathlib import Path
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

try:
    from sudachipy import Dictionary as SudachiDictionary
    from sudachipy import SplitMode
except Exception:  # pragma: no cover - optional runtime dependency
    SudachiDictionary = None
    SplitMode = None

try:
    from fugashi import Tagger
except Exception:  # pragma: no cover - optional runtime dependency
    Tagger = None


APP_DIR = Path(__file__).resolve().parent
DB_PATH = APP_DIR / "data" / "jmdict.sqlite"
JAPANESE_CHAR_PATTERN = r"[\u3040-\u30ff\u3400-\u9fff]"
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/")
DEFAULT_OLLAMA_TEXT_MODEL = "hf.co/XpressAI/shisa-v2.1-unphi4-14b-GGUF:Q4_K_M"
OLLAMA_TEXT_MODEL = os.getenv("OLLAMA_TEXT_MODEL", DEFAULT_OLLAMA_TEXT_MODEL)
MANGA_OCR_REQUIRE_CUDA = os.getenv("MANGA_OCR_REQUIRE_CUDA", "1").lower() not in {"0", "false", "no"}
_manga_ocr = None

app = FastAPI(title="Japanese Photo Reader API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://*", "http://127.0.0.1", "http://localhost"],
    allow_origin_regex=r"chrome-extension://.*",
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

sudachi_tokenizer = SudachiDictionary().create() if SudachiDictionary else None
tagger = Tagger() if Tagger else None


class AnalyzeImageRequest(BaseModel):
    image: str
    explain_grammar: bool = True
    grammar_question: str | None = None


class AnalyzeTextRequest(BaseModel):
    text: str
    explain_grammar: bool = True
    grammar_question: str | None = None


class GrammarQuestionRequest(BaseModel):
    text: str
    grammar_question: str


class LookupTextRequest(BaseModel):
    text: str


SEED_DICTIONARY = {
    "私": {"reading": "わたし", "glosses": ["I; me"]},
    "僕": {"reading": "ぼく", "glosses": ["I; me, used mostly by males"]},
    "彼": {"reading": "かれ", "glosses": ["he; boyfriend"]},
    "彼女": {"reading": "かのじょ", "glosses": ["she; girlfriend"]},
    "日本": {"reading": "にほん", "glosses": ["Japan"]},
    "今日": {"reading": "きょう", "glosses": ["today"]},
    "明日": {"reading": "あした", "glosses": ["tomorrow"]},
    "行く": {"reading": "いく", "glosses": ["to go"]},
    "見る": {"reading": "みる", "glosses": ["to see; to look"]},
    "食べる": {"reading": "たべる", "glosses": ["to eat"]},
    "する": {"reading": "する", "glosses": ["to do"]},
    "ある": {"reading": "ある", "glosses": ["to exist; to have"]},
    "いる": {"reading": "いる", "glosses": ["to be; to exist, for animate things"]},
}


@app.get("/health")
async def health() -> dict[str, Any]:
    return {
        "ok": True,
        "ollama_url": OLLAMA_URL,
        "ollama_text_model": OLLAMA_TEXT_MODEL,
        "ocr_provider": "manga-ocr",
        "manga_ocr_device": manga_ocr_device(),
        "manga_ocr_require_cuda": MANGA_OCR_REQUIRE_CUDA,
        "torch_cuda_available": torch_cuda_available(),
        "dictionary": DB_PATH.exists(),
    }


@app.post("/analyze-image")
async def analyze_image(payload: AnalyzeImageRequest) -> dict[str, Any]:
    image_b64 = normalize_image_payload(payload.image)
    text = await ocr_with_manga_ocr(image_b64)
    result = await analyze_text_internal(text, payload.explain_grammar, payload.grammar_question)
    result["ocr_provider"] = "manga-ocr"
    result["manga_ocr_device"] = manga_ocr_device()
    return result


@app.post("/analyze-text")
async def analyze_text(payload: AnalyzeTextRequest) -> dict[str, Any]:
    return await analyze_text_internal(payload.text, payload.explain_grammar, payload.grammar_question)


@app.post("/answer-grammar-question")
async def answer_grammar_question(payload: GrammarQuestionRequest) -> dict[str, Any]:
    cleaned = normalize_ocr_text(payload.text)
    grammar_question = payload.grammar_question.strip()
    if not cleaned:
        raise HTTPException(status_code=400, detail="text is required")
    if not grammar_question:
        raise HTTPException(status_code=400, detail="grammar_question is required")
    grammar_answer = await answer_grammar_question_with_ollama(cleaned, grammar_question)
    return {
        "text": cleaned,
        "grammar_answer": grammar_answer,
        "grammar_question": grammar_question,
    }


@app.post("/lookup-text")
async def lookup_text(payload: LookupTextRequest) -> dict[str, Any]:
    cleaned = normalize_lookup_text(payload.text)
    tokens = tokenize(cleaned)
    dictionary = [entry for token in tokens if should_lookup_token(token) for entry in lookup_token(token)]
    return {
        "text": cleaned,
        "tokens": tokens,
        "dictionary": dictionary,
    }


async def analyze_text_internal(text: str, explain_grammar: bool, grammar_question: str | None = None) -> dict[str, Any]:
    cleaned = normalize_ocr_text(text)
    tokens = tokenize(cleaned)
    structure = parse_sentence_structure(tokens)
    dictionary = dedupe_entries([entry for item in structure for entry in item.get("dictionary", [])])
    grammar_question = (grammar_question or "").strip()
    grammar_analysis = await analyze_grammar_with_ollama(cleaned, structure) if explain_grammar else ""
    grammar_answer = await answer_grammar_question_with_ollama(cleaned, grammar_question) if explain_grammar and grammar_question else ""
    return {
        "text": cleaned,
        "tokens": tokens,
        "sentence_structure": structure,
        "dictionary": dictionary,
        "grammar_analysis": grammar_analysis,
        "grammar_answer": grammar_answer,
        "grammar_question": grammar_question,
    }


def normalize_image_payload(image: str) -> str:
    if "," in image and image.startswith("data:"):
        image = image.split(",", 1)[1]
    try:
        base64.b64decode(image, validate=True)
    except Exception as exc:
        raise HTTPException(status_code=400, detail="image must be base64 or a data URL") from exc
    return image


async def ocr_with_manga_ocr(image_b64: str) -> str:
    try:
        image_bytes = base64.b64decode(image_b64)
    except Exception as exc:
        raise HTTPException(status_code=400, detail="image must be valid base64") from exc

    try:
        from PIL import Image
        from manga_ocr import MangaOcr
    except ImportError as exc:
        raise HTTPException(
            status_code=500,
            detail="Manga-OCR is not installed. Install it with: python -m pip install -r backend/requirements-manga-ocr.txt",
        ) from exc

    ensure_manga_ocr_cuda_available()

    def run_ocr() -> str:
        global _manga_ocr
        if _manga_ocr is None:
            _manga_ocr = MangaOcr()
        if MANGA_OCR_REQUIRE_CUDA and not manga_ocr_device().startswith("cuda"):
            raise RuntimeError(f"Manga-OCR GPU required, but model loaded on {manga_ocr_device()}")
        with Image.open(io.BytesIO(image_bytes)) as image:
            return str(_manga_ocr(image.convert("RGB"))).strip()

    try:
        return await asyncio.to_thread(run_ocr)
    except RuntimeError as exc:
        if "Manga-OCR GPU required" in str(exc):
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        raise


def manga_ocr_device() -> str:
    if _manga_ocr is None:
        return "not_loaded"
    model = getattr(_manga_ocr, "model", None)
    try:
        return str(next(model.parameters()).device) if model is not None else "unknown"
    except Exception:
        return "unknown"


def torch_cuda_available() -> bool:
    try:
        import torch
    except ImportError:
        return False
    return bool(torch.cuda.is_available())


def ensure_manga_ocr_cuda_available() -> None:
    if not MANGA_OCR_REQUIRE_CUDA:
        return
    try:
        import torch
    except ImportError as exc:
        raise HTTPException(status_code=503, detail="Manga-OCR GPU is required, but PyTorch is not installed") from exc
    if not torch.cuda.is_available():
        raise HTTPException(
            status_code=503,
            detail="Manga-OCR GPU is required, but torch.cuda.is_available() is false in this backend process",
        )


async def analyze_grammar_with_ollama(
    text: str, structure: list[dict[str, str]]
) -> str:
    prompt = f"""
/no_think
You are a Japanese grammar analyst. Return only the final answer, no reasoning.

Sentence:
{text}

SudachiPy token structure:
{format_structure_for_prompt(structure)}

Use the SudachiPy structure to explain how the sentence works grammatically.
Focus on useful learner-facing analysis: clause structure, particles, verb forms, auxiliaries, conjugations, and natural meaning.
Do not return a list of matched grammar labels. Do not include character offsets.
Return a concise plain-text explanation.
""".strip()
    body = {
        "model": OLLAMA_TEXT_MODEL,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "options": {"temperature": 0.2, "num_predict": 1024, "repeat_penalty": 1.1},
    }
    async with httpx.AsyncClient(timeout=120) as client:
        try:
            response = await client.post(f"{OLLAMA_URL}/api/generate", json=body)
            response.raise_for_status()
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=502, detail=f"Ollama grammar analysis request failed: {exc}") from exc
    return ollama_text_response(response.json())


async def answer_grammar_question_with_ollama(
    text: str, grammar_question: str
) -> str:
    prompt = f"""
/no_think
You are a Japanese grammar tutor. Return only the final answer, no reasoning.

Sentence:
{text}

User grammar question:
{grammar_question}

Answer the user question directly in 1 short paragraph. Start with the answer immediately. Do not describe your reasoning. Use only the sentence and the user question; do not use or mention SudachiPy token structure.
""".strip()
    body = {
        "model": OLLAMA_TEXT_MODEL,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "options": {"temperature": 0.2, "num_predict": 1024, "repeat_penalty": 1.1},
    }
    async with httpx.AsyncClient(timeout=120) as client:
        try:
            response = await client.post(f"{OLLAMA_URL}/api/generate", json=body)
            response.raise_for_status()
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=502, detail=f"Ollama grammar question request failed: {exc}") from exc
    return ollama_text_response(response.json())


def ollama_text_response(payload: dict[str, Any]) -> str:
    response = str(payload.get("response") or "").strip()
    if response:
        return response
    return str(payload.get("thinking") or "").strip()


def format_structure_for_prompt(structure: list[dict[str, str]]) -> str:
    if not structure:
        return "(none)"
    return "\n".join(
        "- {surface} | lemma={lemma} | reading={reading} | role={role} | pos={pos}".format(
            surface=item.get("surface", ""),
            lemma=item.get("lemma", ""),
            reading=item.get("reading", ""),
            role=item.get("role", ""),
            pos=item.get("pos", ""),
        )
        for item in structure
    )


def normalize_ocr_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = join_vertical_ocr_lines(text)
    return text.strip()


def normalize_lookup_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def join_vertical_ocr_lines(text: str) -> str:
    paragraphs = text.split("\n\n")
    return "\n\n".join(join_vertical_ocr_paragraph(paragraph) for paragraph in paragraphs)


def join_vertical_ocr_paragraph(paragraph: str) -> str:
    lines = [line.strip() for line in paragraph.split("\n") if line.strip()]
    if len(lines) < 2:
        return paragraph.strip()

    compact_lines = [re.sub(r"\s+", "", line) for line in lines]
    japanese_lines = [line for line in compact_lines if re.search(JAPANESE_CHAR_PATTERN, line)]
    if len(japanese_lines) < 2:
        return "\n".join(lines)

    avg_len = sum(len(line) for line in japanese_lines) / len(japanese_lines)
    short_line_ratio = sum(len(line) <= 5 for line in japanese_lines) / len(japanese_lines)
    japanese_ratio = len(japanese_lines) / len(compact_lines)
    looks_vertical = avg_len <= 5 and short_line_ratio >= 0.75 and japanese_ratio >= 0.75
    if not looks_vertical:
        return "\n".join(lines)

    return " ".join(compact_lines)


def tokenize(text: str) -> list[dict[str, str]]:
    if not text:
        return []
    if sudachi_tokenizer:
        tokens = []
        for word in sudachi_tokenizer.tokenize(text, SplitMode.C):
            surface = word.surface()
            if not surface.strip():
                continue
            pos_parts = [part for part in word.part_of_speech() if part and part != "*"]
            tokens.append(
                {
                    "surface": surface,
                    "lemma": word.dictionary_form() or surface,
                    "reading": word.reading_form() or "",
                    "pos": ",".join(pos_parts),
                    "pos_group": simplify_pos(pos_parts[0] if pos_parts else ""),
                }
            )
        return tokens

    if tagger:
        tokens = []
        for word in tagger(text):
            surface = word.surface
            if not surface.strip():
                continue
            feature = word.feature
            lemma = getattr(feature, "lemma", None) or getattr(feature, "orthBase", None) or surface
            reading = getattr(feature, "kana", None) or getattr(feature, "pron", None) or ""
            pos_parts = [part for part in getattr(feature, "pos", ()) if part]
            tokens.append(
                {
                    "surface": surface,
                    "lemma": lemma,
                    "reading": reading,
                    "pos": ",".join(pos_parts),
                    "pos_group": simplify_pos(pos_parts[0] if pos_parts else ""),
                }
            )
        return tokens

    parts = re.findall(r"[\u3040-\u30ff\u3400-\u9fff]+|[A-Za-z0-9]+|[^\s]", text)
    return [fallback_token(part) for part in parts]


def fallback_token(surface: str) -> dict[str, str]:
    return {
        "surface": surface,
        "lemma": surface,
        "reading": "",
        "pos": guess_fallback_pos(surface),
        "pos_group": simplify_pos(guess_fallback_pos(surface)),
    }


def guess_fallback_pos(surface: str) -> str:
    if re.fullmatch(r"[。！？、,.!?]", surface):
        return "補助記号"
    if surface in {"は", "が", "を", "に", "へ", "で", "と", "も", "の", "から", "まで", "より", "や", "か", "ね", "よ"}:
        return "助詞"
    if surface.endswith(("る", "た", "て", "ます", "ない", "した", "して", "いる")):
        return "動詞"
    return "名詞"


def simplify_pos(pos: str) -> str:
    mapping = {
        "名詞": "noun",
        "代名詞": "pronoun",
        "動詞": "verb",
        "形容詞": "adjective",
        "形状詞": "adjectival noun",
        "副詞": "adverb",
        "助詞": "particle",
        "助動詞": "auxiliary",
        "接続詞": "conjunction",
        "連体詞": "adnominal",
        "感動詞": "interjection",
        "接頭辞": "prefix",
        "接尾辞": "suffix",
        "補助記号": "punctuation",
        "空白": "space",
    }
    return mapping.get(pos, pos or "unknown")


def parse_sentence_structure(tokens: list[dict[str, str]]) -> list[dict[str, Any]]:
    structure = []
    for index, token in enumerate(tokens):
        dictionary = lookup_token(token) if should_lookup_token(token) else []
        structure.append(
            {
                "token_id": index + 1,
                "surface": token.get("surface", ""),
                "lemma": token.get("lemma", ""),
                "reading": token.get("reading", ""),
                "pos": token.get("pos", ""),
                "role": token.get("pos_group") or simplify_pos((token.get("pos") or "").split(",")[0]),
                "dictionary": dictionary,
            }
        )
    return structure


def should_lookup_token(token: dict[str, str]) -> bool:
    return token.get("pos_group") not in {"particle", "auxiliary", "punctuation", "space"}


def lookup_token(token: dict[str, str]) -> list[dict[str, Any]]:
    keys = []
    for key in (token.get("lemma"), token.get("surface")):
        if key and key not in keys:
            keys.append(key)

    results = []
    if DB_PATH.exists():
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            for key in keys:
                rows = conn.execute(
                    """
                    select e.id, e.expression, e.reading, e.glosses
                    from entries e
                    join lookup l on l.entry_id = e.id
                    where l.term = ?
                    limit 5
                    """,
                    (key,),
                ).fetchall()
                for row in rows:
                    results.append(
                        {
                            "query": key,
                            "expression": row["expression"],
                            "reading": row["reading"],
                            "glosses": json.loads(row["glosses"]),
                            "source": "JMdict",
                        }
                    )
    else:
        for key in keys:
            if key in SEED_DICTIONARY:
                item = SEED_DICTIONARY[key]
                results.append(
                    {
                        "query": key,
                        "expression": key,
                        "reading": item["reading"],
                        "glosses": item["glosses"],
                        "source": "seed",
                    }
                )
    return dedupe_entries(results)


def dedupe_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen = set()
    unique = []
    for entry in entries:
        key = (entry["expression"], entry["reading"], tuple(entry["glosses"]))
        if key not in seen:
            seen.add(key)
            unique.append(entry)
    return unique


def normalize_for_grammar(text: str) -> str:
    return re.sub(
        rf"({JAPANESE_CHAR_PATTERN})[ \t\n]+({JAPANESE_CHAR_PATTERN})",
        r"\1\2",
        text,
    )
