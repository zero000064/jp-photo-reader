#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import time
import urllib.request
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.app import OLLAMA_TEXT_MODEL, OLLAMA_URL, classify_grammar_points_with_ollama, ollama_candidate_to_match, tokenize
from backend.grammar_matcher import (
    DEFAULT_GRAMMAR_DIR,
    DEFAULT_MARKDOWN_DIR,
    canonical_title,
    load_grammar_entries,
    match_grammar_points,
    normalize_japanese_text,
)

JAPANESE_RE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]")
JAPANESE_CHUNK_RE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]+")
SENTENCE_END_RE = re.compile(r"[。！？?]$")
INLINE_MARKDOWN_RE = re.compile(r"[*_`]+")
LEADING_MARKDOWN_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+|#+\s*)")
ROMAJI_LINE_RE = re.compile(r"^[\s*_`'\-A-Za-zāīūēōĀĪŪĒŌ.,!?;:()]+$")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit grammar matching against Hanabira markdown example sentences.")
    parser.add_argument("--markdown-dir", type=Path, default=DEFAULT_MARKDOWN_DIR)
    parser.add_argument("--examples-per-file", type=int, default=1)
    parser.add_argument("--limit-files", type=int, default=0)
    parser.add_argument("--limit", type=int, default=12, help="Matcher result limit per example.")
    parser.add_argument("--report", type=Path, default=Path("tmp/hanabira_markdown_example_report.json"))
    parser.add_argument("--use-ollama-classifier", action="store_true", help="Call Ollama for examples that fail the normal matcher.")
    parser.add_argument("--ollama-model", default=os.getenv("OLLAMA_TEXT_MODEL", OLLAMA_TEXT_MODEL))
    parser.add_argument("--ollama-url", default=os.getenv("OLLAMA_URL", OLLAMA_URL))
    parser.add_argument("--ollama-timeout", type=int, default=90)
    parser.add_argument("--fail-under", type=float, default=0.0, help="Exit nonzero when pass rate is below this ratio.")
    parser.add_argument("--rerun-failed-report", type=Path, help="Only rerun failed entries from an existing report and update that report in place.")
    args = parser.parse_args()

    if args.rerun_failed_report:
        return rerun_failed_report(args)

    files = sorted(args.markdown_dir.glob("*.md"))
    if args.limit_files > 0:
        files = files[: args.limit_files]

    results: list[dict[str, Any]] = []
    skipped = []

    for path in files:
        title = read_markdown_title(path)
        expected_keys = expected_keys_for(path, title)
        examples = extract_japanese_examples(path.read_text(encoding="utf-8", errors="replace"), title, path)[: args.examples_per_file]
        if not examples:
            skipped.append({"markdown_file": path.name, "title": title, "reason": "no Japanese example sentence found"})
            continue

        file_pass = False
        example_results = []
        for example in examples:
            matches = match_grammar_points(example, tokenize(example), tokenize, limit=args.limit)
            passed = any(match_satisfies_expected(match, expected_keys) for match in matches)
            ollama_candidates: list[dict[str, Any]] = []
            ollama_elapsed = 0.0
            ollama_passed = False
            if not passed and args.use_ollama_classifier:
                start = time.time()
                ollama_candidates, ollama_matches = classify_with_backend_ollama(example, args.ollama_timeout)
                ollama_elapsed = time.time() - start
                ollama_passed = any(candidate_satisfies_expected(candidate, expected_keys) for candidate in ollama_candidates) or any(match_satisfies_expected(match, expected_keys) for match in ollama_matches)
                if ollama_matches:
                    matches = ollama_matches
                passed = ollama_passed
            file_pass = file_pass or passed
            example_results.append({
                "sentence": example,
                "passed": passed,
                "matched_by": "normal" if passed and not ollama_passed else "ollama" if ollama_passed else "none",
                "matches": [compact_match(match) for match in matches],
                "ollama_candidates": ollama_candidates,
                "ollama_elapsed_sec": round(ollama_elapsed, 3) if ollama_elapsed else 0,
            })

        results.append({
            "markdown_file": path.name,
            "title": title,
            "passed": file_pass,
            "examples": example_results,
        })

    tested = len(results)
    passed = sum(1 for item in results if item["passed"])
    failed = tested - passed
    pass_rate = passed / tested if tested else 0.0

    report = {
        "summary": {
            "markdown_dir": str(args.markdown_dir),
            "files_seen": len(files),
            "tested": tested,
            "passed": passed,
            "failed": failed,
            "skipped": len(skipped),
            "pass_rate": round(pass_rate, 4),
            "examples_per_file": args.examples_per_file,
            "use_ollama_classifier": args.use_ollama_classifier,
        },
        "failed": [item for item in results if not item["passed"]],
        "passed": [item for item in results if item["passed"]],
        "skipped": skipped,
    }

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print_summary(report, args.report)
    if args.fail_under and pass_rate < args.fail_under:
        return 1
    return 0



def rerun_failed_report(args: argparse.Namespace) -> int:
    report_path = args.rerun_failed_report
    report = json.loads(report_path.read_text(encoding="utf-8"))
    failed = report.get("failed", [])
    still_failed = []
    newly_passed = []

    for item in failed:
        title = str(item.get("title") or "")
        markdown_file = str(item.get("markdown_file") or "")
        expected_keys = expected_keys_for(Path(markdown_file), title)
        file_pass = False
        updated_examples = []
        for example_result in item.get("examples", []):
            sentence = str(example_result.get("sentence") or "")
            start = time.time()
            ollama_candidates, ollama_matches = classify_with_backend_ollama(sentence, args.ollama_timeout)
            elapsed = time.time() - start
            passed = any(candidate_satisfies_expected(candidate, expected_keys) for candidate in ollama_candidates) or any(match_satisfies_expected(match, expected_keys) for match in ollama_matches)
            updated = dict(example_result)
            updated.update({
                "passed": passed,
                "matched_by": "ollama" if passed else "none",
                "matches": [compact_match(match) for match in ollama_matches],
                "ollama_candidates": ollama_candidates,
                "ollama_elapsed_sec": round(elapsed, 3),
            })
            updated_examples.append(updated)
            file_pass = file_pass or passed

        updated_item = dict(item)
        updated_item["passed"] = file_pass
        updated_item["examples"] = updated_examples
        if file_pass:
            newly_passed.append(updated_item)
        else:
            still_failed.append(updated_item)

    report["failed"] = still_failed
    report["passed"] = report.get("passed", []) + newly_passed
    summary = report.setdefault("summary", {})
    summary["tested"] = len(report.get("passed", [])) + len(report.get("failed", []))
    summary["passed"] = len(report.get("passed", []))
    summary["failed"] = len(report.get("failed", []))
    summary["pass_rate"] = round(summary["passed"] / summary["tested"], 4) if summary["tested"] else 0.0
    summary["reran_failed_with_backend_catalog_classifier"] = True
    summary["reran_failed_count"] = len(failed)
    summary["newly_passed_from_rerun"] = len(newly_passed)

    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print_summary(report, report_path)
    print("reran_failed=", len(failed), "newly_passed=", len(newly_passed), "still_failed=", len(still_failed))
    return 0


def classify_with_backend_ollama(sentence: str, timeout: int) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    async def run() -> list[dict[str, Any]]:
        return await classify_grammar_points_with_ollama(sentence)

    try:
        candidates = asyncio.run(asyncio.wait_for(run(), timeout=timeout))
    except Exception as exc:
        return ([{"label": "ollama_error", "span_hint": "", "confidence": 0.0, "error": str(exc)}], [])

    entries = load_grammar_entries(str(DEFAULT_GRAMMAR_DIR))
    matches = [ollama_candidate_to_match(candidate, sentence, entries) for candidate in candidates]
    return candidates, matches

def read_markdown_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        stripped = line.strip()
        if stripped.startswith("# Japanese Grammar Point:"):
            return stripped.split(":", 1)[1].strip()
        if stripped.startswith("Processing keyword:"):
            return stripped.split(":", 1)[1].strip()
    return path.stem.replace("_", " ")


def expected_keys_for(path: Path, title: str) -> set[str]:
    keys = {canonical_title(title), canonical_title(path.stem)}
    keys.add(canonical_title(path.stem.replace("_", " ")))
    return {key for key in keys if key}


def extract_japanese_examples(markdown: str, title: str = "", path: Path | None = None) -> list[str]:
    examples: list[str] = []
    seen = set()
    in_code_block = False
    in_examples = False
    target_markers = target_markers_for(title, path)

    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        heading_text = line.lstrip("# ").lower()
        if line.startswith("#"):
            if any(marker in heading_text for marker in ["examples in context", "sentence examples", "examples", "例文"]):
                in_examples = True
                continue
            if in_examples and re.match(r"#+\s*(?:5|6|7|cultural|common|summary|review)", heading_text):
                in_examples = False
        if not in_examples:
            continue
        if line.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        lower = line.lower()
        if line.startswith(">"):
            line = line.lstrip("> ").strip()
        if not line or ROMAJI_LINE_RE.match(line):
            continue
        if "|" in line:
            continue
        if not JAPANESE_RE.search(line):
            continue
        if line.startswith(("Processing keyword:", "# Japanese Grammar Point:")):
            continue
        if any(marker in line for marker in ["Incorrect", "Correction", "Answer:", "Structure", "Formation"]):
            continue

        cleaned = clean_markdown_sentence(line)
        if not cleaned or not JAPANESE_RE.search(cleaned):
            continue
        if not SENTENCE_END_RE.search(cleaned):
            if not in_examples:
                continue
            cleaned = cleaned.rstrip("。！？?") + "。"
        if japanese_char_count(cleaned) < 6 or japanese_ratio(cleaned) < 0.35:
            continue
        key = normalize_japanese_text(cleaned)
        if key in seen:
            continue
        seen.add(key)
        examples.append(cleaned)

    targeted = [example for example in examples if sentence_contains_target_marker(example, target_markers)]
    return targeted or examples


def target_markers_for(title: str, path: Path | None = None) -> list[str]:
    values = [title]
    if path is not None:
        values.extend([path.stem, path.stem.replace("_", " ")])
    markers: list[str] = []
    low_signal = {"が", "は", "を", "に", "へ", "で", "と", "も", "の", "か", "や", "ね", "よ", "だ", "です", "ます", "た", "て", "ない", "する", "ある", "いる", "なる"}
    for value in values:
        for chunk in JAPANESE_CHUNK_RE.findall(value):
            normalized = normalize_japanese_text(chunk)
            if not normalized or normalized in low_signal or len(normalized) < 2:
                continue
            if normalized not in markers:
                markers.append(normalized)
    return markers


def sentence_contains_target_marker(sentence: str, markers: list[str]) -> bool:
    if not markers:
        return False
    normalized = normalize_japanese_text(sentence)
    return any(marker in normalized for marker in markers)


def clean_markdown_sentence(line: str) -> str:
    line = LEADING_MARKDOWN_RE.sub("", line).strip()
    line = INLINE_MARKDOWN_RE.sub("", line).strip()
    line = re.sub(r"<[^>]+>", "", line).strip()
    line = line.replace("❌", "").replace("✅", "").strip()

    # Prefer the side of a separator that actually contains a Japanese sentence.
    for separator in [":", "："]:
        if separator in line:
            left, right = [part.strip() for part in line.split(separator, 1)]
            if japanese_char_count(right) >= japanese_char_count(left):
                line = right
            else:
                line = left
            break

    line = re.sub(r"\s+", "", line)
    for separator in ["（", "(", "-", "–", "—"]:
        if separator in line:
            parts = [part.strip() for part in line.split(separator, 1)]
            line = max(parts, key=japanese_char_count)
            break
    return line.strip()


def japanese_char_count(text: str) -> int:
    return len(JAPANESE_RE.findall(text))


def japanese_ratio(text: str) -> float:
    compact = re.sub(r"\s+", "", text)
    return japanese_char_count(compact) / len(compact) if compact else 0.0


def match_satisfies_expected(match: dict[str, Any], expected_keys: set[str]) -> bool:
    markdown_file = str(match.get("markdown_file") or "")
    title = str(match.get("title") or "")
    keys = {canonical_title(title), canonical_title(markdown_file.removesuffix(".md"))}
    return keys_satisfy_expected(keys, expected_keys)


def candidate_satisfies_expected(candidate: dict[str, Any], expected_keys: set[str]) -> bool:
    label = str(candidate.get("label") or "")
    keys = {canonical_title(label)}
    return keys_satisfy_expected(keys, expected_keys)


def keys_satisfy_expected(keys: set[str], expected_keys: set[str]) -> bool:
    keys = {key for key in keys if key}
    if expected_keys & keys:
        return True
    for key in keys:
        for expected in expected_keys:
            if len(key) >= 2 and len(expected) >= 2 and (key in expected or expected in key):
                return True
    return False


def classify_with_ollama(sentence: str, title: str, model: str, url: str, timeout: int) -> list[dict[str, Any]]:
    prompt = f"""
/no_think
You are a Japanese grammar point detector. Return only valid JSON, no markdown.

The source grammar lesson title is:
{title}

Detect learner-facing Japanese grammar points in the sentence. Return at most 8 candidates. Include candidate labels as concise Japanese grammar point names when possible.

Return this exact JSON shape:
{{
  "candidates": [
    {{"label": "grammar label", "span_hint": "Japanese span in the sentence", "confidence": 0.0}}
  ]
}}

Sentence:
{sentence}
""".strip()
    body = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "format": "json",
        "options": {"temperature": 0.0, "num_predict": 650, "repeat_penalty": 1.05},
    }
    data = json.dumps(body).encode("utf-8")
    request = urllib.request.Request(f"{url.rstrip('/')}/api/generate", data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
        content = str(payload.get("response") or "")
        parsed = json.loads(content)
    except Exception as exc:
        return [{"label": "ollama_error", "span_hint": "", "confidence": 0.0, "error": str(exc)}]
    candidates = parsed.get("candidates", []) if isinstance(parsed, dict) else []
    return [compact_candidate(item) for item in candidates if isinstance(item, dict)]


def compact_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "label": str(candidate.get("label") or ""),
        "span_hint": str(candidate.get("span_hint") or ""),
        "confidence": candidate.get("confidence", 0),
    }


def compact_match(match: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": match.get("title", ""),
        "markdown_file": match.get("markdown_file", ""),
        "matched_text": match.get("matched_text", ""),
        "confidence": match.get("confidence", 0),
        "source": match.get("source", ""),
    }


def print_summary(report: dict[str, Any], report_path: Path) -> None:
    summary = report["summary"]
    print("Hanabira markdown example matcher audit")
    print("tested=", summary["tested"], "passed=", summary["passed"], "failed=", summary["failed"], "skipped=", summary["skipped"], "pass_rate=", summary["pass_rate"])
    print("report=", report_path)
    if report["failed"]:
        print("\nFirst failures:")
        for item in report["failed"][:10]:
            example = item["examples"][0] if item.get("examples") else {}
            print("-", item["markdown_file"], "|", item["title"], "|", example.get("sentence", ""))


if __name__ == "__main__":
    raise SystemExit(main())
