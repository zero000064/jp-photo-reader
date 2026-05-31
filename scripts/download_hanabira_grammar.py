from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

FILES = [
    "grammar_ja_N1_full_alphabetical_0001.json",
    "grammar_ja_N2_full_alphabetical_0001.json",
    "grammar_ja_N3_full_alphabetical_0001.json",
    "grammar_ja_N4_full_alphabetical_0001.json",
    "grammar_ja_N5_full_alphabetical_0001.json",
]
BASE_URL = "https://raw.githubusercontent.com/tristcoil/hanabira.org-japanese-content/main/grammar_json"
MARKDOWN_API_URL = "https://api.github.com/repos/tristcoil/hanabira.org-japanese-content/contents/markdown_grammar_japanese"
MARKDOWN_RAW_BASE_URL = "https://raw.githubusercontent.com/tristcoil/hanabira.org-japanese-content/main/markdown_grammar_japanese"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parents[1] / "backend" / "data" / "hanabira_grammar"
DEFAULT_MARKDOWN_OUTPUT_DIR = Path(__file__).resolve().parents[1] / "backend" / "data" / "hanabira_grammar_markdown"


def download(output_dir: Path, markdown_output_dir: Path = DEFAULT_MARKDOWN_OUTPUT_DIR) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        url = f"{BASE_URL}/{name}"
        target = output_dir / name
        print(f"Downloading {url}")
        with urllib.request.urlopen(url, timeout=60) as response:
            target.write_bytes(response.read())
        print(f"Wrote {target}")

    download_markdown(markdown_output_dir)

    attribution = output_dir / "ATTRIBUTION.txt"
    attribution.write_text(
        "Japanese grammar content from hanabira.org-japanese-content.\n"
        "Repository: https://github.com/tristcoil/hanabira.org-japanese-content\n"
        "The repository README describes the content as Creative Commons and asks users to link to Hanabira.org.\n",
        encoding="utf-8",
    )


def download_markdown(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Listing markdown files from {MARKDOWN_API_URL}")
    with urllib.request.urlopen(MARKDOWN_API_URL, timeout=60) as response:
        items = json.loads(response.read().decode("utf-8"))
    for item in items:
        name = item.get("name")
        if not isinstance(name, str) or not name.endswith(".md"):
            continue
        url = f"{MARKDOWN_RAW_BASE_URL}/{urllib.parse.quote(name)}"
        target = output_dir / name
        print(f"Downloading {name}")
        with urllib.request.urlopen(url, timeout=60) as response:
            target.write_bytes(response.read())
    attribution = output_dir / "ATTRIBUTION.txt"
    attribution.write_text(
        "Japanese grammar markdown from hanabira.org-japanese-content.\n"
        "Repository: https://github.com/tristcoil/hanabira.org-japanese-content\n"
        "The repository README describes the content as Creative Commons and asks users to link to Hanabira.org.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT_DIR
    markdown_output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_MARKDOWN_OUTPUT_DIR
    download(output_dir, markdown_output_dir)
