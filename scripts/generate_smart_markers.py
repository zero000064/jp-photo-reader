import json
import httpx
import asyncio
from pathlib import Path
import os
import sys
import re

# Add the project root to sys.path so we can import backend
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.grammar_matcher import DEFAULT_GRAMMAR_DIR

PROMPT_TEMPLATE = """
/think
You are an expert Japanese linguist and programmer. Your task is to convert a human-readable Japanese grammar rule into a rigid JSON structure for a deterministic token matching engine.

You will be given the "Title" and "Formation" of a grammar point.
Output the result in a markdown JSON code block. Do not output anything outside the code block.
The JSON must contain exactly two keys: "markers" and "formation_patterns".

1. "markers": A list of Boolean Abstract Syntax Trees (AST) that uniquely identify this grammar point.
   - Use native JSON objects to represent AND/OR logic.
   - For a single string: just output the string. e.g. "ほしいです"
   - For AND logic (both must be present): {{"AND": ["string1", "string2"]}}
   - For OR logic: {{"OR": ["string1", "string2"]}}
   - Do NOT include generic parts-of-speech (like Noun, Verb) in the markers. Only include exact Japanese text.
   - CRITICAL RULE 1: DO NOT invent synonyms or equivalent phrases! ONLY use exact Japanese words literally present in the "Title" or "Formation".
   - CRITICAL RULE 2: Keep the array extremely small! The "markers" array should almost always contain EXACTLY 1 boolean rule (e.g. `[{{"AND": ["すこしも", "ない"]}}]`). NEVER generate large lists of permutations.
   - Example 1 (Simple): "ほしいです"
   - Example 2 (Both required): {{"AND": ["て", "さしあげる"]}}
   - Example 3 (Complex): {{"AND": ["ない", {{"OR": ["ことには", "といけない"]}}]}}

2. "formation_patterns": A list of lists of token dictionaries. Each token dictionary must be either:
   - A literal string: {{"kind": "literal", "text": "exact japanese string"}}
   - A part-of-speech slot: {{"kind": "slot", "pos": "verb" | "noun" | "adjective" | "any"}}

Example Input:
Title: Noun と相まって
Formation: Noun + と相まって

Example Output:
{{
  "markers": [
    {{"AND": ["と", "相まって"]}}
  ],
  "formation_patterns": [
    [
      {{"kind": "slot", "pos": "noun"}},
      {{"kind": "literal", "text": "と"}},
      {{"kind": "literal", "text": "相まって"}}
    ]
  ]
}}

Now process this input:
Title: {title}
Formation: {formation}
"""

async def process_entry(client: httpx.AsyncClient, title: str, formation: str) -> dict:
    if not title or not formation:
        return {}
    prompt = PROMPT_TEMPLATE.format(title=title, formation=formation)
    try:
        response = await client.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "hf.co/DevQuasar/shisa-ai.shisa-v2-qwen2.5-32b-GGUF:Q3_K_M",
                "prompt": prompt,
                "stream": False
            }
        )
        res_json = response.json()
        raw_text = str(res_json.get("response") or res_json.get("thinking") or "")
        
        # Strip <think> blocks
        cleaned = re.sub(r"<think>.*?</think>", "", raw_text, flags=re.IGNORECASE | re.DOTALL).strip()
        # Extract markdown JSON block
        json_match = re.search(r"```json\s*(.*?)\s*```", cleaned, re.IGNORECASE | re.DOTALL)
        if json_match:
            cleaned = json_match.group(1).strip()
        else:
            # Fallback if no block is used
            json_match = re.search(r"\{.*\}", cleaned, re.DOTALL)
            if json_match:
                cleaned = json_match.group(0).strip()
                
        return json.loads(cleaned)
    except Exception as e:
        print(f"Error processing '{title}': {e}")
        return {}

async def main():
    grammar_dir = Path(DEFAULT_GRAMMAR_DIR)
    json_files = []
    for level in ["N1", "N2", "N3", "N4"]:
        json_files.extend(sorted(grammar_dir.glob(f"grammar_ja_{level}_*.json")))
    
    total_processed = 0
    total_skipped = 0
    total_errors = 0
    
    timeout = httpx.Timeout(180.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        for json_file in json_files:
            print(f"Processing {json_file.name}...")
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    entries = json.load(f)
            except Exception as e:
                print(f"Failed to load {json_file.name}: {e}")
                continue
                
            modified = False
            for i, entry in enumerate(entries):
                title = entry.get("title", "")
                formation = entry.get("formation", "")
                
                # Skip if already processed or if no formation exists to parse
                # if entry.get("llm_markers") and entry.get("llm_formation_patterns"):
                #     total_skipped += 1
                #     continue
                if not title or not formation:
                    total_skipped += 1
                    continue
                    
                print(f"  [{i+1}/{len(entries)}] Querying Ollama for: {title}")
                llm_data = await process_entry(client, title, formation)
                
                if llm_data and "markers" in llm_data and "formation_patterns" in llm_data:
                    entry["llm_markers"] = llm_data["markers"]
                    entry["llm_formation_patterns"] = llm_data["formation_patterns"]
                    modified = True
                    total_processed += 1
                else:
                    total_errors += 1
                    
                # Save after every successful API call to prevent data loss on crash
                if modified:
                    with open(json_file, "w", encoding="utf-8") as f:
                        json.dump(entries, f, ensure_ascii=False, indent=2)
                        
    print(f"\nFinished processing all files.")
    print(f"Successfully processed: {total_processed}")
    print(f"Skipped (already processed/no formation): {total_skipped}")
    print(f"Errors: {total_errors}")

if __name__ == "__main__":
    asyncio.run(main())
