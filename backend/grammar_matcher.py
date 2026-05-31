from __future__ import annotations

import json
import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable

JAPANESE_RE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff\u3005\u30fc]+")
DEFAULT_GRAMMAR_DIR = Path(__file__).resolve().parent / "data" / "hanabira_grammar"
DEFAULT_MARKDOWN_DIR = Path(__file__).resolve().parent / "data" / "hanabira_grammar_markdown"
HANABIRA_ATTRIBUTION = "Grammar reference content from Hanabira.org Japanese Content (Creative Commons)."

LEVEL_WEIGHT = {"N5": 0.05, "N4": 0.04, "N3": 0.03, "N2": 0.02, "N1": 0.01}
CLASSIFIER_MODEL = os.getenv("JPR_GRAMMAR_CLASSIFIER_MODEL", "arvine111/japanese-grammar-classification")
CLASSIFIER_ENABLED = os.getenv("JPR_GRAMMAR_CLASSIFIER", "0").lower() in {"1", "true", "yes"}
CLASSIFIER_LOCAL_ONLY = os.getenv("JPR_GRAMMAR_CLASSIFIER_LOCAL_ONLY", "1").lower() not in {"0", "false", "no"}
CLASSIFIER_TOP_K = int(os.getenv("JPR_GRAMMAR_CLASSIFIER_TOP_K", "6"))
CLASSIFIER_THRESHOLD = float(os.getenv("JPR_GRAMMAR_CLASSIFIER_THRESHOLD", "0.15"))

TokenizeFn = Callable[[str], list[dict[str, str]]]


def match_grammar_points(
    text: str,
    tokens: list[dict[str, Any]],
    tokenize_fn: TokenizeFn,
    limit: int = 8,
    grammar_dir: Path = DEFAULT_GRAMMAR_DIR,
) -> list[dict[str, Any]]:
    entries = load_grammar_entries(str(grammar_dir))
    if not entries or not tokens:
        return []

    token_surfaces = [str(token.get("surface") or "") for token in tokens]
    token_roles = [str(token.get("pos_group") or token.get("role") or "") for token in tokens]
    normalized_text = normalize_japanese_text(text)
    matches: list[dict[str, Any]] = []
    entry_index = build_entry_index(entries)
    rule_matches = apply_marker_token_overrides(tokens, entry_index)
    matches.extend(rule_matches)
    recovered_labels = {str(match.get("rule_label") or "") for match in rule_matches}
    matches.extend(recover_classifier_candidates(tokens, infer_classifier_candidates(text, tokens), entry_index, recovered_labels))

    for entry in entries:
        for formation_match in match_formation_patterns(entry, tokens):
            matches.append(formation_match)

        for marker in entry["markers"]:
            spans = evaluate_marker_ast(token_surfaces, marker)
            for start, end in spans:
                marker_str = json.dumps(marker, ensure_ascii=False) if isinstance(marker, dict) else str(marker)
                marker_matches = [{"marker": marker_str, "start_token": start + 1, "end_token": end}]
                
                span_start = start
                span_end = end
                matched_text = "".join(token_surfaces[span_start:span_end])
                confidence = score_match(entry, marker_matches, matched_text, normalized_text, token_roles, span_start, span_end)
                if confidence < 0.58:
                    continue

                matches.append(
                    {
                        "title": entry["title"],
                        "markdown_file": entry.get("markdown_file", ""),
                        "jlpt_level": entry["jlpt_level"],
                        "confidence": round(min(confidence, 0.99), 2),
                        "matched_text": matched_text,
                        "matched_markers": marker_matches,
                        "formation": entry.get("formation", ""),
                        "short_explanation": entry.get("short_explanation", ""),
                        "long_explanation": entry.get("long_explanation", ""),
                        "examples": entry.get("examples", [])[:2],
                        "source": "Hanabira.org Japanese Content",
                    }
                )

    matches.sort(key=lambda item: (item["confidence"], len(item["matched_text"]), -jlpt_sort(item["jlpt_level"])), reverse=True)
    return remove_contained_matches(dedupe_matches(matches))[:limit]


def build_entry_index(entries: tuple[dict[str, Any], ...]) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    aliases = {
        "te_miru": ["てみる"],
        "temo_ii": ["てもいい"],
        "kamo": ["かもしれない"],
    }
    for key, needles in aliases.items():
        for entry in entries:
            haystack = normalize_japanese_text(entry.get("title", "") + entry.get("formation", ""))
            if any(needle in haystack for needle in needles):
                index.setdefault(key, entry)
                break
    return index


def apply_marker_token_overrides(tokens: list[dict[str, Any]], entry_index: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    for span in find_te_miru_spans(tokens):
        matches.append(evaluate_with_token_overrides("te_miru", span, tokens, entry_index, 0.86))
    for span in find_temo_ii_spans(tokens):
        matches.append(evaluate_with_token_overrides("temo_ii", span, tokens, entry_index, 0.88))
    for span in find_kamo_spans(tokens):
        matches.append(evaluate_with_token_overrides("kamo", span, tokens, entry_index, 0.78))
    for span in find_instrumental_de_spans(tokens):
        matches.append(evaluate_with_token_overrides("instrumental_de", span, tokens, entry_index, 0.7))
    # Filter out Nones
    return [m for m in matches if m is not None]


def infer_classifier_candidates(text: str, tokens: list[dict[str, Any]]) -> list[str]:
    candidates: list[str] = []
    candidates.extend(predict_classifier_labels(text))

    # Deterministic candidates keep the recovery path exercised even when the
    # optional Hugging Face classifier is disabled or unavailable.
    if find_te_miru_spans(tokens):
        candidates.append("te_miru")
    if find_temo_ii_spans(tokens):
        candidates.append("temo_ii")
    if find_kamo_spans(tokens):
        candidates.append("kamo")
    if find_instrumental_de_spans(tokens):
        candidates.append("instrumental_de")
    return dedupe_labels(candidates)


def predict_classifier_labels(text: str) -> list[str]:
    classifier = get_classifier_pipeline()
    if classifier is None:
        return []
    try:
        raw = classifier(text, top_k=CLASSIFIER_TOP_K, truncation=True)
    except Exception:
        return []

    labels: list[str] = []
    for item in flatten_classifier_output(raw):
        score = float(item.get("score") or 0)
        if score < CLASSIFIER_THRESHOLD:
            continue
        labels.extend(normalize_classifier_label(str(item.get("label") or "")))
    return dedupe_labels(labels)


@lru_cache(maxsize=1)
def get_classifier_pipeline() -> Any | None:
    if not CLASSIFIER_ENABLED:
        return None
    try:
        from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
    except Exception:
        return None
    try:
        tokenizer = AutoTokenizer.from_pretrained(CLASSIFIER_MODEL, local_files_only=CLASSIFIER_LOCAL_ONLY)
        model = AutoModelForSequenceClassification.from_pretrained(CLASSIFIER_MODEL, local_files_only=CLASSIFIER_LOCAL_ONLY)
        return pipeline("text-classification", model=model, tokenizer=tokenizer)
    except Exception:
        return None


def flatten_classifier_output(raw: Any) -> list[dict[str, Any]]:
    if isinstance(raw, dict):
        return [raw]
    if not isinstance(raw, list):
        return []
    if raw and isinstance(raw[0], list):
        return [item for group in raw for item in group if isinstance(item, dict)]
    return [item for item in raw if isinstance(item, dict)]


def normalize_classifier_label(label: str) -> list[str]:
    normalized = normalize_japanese_text(label).lower()
    mapped: list[str] = []
    if any(part in normalized for part in ["てみる", "temiru", "temiru", "try"]):
        mapped.append("te_miru")
    if any(part in normalized for part in ["てもいい", "temoii", "temo ii", "もいい"]):
        mapped.append("temo_ii")
    if any(part in normalized for part in ["かもしれない", "かも", "kamoshirenai", "kamo"]):
        mapped.append("kamo")
    if normalized in {"で", "de"} or "instrument" in normalized or "means" in normalized or "bymeans" in normalized:
        mapped.append("instrumental_de")
    return mapped or ["classifier:" + label.strip()] if label.strip() else []


def dedupe_labels(labels: list[str]) -> list[str]:
    seen = set()
    result = []
    for label in labels:
        if not label or label in seen:
            continue
        seen.add(label)
        result.append(label)
    return result


def recover_classifier_candidates(
    tokens: list[dict[str, Any]],
    candidate_labels: list[str],
    entry_index: dict[str, dict[str, Any]],
    skip_labels: set[str] | None = None,
) -> list[dict[str, Any]]:
    recovered: list[dict[str, Any]] = []
    finders = {
        "te_miru": find_te_miru_spans,
        "temo_ii": find_temo_ii_spans,
        "kamo": find_kamo_spans,
        "instrumental_de": find_instrumental_de_spans,
    }
    skip_labels = skip_labels or set()
    for label in candidate_labels:
        if label in skip_labels:
            continue
        finder = finders.get(label)
        if not finder:
            recovered.append(possible_classifier_match(label))
            continue
        spans = finder(tokens)
        if spans:
            for span in spans:
                match = evaluate_with_token_overrides(label, span, tokens, entry_index, 0.72, source="Classifier candidate + span recovery")
                if match is not None:
                    recovered.append(match)
        else:
            recovered.append(possible_classifier_match(label))
    return recovered


def find_te_miru_spans(tokens: list[dict[str, Any]]) -> list[tuple[int, int]]:
    spans = []
    for i in range(len(tokens) - 2):
        if is_verb(tokens[i]) and surface(tokens[i + 1]) in {"て", "で"} and lemma(tokens[i + 2]) == "みる":
            spans.append((i, i + 3))
    return spans


def find_temo_ii_spans(tokens: list[dict[str, Any]]) -> list[tuple[int, int]]:
    spans = []
    for i in range(len(tokens) - 3):
        if is_verb(tokens[i]) and surface(tokens[i + 1]) in {"て", "で"} and surface(tokens[i + 2]) == "も" and lemma(tokens[i + 3]) in {"いい", "よい", "良い"}:
            spans.append((i, i + 4))
    for i in range(len(tokens) - 5):
        if (
            is_verb(tokens[i])
            and surface(tokens[i + 1]) in {"て", "で"}
            and lemma(tokens[i + 2]) == "みる"
            and surface(tokens[i + 3]) in {"て", "で"}
            and surface(tokens[i + 4]) == "も"
            and lemma(tokens[i + 5]) in {"いい", "よい", "良い"}
        ):
            spans.append((i, i + 6))
    return spans


def find_kamo_spans(tokens: list[dict[str, Any]]) -> list[tuple[int, int]]:
    spans = []
    for i in range(len(tokens) - 1):
        if surface(tokens[i]) == "か" and surface(tokens[i + 1]) == "も":
            after = [surface(token) for token in tokens[i + 2: i + 4]]
            if not after or all(item in {"ね", "よ", "。", "！", "？"} for item in after):
                spans.append((i, i + 2))
    return spans


def find_instrumental_de_spans(tokens: list[dict[str, Any]]) -> list[tuple[int, int]]:
    spans = []
    for i in range(1, len(tokens) - 1):
        if surface(tokens[i]) != "で" or not is_noun(tokens[i - 1]):
            continue
        if "接続助詞" in str(tokens[i].get("pos") or ""):
            continue
        if any(is_verb(token) for token in tokens[i + 1: min(len(tokens), i + 5)]):
            start = i - 1
            while start > 0 and (is_noun_modifier(tokens[start - 1]) or surface(tokens[start - 1]) == "の"):
                start -= 1
            spans.append((start, i + 1))
    return spans


def evaluate_with_token_overrides(
    label: str,
    span: tuple[int, int],
    tokens: list[dict[str, Any]],
    entry_index: dict[str, dict[str, Any]],
    confidence: float,
    source: str = "AST Token Override",
) -> dict[str, Any] | None:
    entry = entry_index.get(label, {})
    if not entry:
        return None
        
    start, end = span
    fallback = fallback_rule_metadata(label)
    title = entry.get("title") or fallback["title"]
    
    target_string_map = {
        "te_miru": "てみる",
        "temo_ii": "てもいい",
        "kamo": "かもしれない",
        "instrumental_de": "で"
    }
    target_str = target_string_map.get(label)
    
    # Strictly enforce the AST using the token rule override
    if entry.get("markers"):
        valid_match = False
        override = {target_str: [span]} if target_str else {}
        token_surfaces = [surface(t) for t in tokens]
        
        for marker in entry["markers"]:
            ast_spans = evaluate_marker_ast(token_surfaces, marker, override_spans=override)
            if ast_spans:
                valid_match = True
                start, end = ast_spans[0]
                break
                
        if not valid_match:
            return None
            
    return {
        "title": title,
        "markdown_file": entry.get("markdown_file", ""),
        "jlpt_level": entry.get("jlpt_level") or fallback.get("jlpt_level", ""),
        "confidence": confidence,
        "matched_text": "".join(surface(token) for token in tokens[start:end]),
        "matched_markers": [{"marker": fallback["marker"], "start_token": start + 1, "end_token": end}],
        "formation": entry.get("formation") or fallback.get("formation", ""),
        "short_explanation": entry.get("short_explanation") or fallback.get("short_explanation", ""),
        "long_explanation": entry.get("long_explanation") or fallback.get("long_explanation", ""),
        "examples": entry.get("examples", [])[:2],
        "source": source,
        "rule_label": label,
    }


def fallback_rule_metadata(label: str) -> dict[str, str]:
    return {
        "te_miru": {
            "title": "Vてみる",
            "marker": "てみる",
            "formation": "Verb te-form + みる",
            "short_explanation": "Try doing something.",
            "long_explanation": "Used after a verb in te-form to mean trying an action to see what happens.",
            "jlpt_level": "N4",
        },
        "temo_ii": {
            "title": "Vてもいい",
            "marker": "てもいい",
            "formation": "Verb te-form + も + いい",
            "short_explanation": "It is okay to do something.",
            "long_explanation": "Used to express permission or acceptability of doing an action.",
            "jlpt_level": "N5",
        },
        "kamo": {
            "title": "かも / かもしれない",
            "marker": "かも",
            "formation": "Plain clause + かも",
            "short_explanation": "Maybe; might.",
            "long_explanation": "A casual shortened form of かもしれない used to express possibility.",
            "jlpt_level": "N4",
        },
        "instrumental_de": {
            "title": "で",
            "marker": "で",
            "formation": "Noun + で + action",
            "short_explanation": "Using; by means of.",
            "long_explanation": "The particle で can mark the means, tool, or material used for an action.",
            "jlpt_level": "N5",
        },
    }.get(label, {"title": label, "marker": label})


def possible_classifier_match(label: str) -> dict[str, Any]:
    meta = fallback_rule_metadata(label)
    return {
        "title": meta["title"],
        "markdown_file": "",
        "jlpt_level": meta.get("jlpt_level", ""),
        "confidence": 0.4,
        "matched_text": "",
        "matched_markers": [],
        "formation": meta.get("formation", ""),
        "short_explanation": "Possible grammar candidate, but no reliable span was recovered.",
        "long_explanation": meta.get("long_explanation", ""),
        "examples": [],
        "source": "Classifier candidate",
        "rule_label": label,
    }


def surface(token: dict[str, Any]) -> str:
    return str(token.get("surface") or "")


def lemma(token: dict[str, Any]) -> str:
    return str(token.get("lemma") or "")


def is_verb(token: dict[str, Any]) -> bool:
    return str(token.get("pos_group") or token.get("role") or "") == "verb"


def is_noun(token: dict[str, Any]) -> bool:
    return str(token.get("pos_group") or token.get("role") or "") in {"noun", "pronoun"}


def is_noun_modifier(token: dict[str, Any]) -> bool:
    return is_noun(token) or str(token.get("pos_group") or token.get("role") or "") in {"adjective", "verb"}


@lru_cache(maxsize=4)
def load_grammar_entries(grammar_dir: str) -> tuple[dict[str, Any], ...]:
    root = Path(grammar_dir)
    if not root.exists():
        return ()

    entries: list[dict[str, Any]] = []
    markdown_index = load_markdown_index(str(DEFAULT_MARKDOWN_DIR))
    for path in sorted(root.glob("grammar_ja_N*_full_alphabetical_*.json")):
        level_match = re.search(r"grammar_ja_(N[1-5])_", path.name)
        level = level_match.group(1) if level_match else ""
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(data, list):
            continue
        for index, raw in enumerate(data):
            if not isinstance(raw, dict):
                continue
            entry = normalize_entry(raw, level, index, markdown_index)
            if entry["markers"]:
                entries.append(entry)
    return tuple(entries)


@lru_cache(maxsize=4)
def load_markdown_index(markdown_dir: str) -> dict[str, str]:
    root = Path(markdown_dir)
    if not root.exists():
        return {}
    index: dict[str, str] = {}
    for path in sorted(root.glob("*.md")):
        key = canonical_title(path.stem)
        if key and key not in index:
            index[key] = path.name
    return index


def read_grammar_markdown(markdown_file: str, markdown_dir: Path = DEFAULT_MARKDOWN_DIR) -> dict[str, str]:
    if not markdown_file or Path(markdown_file).name != markdown_file or not markdown_file.endswith(".md"):
        return {}
    path = markdown_dir / markdown_file
    try:
        markdown = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    return {
        "markdown_file": markdown_file,
        "title": markdown_file.removesuffix(".md").replace("_", " "),
        "markdown": markdown,
        "source": "Hanabira.org Japanese Content",
        "attribution": HANABIRA_ATTRIBUTION,
    }


def normalize_entry(raw: dict[str, Any], level: str, index: int, markdown_index: dict[str, str] | None = None) -> dict[str, Any]:
    title = str(raw.get("title") or "").strip()
    formation = str(raw.get("formation") or "").strip()
    examples = raw.get("examples") if isinstance(raw.get("examples"), list) else []
    
    markers = raw.get("llm_markers", [])
    formation_patterns = raw.get("llm_formation_patterns", [])

    markdown_file = (markdown_index or {}).get(canonical_title(title), "")
    return {
        "id": f"{level}-{index + 1}",
        "jlpt_level": level,
        "title": title,
        "markdown_file": markdown_file,
        "short_explanation": str(raw.get("short_explanation") or "").strip(),
        "long_explanation": str(raw.get("long_explanation") or "").strip(),
        "formation": formation,
        "examples": [example for example in examples if isinstance(example, dict)],
        "markers": markers,
        "formation_patterns": formation_patterns,
    }






def match_formation_patterns(entry: dict[str, Any], tokens: list[dict[str, Any]]) -> list[dict[str, Any]]:
    patterns = entry.get("formation_patterns") or []
    if not patterns:
        return []
    matches = []
    for pattern in patterns:
        for start in range(len(tokens)):
            found = match_formation_at(pattern, tokens, start)
            if not found:
                continue
            end, marker_matches = found
            if end <= start:
                continue
            matches.append({
                "title": entry["title"],
                "markdown_file": entry.get("markdown_file", ""),
                "jlpt_level": entry["jlpt_level"],
                "confidence": 0.84,
                "matched_text": "".join(surface(token) for token in tokens[start:end]),
                "matched_markers": marker_matches,
                "formation": entry.get("formation", ""),
                "short_explanation": entry.get("short_explanation", ""),
                "long_explanation": entry.get("long_explanation", ""),
                "examples": entry.get("examples", [])[:2],
                "source": "Hanabira formation pattern",
            })
            break
    return matches[:2]


def match_formation_at(pattern: list[dict[str, str]], tokens: list[dict[str, Any]], start: int) -> tuple[int, list[dict[str, Any]]] | None:
    index = start
    variables: dict[str, str] = {}
    marker_matches: list[dict[str, Any]] = []
    for part in pattern:
        index = skip_punctuation(tokens, index)
        if index >= len(tokens):
            return None
            
        token = tokens[index]
        if not isinstance(part, dict):
            return None
        kind = part.get("kind")
        
        if kind == "slot":
            if not token_matches_slot(token, part):
                return None
            var = part.get("var", "")
            value = normalize_japanese_text(surface(tokens[index]))
            if var:
                if part.get("repeat") and variables.get(var) != value:
                    return None
                if var in variables and variables[var] != value:
                    return None
                variables.setdefault(var, value)
            marker_matches.append({"marker": part.get("var") or part.get("pos"), "start_token": index + 1, "end_token": index + 1})
            index += 1
            continue

        literal = part.get("text", "")
        matched = match_literal_at(tokens, literal, index)
        if matched is None:
            return None
        literal_start, literal_end = matched
        marker_matches.append({"marker": literal, "start_token": literal_start + 1, "end_token": literal_end})
        index = literal_end

    if len(pattern) < 3:
        return None
    return index, marker_matches


def token_matches_slot(token: dict[str, Any], part: dict[str, str]) -> bool:
    expected = part.get("pos")
    role = str(token.get("pos_group") or token.get("role") or "")
    if expected == "noun":
        return role in {"noun", "pronoun"}
    if expected == "verb":
        return role == "verb"
    if expected == "adjective":
        return role in {"adjective", "adjectival noun"}
    return True


def match_literal_at(tokens: list[dict[str, Any]], literal: str, start: int) -> tuple[int, int] | None:
    if not literal:
        return None
    max_len = min(max(len(literal), 1), 8)
    for end in range(start + 1, min(len(tokens), start + max_len) + 1):
        if normalize_japanese_text("".join(surface(token) for token in tokens[start:end])) == literal:
            return start, end
    return None


def skip_punctuation(tokens: list[dict[str, Any]], index: int) -> int:
    while index < len(tokens) and str(tokens[index].get("pos_group") or tokens[index].get("role") or "") == "punctuation":
        index += 1
    return index




def find_marker_spans(token_surfaces: list[str], marker: str) -> list[tuple[int, int]]:
    if not marker:
        return []
    
    joined_text = "".join(token_surfaces)
    char_starts = []
    char_ends = []
    current = 0
    for surf in token_surfaces:
        char_starts.append(current)
        current += len(surf)
        char_ends.append(current)
        
    spans = []
    start_idx = 0
    while True:
        idx = joined_text.find(marker, start_idx)
        if idx == -1:
            break
        
        start_token = -1
        end_token = -1
        for i in range(len(token_surfaces)):
            if char_starts[i] <= idx < char_ends[i]:
                start_token = i
            if char_starts[i] < idx + len(marker) <= char_ends[i]:
                end_token = i
                
        if start_token != -1 and end_token != -1:
            spans.append((start_token, end_token + 1))
            
        start_idx = idx + 1
        
    return spans


def evaluate_marker_ast(token_surfaces: list[str], marker: Any, override_spans: dict[str, list[tuple[int, int]]] | None = None) -> list[tuple[int, int]]:
    override_spans = override_spans or {}
    
    if isinstance(marker, str):
        if marker in override_spans:
            return override_spans[marker]
        return find_marker_spans(token_surfaces, marker)
    elif isinstance(marker, dict):
        if "AND" in marker:
            spans = None
            for child in marker["AND"]:
                child_spans = evaluate_marker_ast(token_surfaces, child, override_spans)
                if not child_spans:
                    return []
                if spans is None:
                    spans = child_spans
                else:
                    new_spans = []
                    for s1, e1 in spans:
                        for s2, e2 in child_spans:
                            # Strict sequential AND: the second token must appear at or after the first token ends
                            if e1 <= s2:
                                new_spans.append((s1, e2))
                    spans = new_spans
            return spans or []
        elif "OR" in marker:
            spans = []
            for child in marker["OR"]:
                spans.extend(evaluate_marker_ast(token_surfaces, child, override_spans))
            return spans
    return []


def score_match(
    entry: dict[str, Any],
    marker_matches: list[dict[str, Any]],
    matched_text: str,
    normalized_text: str,
    token_roles: list[str],
    span_start: int,
    span_end: int,
) -> float:
    confidence = 0.38
    confidence += min(0.22, 0.06 * len(marker_matches))
    confidence += min(0.15, len(matched_text) / 60)
    confidence += LEVEL_WEIGHT.get(entry.get("jlpt_level", ""), 0)
    if normalize_japanese_text(matched_text) in normalized_text:
        confidence += 0.08
    confidence += pos_hint_bonus(entry.get("formation", "") + " " + entry.get("title", ""), token_roles, span_start, span_end)
    if example_overlap(entry.get("examples", []), normalized_text):
        confidence += 0.08
    return confidence


def pos_hint_bonus(pattern_text: str, token_roles: list[str], span_start: int, span_end: int) -> float:
    nearby = set(token_roles[max(0, span_start - 2): min(len(token_roles), span_end + 2)])
    bonus = 0.0
    if "Verb" in pattern_text and "verb" in nearby:
        bonus += 0.04
    if "Noun" in pattern_text and ("noun" in nearby or "pronoun" in nearby):
        bonus += 0.04
    if "Adjective" in pattern_text and ("adjective" in nearby or "adjectival noun" in nearby):
        bonus += 0.04
    return min(bonus, 0.1)


def example_overlap(examples: list[dict[str, Any]], normalized_text: str) -> bool:
    for example in examples[:4]:
        jp = normalize_japanese_text(str(example.get("jp") or ""))
        if len(jp) >= 6 and (jp in normalized_text or normalized_text in jp):
            return True
    return False


def normalize_japanese_text(text: str) -> str:
    return re.sub(r"[\s\u3000、。,.!?！？\-ー]+", "", text)


def dedupe_matches(matches: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen = set()
    unique = []
    for match in matches:
        key = (canonical_title(match["title"]), match["matched_text"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(match)
    return unique


def remove_contained_matches(matches: list[dict[str, Any]]) -> list[dict[str, Any]]:
    filtered = []
    for match in matches:
        text = normalize_japanese_text(str(match.get("matched_text") or ""))
        title = canonical_title(str(match.get("title") or ""))
        if text and any(
            title == canonical_title(str(kept.get("title") or ""))
            and text != normalize_japanese_text(str(kept.get("matched_text") or ""))
            and text in normalize_japanese_text(str(kept.get("matched_text") or ""))
            for kept in filtered
        ):
            continue
        filtered.append(match)
    return filtered


def canonical_title(title: str) -> str:
    return re.sub(r"[\s\u3000～〜()（）A-Za-z0-9_.+\-]+", "", title)


def jlpt_sort(level: str) -> int:
    try:
        return int(level.removeprefix("N"))
    except ValueError:
        return 9
