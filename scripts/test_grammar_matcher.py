#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.app import tokenize
from backend.grammar_matcher import match_grammar_points


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


def main() -> int:
    failures = []
    for case in CASES:
        text = case["text"]
        matches = match_grammar_points(text, tokenize(text), tokenize, limit=12)
        matched_texts = [match.get("matched_text", "") for match in matches]
        print("---", text)
        for match in matches:
            print(
                f"{match['title']} => {match['matched_text']} "
                f"confidence={match['confidence']} source={match['source']}"
            )
        for expected in case["expected"]:
            if not any(expected in matched for matched in matched_texts):
                failures.append(f"{text}: missing {expected}")

    if failures:
        print("\nFAILURES:")
        for failure in failures:
            print("-", failure)
        return 1

    print("\nAll grammar matcher smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
