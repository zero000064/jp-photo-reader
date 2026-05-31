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
    from grammar_matcher import (
        HANABIRA_ATTRIBUTION,
        DEFAULT_GRAMMAR_DIR,
        DEFAULT_MARKDOWN_DIR,
        build_entry_index,
        canonical_title,
        dedupe_matches,
        load_grammar_entries,
        match_grammar_points,
        normalize_classifier_label,
        recover_classifier_candidates,
        remove_contained_matches,
        read_grammar_markdown,
    )
except ImportError:  # pragma: no cover - supports importing backend.app from repo root
    from backend.grammar_matcher import (
        HANABIRA_ATTRIBUTION,
        DEFAULT_GRAMMAR_DIR,
        DEFAULT_MARKDOWN_DIR,
        build_entry_index,
        canonical_title,
        dedupe_matches,
        load_grammar_entries,
        match_grammar_points,
        normalize_classifier_label,
        recover_classifier_candidates,
        remove_contained_matches,
        read_grammar_markdown,
    )

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
DEFAULT_OLLAMA_TEXT_MODEL = "hf.co/DevQuasar/shisa-ai.shisa-v2-qwen2.5-32b-GGUF:Q3_K_M"
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
    explain_sentence_tree: bool = False
    use_ollama_grammar_classifier: bool = False
    grammar_question: str | None = None


class AnalyzeTextRequest(BaseModel):
    text: str
    explain_grammar: bool = True
    explain_sentence_tree: bool = False
    use_ollama_grammar_classifier: bool = False
    grammar_question: str | None = None


class GrammarQuestionRequest(BaseModel):
    text: str
    grammar_question: str


class LookupTextRequest(BaseModel):
    text: str


class GrammarMarkdownRequest(BaseModel):
    markdown_file: str


class AnalyzeGrammarOnlyRequest(BaseModel):
    text: str
    use_ollama_grammar_classifier: bool = False


class AnalyzeSentenceOnlyRequest(BaseModel):
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
        "hanabira_grammar": DEFAULT_GRAMMAR_DIR.exists(),
        "hanabira_grammar_markdown": DEFAULT_MARKDOWN_DIR.exists(),
    }


@app.post("/analyze-image")
async def analyze_image(payload: AnalyzeImageRequest) -> dict[str, Any]:
    image_b64 = normalize_image_payload(payload.image)
    text = await ocr_with_manga_ocr(image_b64)
    result = await analyze_text_internal(
        text,
        payload.explain_grammar,
        payload.grammar_question,
        payload.explain_sentence_tree,
        payload.use_ollama_grammar_classifier,
    )
    result["ocr_provider"] = "manga-ocr"
    result["manga_ocr_device"] = manga_ocr_device()
    return result


@app.post("/analyze-text")
async def analyze_text(payload: AnalyzeTextRequest) -> dict[str, Any]:
    return await analyze_text_internal(
        payload.text,
        payload.explain_grammar,
        payload.grammar_question,
        payload.explain_sentence_tree,
        payload.use_ollama_grammar_classifier,
    )


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


@app.post("/grammar-markdown")
async def grammar_markdown(payload: GrammarMarkdownRequest) -> dict[str, Any]:
    result = read_grammar_markdown(payload.markdown_file)
    if not result:
        raise HTTPException(status_code=404, detail="grammar markdown not found")
    return result


@app.post("/analyze-grammar-only")
async def analyze_grammar_only(payload: AnalyzeGrammarOnlyRequest) -> dict[str, Any]:
    cleaned = normalize_ocr_text(payload.text)
    if not cleaned:
        raise HTTPException(status_code=400, detail="text is required")
    tokens = tokenize(cleaned)
    structure = parse_sentence_structure(tokens)
    grammar_matches = match_grammar_points(cleaned, tokens, tokenize)
    if payload.use_ollama_grammar_classifier:
        grammar_matches = await enrich_grammar_matches_with_ollama(cleaned, tokens, grammar_matches)
    grammar_analysis = await analyze_grammar_with_ollama(cleaned, structure, grammar_matches)
    return {
        "text": cleaned,
        "grammar_analysis": grammar_analysis,
    }


@app.post("/analyze-sentence-only")
async def analyze_sentence_only(payload: AnalyzeSentenceOnlyRequest) -> dict[str, Any]:
    cleaned = normalize_ocr_text(payload.text)
    if not cleaned:
        raise HTTPException(status_code=400, detail="text is required")
    tokens = tokenize(cleaned)
    structure = parse_sentence_structure(tokens)
    sentence_analysis = await analyze_sentence_tree_with_ollama(cleaned, structure)
    return {
        "text": cleaned,
        "sentence_analysis": sentence_analysis,
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


async def analyze_text_internal(
    text: str,
    explain_grammar: bool,
    grammar_question: str | None = None,
    explain_sentence_tree: bool = False,
    use_ollama_grammar_classifier: bool = False,
) -> dict[str, Any]:
    cleaned = normalize_ocr_text(text)
    tokens = tokenize(cleaned)
    structure = parse_sentence_structure(tokens)
    dictionary = dedupe_entries([entry for item in structure for entry in item.get("dictionary", [])])
    grammar_question = (grammar_question or "").strip()
    grammar_matches = match_grammar_points(cleaned, tokens, tokenize)
    if use_ollama_grammar_classifier:
        grammar_matches = await enrich_grammar_matches_with_ollama(cleaned, tokens, grammar_matches)
    sentence_analysis = fallback_sentence_analysis(cleaned, structure)
    grammar_analysis = ""
    grammar_answer = ""

    if explain_grammar and explain_sentence_tree:
        grammar_analysis, sentence_analysis = await asyncio.gather(
            analyze_grammar_with_ollama(cleaned, structure, grammar_matches),
            analyze_sentence_tree_with_ollama(cleaned, structure),
        )
    elif explain_sentence_tree:
        sentence_analysis = await analyze_sentence_tree_with_ollama(cleaned, structure)
    elif explain_grammar:
        grammar_analysis = await analyze_grammar_with_ollama(cleaned, structure, grammar_matches)

    if explain_grammar and grammar_question:
        grammar_answer = await answer_grammar_question_with_ollama(cleaned, grammar_question)
    return {
        "text": cleaned,
        "tokens": tokens,
        "sentence_structure": structure,
        "dictionary": dictionary,
        "sentence_analysis": sentence_analysis,
        "grammar_matches": grammar_matches,
        "grammar_reference_attribution": HANABIRA_ATTRIBUTION if grammar_matches else "",
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
    global _manga_ocr
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
    except Exception as exc:
        if "Manga-OCR GPU required" in str(exc):
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        if is_cuda_ocr_error(exc):
            _manga_ocr = None
            raise HTTPException(
                status_code=503,
                detail=(
                    "Manga-OCR failed while running on CUDA. Restart the backend to reset the CUDA context, "
                    "then retry image analysis. If this repeats, close other GPU-heavy apps or start the backend "
                    "with MANGA_OCR_REQUIRE_CUDA=0 to allow CPU OCR."
                ),
            ) from exc
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


def is_cuda_ocr_error(exc: BaseException) -> bool:
    message = str(exc).lower()
    error_type = type(exc).__name__.lower()
    return "cuda" in message and (
        "launch failure" in message
        or "acceleratorerror" in error_type
        or "out of memory" in message
        or "illegal memory access" in message
    )


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


async def enrich_grammar_matches_with_ollama(
    text: str,
    tokens: list[dict[str, Any]],
    existing_matches: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    if not text or not tokens:
        return existing_matches

    candidates = await classify_grammar_points_with_ollama(text)
    if not candidates:
        return existing_matches

    entries = load_grammar_entries(str(DEFAULT_GRAMMAR_DIR))
    entry_index = build_entry_index(entries)
    labels = normalize_ollama_candidate_labels(candidates)
    recovered_labels = {str(match.get("rule_label") or "") for match in existing_matches}
    recovered = recover_classifier_candidates(tokens, labels, entry_index, recovered_labels)
    raw_candidate_matches = [
        ollama_candidate_to_match(candidate, text, entries)
        for candidate in candidates
        if not has_known_classifier_label(str(candidate.get("label") or ""))
    ]
    combined = [*existing_matches, *recovered, *raw_candidate_matches]
    combined = [match for match in combined if match.get("title")]
    combined.sort(key=lambda item: (float(item.get("confidence") or 0), len(str(item.get("matched_text") or ""))), reverse=True)
    return remove_contained_matches(dedupe_matches(combined))[:12]


async def classify_grammar_points_with_ollama(text: str) -> list[dict[str, Any]]:
    catalog = format_candidate_grammar_catalog(text)
    prompt = f"""
/no_think
You are a Japanese grammar point detector. Return only valid JSON, no markdown.

Detect learner-facing Japanese grammar points in the sentence. Do not explain the full sentence.
Prefer labels from this local Hanabira grammar catalog when the marker appears with the same meaning in the sentence:
{catalog}

Return this exact JSON shape:
{{
  "candidates": [
    {{"label": "grammar label", "span_hint": "Japanese span in the sentence", "confidence": 0.0}}
  ]
}}

Rules:
- Return at most 8 candidates.
- Include useful particles only when they have a clear learner-facing role, such as で meaning using/by means of.
- Include nested grammar when useful, e.g. Vてみる inside Vてもいい.
- Use plain labels like Vてみる, Vてもいい, かも, で.

Sentence:
{text}
""".strip()
    body = {
        "model": OLLAMA_TEXT_MODEL,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "format": "json",
        "options": {"temperature": 0.0, "num_predict": 700, "repeat_penalty": 1.05},
    }
    timeout = float(os.getenv("JPR_OLLAMA_GRAMMAR_CLASSIFIER_TIMEOUT", "35"))
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(f"{OLLAMA_URL}/api/generate", json=body)
            response.raise_for_status()
    except (httpx.HTTPError, ValueError):
        return []

    content = ollama_text_response(response.json())
    try:
        parsed = json.loads(content)
    except json.JSONDecodeError:
        return []
    candidates = parsed.get("candidates", []) if isinstance(parsed, dict) else []
    return [compact_ollama_candidate(item) for item in candidates if isinstance(item, dict)]


def format_candidate_grammar_catalog(text: str, limit: int = 40) -> str:
    normalized_text = re.sub(r"[\s\u3000、。,.!?！？\-ー]+", "", text)
    candidates = []
    for entry in load_grammar_entries(str(DEFAULT_GRAMMAR_DIR)):
        markers = [str(marker) for marker in entry.get("markers", []) if marker]
        matched_markers = [marker for marker in markers if marker in normalized_text]
        if not matched_markers:
            continue
        title = str(entry.get("title") or "").strip()
        formation = str(entry.get("formation") or "").strip()
        if not title:
            continue
        marker_text = "/".join(matched_markers[:3])
        row = f"- {title} [marker: {marker_text}]: {formation}" if formation else f"- {title} [marker: {marker_text}]"
        candidates.append((max(len(marker) for marker in matched_markers), row))
    candidates.sort(key=lambda item: item[0], reverse=True)
    rows = [row for _, row in candidates[:limit]]
    return "\n".join(rows) if rows else "- No local catalog candidates found."


def normalize_ollama_candidate_labels(candidates: list[dict[str, Any]]) -> list[str]:
    labels: list[str] = []
    for candidate in candidates:
        label = str(candidate.get("label") or "")
        for normalized in normalize_classifier_label(label):
            if normalized.startswith("classifier:"):
                continue
            labels.append(normalized)
    seen = set()
    result = []
    for label in labels:
        if label and label not in seen:
            seen.add(label)
            result.append(label)
    return result


def has_known_classifier_label(label: str) -> bool:
    return any(not item.startswith("classifier:") for item in normalize_classifier_label(label))


def compact_ollama_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    confidence = candidate.get("confidence", 0.55)
    try:
        confidence = float(confidence)
    except (TypeError, ValueError):
        confidence = 0.55
    return {
        "label": str(candidate.get("label") or "").strip(),
        "span_hint": str(candidate.get("span_hint") or "").strip(),
        "confidence": max(0.0, min(confidence, 0.9)),
    }


def ollama_candidate_to_match(candidate: dict[str, Any], text: str, entries: tuple[dict[str, Any], ...]) -> dict[str, Any]:
    label = str(candidate.get("label") or "").strip()
    span_hint = str(candidate.get("span_hint") or "").strip()
    entry = find_entry_for_candidate_label(label, entries) or {}
    matched_text = span_hint if span_hint and span_hint in text else ""
    confidence = float(candidate.get("confidence") or 0.55)
    return {
        "title": entry.get("title") or label,
        "markdown_file": entry.get("markdown_file", ""),
        "jlpt_level": entry.get("jlpt_level", ""),
        "confidence": round(min(confidence, 0.86), 2),
        "matched_text": matched_text,
        "matched_markers": [{"marker": label, "start_token": 0, "end_token": 0}] if label else [],
        "formation": entry.get("formation", ""),
        "short_explanation": entry.get("short_explanation", "AI-detected grammar candidate."),
        "long_explanation": entry.get("long_explanation", ""),
        "examples": entry.get("examples", [])[:2],
        "source": "Ollama grammar classifier",
    }


def find_entry_for_candidate_label(label: str, entries: tuple[dict[str, Any], ...]) -> dict[str, Any] | None:
    key = canonical_title(label)
    if not key:
        return None
    fallback = None
    for entry in entries:
        entry_key = canonical_title(str(entry.get("title") or ""))
        formation_key = canonical_title(str(entry.get("formation") or ""))
        if key == entry_key or key == formation_key:
            return entry
        if len(key) >= 3 and (key in entry_key or entry_key in key or key in formation_key):
            fallback = fallback or entry
    return fallback


async def analyze_grammar_with_ollama(
    text: str, structure: list[dict[str, str]], grammar_matches: list[dict[str, Any]] | None = None
) -> str:
    prompt = f"""
/think
You are a Japanese grammar analyst.

Sentence:
{text}

Explain how the sentence works grammatically.
Focus on useful learner-facing analysis: clause structure, particles, verb forms, auxiliaries, conjugations, and natural meaning.
Return a concise plain-text explanation.
""".strip()
    body = {
        "model": OLLAMA_TEXT_MODEL,
        "prompt": prompt,
        "stream": False,

        "options": {"temperature": 0.2, "num_predict": -1, "repeat_penalty": 1.1},
    }
    async with httpx.AsyncClient(timeout=None) as client:
        try:
            response = await client.post(f"{OLLAMA_URL}/api/generate", json=body)
            response.raise_for_status()
            return clean_ollama_final_answer(ollama_text_response(response.json()))
        except Exception as exc:
            print(f"Error calling Ollama: {exc}")
            return "⚠️ Ollama connection failed. Please ensure the local Ollama server is running."


def clean_ollama_final_answer(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.IGNORECASE | re.DOTALL).strip()
    return re.sub(r"^\s*(?:\*\*)?final answer:?(?:\*\*)?\s*", "", text, flags=re.IGNORECASE).strip()


async def analyze_sentence_tree_with_ollama(
    text: str, structure: list[dict[str, str]]
) -> dict[str, Any]:
    prompt = f"""
/think
You are a Japanese sentence analyzer. Output the result in a markdown JSON code block.

Sentence:
{text}

SudachiPy token structure:
{format_structure_for_prompt(structure)}

Create a learner-facing sentence analysis tree inspired by parse-tree language learning tools.
Use this exact JSON shape:
{{
  "summary": "one concise English summary of the sentence structure",
  "tree": {{
    "type": "sentence",
    "value": "the full Japanese sentence",
    "translation": "natural English meaning",
    "role": "sentence",
    "children": [
      {{
        "type": "phrase type such as topic, noun_phrase, verb_phrase, modifier, particle, auxiliary",
        "value": "Japanese span",
        "translation": "English gloss or role",
        "role": "short learner-facing role",
        "children": []
      }}
    ]
  }}
}}

Group adjacent tokens into meaningful phrases when possible. Include particles and auxiliaries as child nodes under the phrase they mark. Keep labels concise.
""".strip()
    body = {
        "model": OLLAMA_TEXT_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.1, "num_predict": -1, "repeat_penalty": 1.1},
    }
    async with httpx.AsyncClient(timeout=None) as client:
        try:
            response = await client.post(f"{OLLAMA_URL}/api/generate", json=body)
            response.raise_for_status()
            content = ollama_text_response(response.json())
            parsed = parse_sentence_analysis_json(content)
            return parsed if parsed else fallback_sentence_analysis(text, structure)
        except Exception as exc:
            print(f"Error calling Ollama: {exc}")
            return fallback_sentence_analysis(text, structure)


async def answer_grammar_question_with_ollama(
    text: str, grammar_question: str
) -> str:
    prompt = f"""
/think
You are a Japanese grammar tutor.

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

        "options": {"temperature": 0.2, "num_predict": -1, "repeat_penalty": 1.1},
    }
    async with httpx.AsyncClient(timeout=None) as client:
        try:
            response = await client.post(f"{OLLAMA_URL}/api/generate", json=body)
            response.raise_for_status()
            return clean_ollama_final_answer(ollama_text_response(response.json()))
        except Exception as exc:
            print(f"Error calling Ollama: {exc}")
            return "⚠️ Ollama connection failed. Please ensure the local Ollama server is running."


def ollama_text_response(payload: dict[str, Any]) -> str:
    response = str(payload.get("response") or "").strip()
    if response:
        return response
    return str(payload.get("thinking") or "").strip()


def parse_sentence_analysis_json(content: str) -> dict[str, Any] | None:
    if not content:
        return None
    try:
        payload = json.loads(content)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if not match:
            return None
        try:
            payload = json.loads(match.group(0))
        except json.JSONDecodeError:
            return None
    if not isinstance(payload, dict):
        return None
    tree = payload.get("tree")
    if not isinstance(tree, dict):
        return None
    return {
        "summary": str(payload.get("summary") or "").strip(),
        "tree": normalize_tree_node(tree),
        "source": "ollama",
    }


def normalize_tree_node(node: dict[str, Any]) -> dict[str, Any]:
    children = node.get("children")
    return {
        "type": str(node.get("type") or "phrase"),
        "value": str(node.get("value") or ""),
        "translation": str(node.get("translation") or ""),
        "role": str(node.get("role") or ""),
        "children": [
            normalize_tree_node(child)
            for child in children
            if isinstance(child, dict)
        ] if isinstance(children, list) else [],
    }


def fallback_sentence_analysis(text: str, structure: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "summary": "Token-based sentence structure. Full phrase grouping requires grammar analysis.",
        "source": "tokenizer",
        "tree": {
            "type": "sentence",
            "value": text,
            "translation": "",
            "role": "sentence",
            "children": [
                {
                    "type": item.get("role") or "token",
                    "value": item.get("surface") or "",
                    "translation": item.get("lemma") or "",
                    "role": item.get("pos") or item.get("role") or "",
                    "children": [],
                }
                for item in structure
            ],
        },
    }


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


def format_grammar_matches_for_prompt(matches: list[dict[str, Any]]) -> str:
    if not matches:
        return "(none)"
    lines = []
    for match in matches[:6]:
        lines.append(
            "- {title} | level={level} | confidence={confidence} | matched={matched} | formation={formation} | explanation={explanation}".format(
                title=match.get("title", ""),
                level=match.get("jlpt_level", ""),
                confidence=match.get("confidence", ""),
                matched=match.get("matched_text", ""),
                formation=match.get("formation", ""),
                explanation=match.get("short_explanation", ""),
            )
        )
    return "\n".join(lines)


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
