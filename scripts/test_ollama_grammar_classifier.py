#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
import time
import urllib.request
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.app import OLLAMA_TEXT_MODEL, OLLAMA_URL, tokenize
from backend.grammar_matcher import (
    DEFAULT_GRAMMAR_DIR,
    build_entry_index,
    load_grammar_entries,
    match_grammar_points,
    normalize_classifier_label,
    recover_classifier_candidates,
)

CASES = [
    {
        "text": "ピザよりハンバーガーのほうが美味しい。",
        "expected": ["より", "のほうが"],
    },
    {
        "text": "明日までに宿題をしなければならない。",
        "expected": ["なければならない", "までに"],
    },
    {
        "text": "母に野菜を食べさせられた。",
        "expected": ["られた"],
    },
    {
        "text": "基本のコーディネイトを違う商品で組んでみてもいいかもね。",
        "expected": ["組んでみ", "組んでみてもいい", "かも", "違う商品で"],
    },
]

KNOWN_LABELS = [
    "AよりBのほうが",
    "Vてみる",
    "Vてもいい",
    "かも",
    "かもしれない",
    "で",
    "までに",
    "なければならない",
    "られる/られた",
    "受身",
    "使役受身",
    "ている",
    "ことができる",
    "たことがある",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Try Ollama as a grammar-label classifier and recover spans with local rules.")
    parser.add_argument("--model", default=os.getenv("OLLAMA_TEXT_MODEL", OLLAMA_TEXT_MODEL))
    parser.add_argument("--url", default=os.getenv("OLLAMA_URL", OLLAMA_URL))
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--report", type=Path, default=Path("tmp/ollama_grammar_classifier_report.json"))
    args = parser.parse_args()

    entries = load_grammar_entries(str(DEFAULT_GRAMMAR_DIR))
    entry_index = build_entry_index(entries)
    report: list[dict[str, Any]] = []

    for case in CASES:
        text = case["text"]
        tokens = tokenize(text)
        baseline = match_grammar_points(text, tokens, tokenize, limit=12)
        start = time.time()
        candidates = classify_with_ollama(text, args.model, args.url, args.timeout)
        elapsed = time.time() - start
        labels = normalize_candidate_labels(candidates)
        recovered = recover_classifier_candidates(tokens, labels, entry_index, skip_labels=set())

        row = {
            "text": text,
            "elapsed_sec": round(elapsed, 3),
            "raw_candidates": candidates,
            "normalized_labels": labels,
            "recovered": [compact_match(match) for match in recovered],
            "baseline": [compact_match(match) for match in baseline],
        }
        report.append(row)
        print_case(row)

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\nreport=", args.report)
    return 0


def classify_with_ollama(text: str, model: str, url: str, timeout: int) -> list[dict[str, Any]]:
    prompt = f"""
/no_think
You are a Japanese grammar point detector. Return only valid JSON, no markdown.

Detect learner-facing Japanese grammar points in the sentence. Do not explain the full sentence.
Prefer labels from this known list when applicable:
{', '.join(KNOWN_LABELS)}

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
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "format": "json",
        "options": {"temperature": 0.0, "num_predict": 700, "repeat_penalty": 1.05},
    }
    data = json.dumps(body).encode("utf-8")
    request = urllib.request.Request(f"{url.rstrip('/')}/api/generate", data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = json.loads(response.read().decode("utf-8"))
    content = str(payload.get("response") or "")
    try:
        parsed = json.loads(content)
    except json.JSONDecodeError:
        return [{"label": "parse_error", "span_hint": "", "confidence": 0.0, "raw": content}]
    candidates = parsed.get("candidates", []) if isinstance(parsed, dict) else []
    return [item for item in candidates if isinstance(item, dict)]


def normalize_candidate_labels(candidates: list[dict[str, Any]]) -> list[str]:
    labels: list[str] = []
    for candidate in candidates:
        label = str(candidate.get("label") or "")
        labels.extend(normalize_classifier_label(label))
    seen = set()
    result = []
    for label in labels:
        if label and label not in seen:
            seen.add(label)
            result.append(label)
    return result


def compact_match(match: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": match.get("title", ""),
        "matched_text": match.get("matched_text", ""),
        "confidence": match.get("confidence", 0),
        "source": match.get("source", ""),
    }


def print_case(row: dict[str, Any]) -> None:
    print("---", row["text"])
    print("elapsed_sec=", row["elapsed_sec"])
    print("raw_candidates=", row["raw_candidates"])
    print("normalized_labels=", row["normalized_labels"])
    print("recovered=")
    for match in row["recovered"]:
        print("  ", match["title"], "=>", match["matched_text"], match["confidence"], match["source"])
    print("baseline=")
    for match in row["baseline"]:
        print("  ", match["title"], "=>", match["matched_text"], match["confidence"], match["source"])


if __name__ == "__main__":
    raise SystemExit(main())
