# Grammar Matching Test Cases

## Case: compound permissive/try/maybe sentence

### Sentence

```text
基本のコーディネイトを違う商品で組んでみてもいいかもね。
```

### Expected grammar points

These were returned by ChatGPT and should be considered the target behavior for the extension grammar matching UI.

| Grammar point | Meaning | Expected matched span | Notes |
| --- | --- | --- | --- |
| `Vてみる` | try doing something | `組んでみ` / `組んでみる` | Appears inside `組んでみても`. The matcher should recognize the `てみる` auxiliary pattern even when followed by `てもいい`. |
| `Vてもいい` | it is okay to do V | `組んでみてもいい` | The sentence means it may be okay to try assembling/coordinating it with different products. |
| `かも` | maybe / might | `かも` | Sentence-final hedge before `ね`. |
| `で` | using / by means of | `違う商品で` | Instrumental/means particle: using different products/items. |

### Current observed backend result

This case now passes with the hybrid token-rule/recovery matcher. Expected smoke-test output includes:

```text
～てもいい (〜temo ii) => 組んでみてもいい
～てみる (〜te miru) => 組んでみ
もしかすると〜かもしれない (moshikasuru to 〜kamoshirenai) => かも
で => 違う商品で
```

The older literal-marker matcher only returned `～ても`; keep this case as a regression test for nested and overlapping grammar.

### Backend smoke test

Run the dedicated matcher smoke test from the repo root:

```bash
python3 scripts/test_grammar_matcher.py
```

For only this sentence, run:

```bash
python3 - <<'PY'
from backend.app import tokenize
from backend.grammar_matcher import match_grammar_points

text = "基本のコーディネイトを違う商品で組んでみてもいいかもね。"
matches = match_grammar_points(text, tokenize(text), tokenize, limit=10)
for match in matches:
    print(match["title"], "=>", match["matched_text"], "confidence=", match["confidence"], "source=", match["source"])
PY
```

Passing behavior includes matches equivalent to:

```text
Vてみる => 組んでみ
Vてもいい => 組んでみてもいい
かも => かも
で => 違う商品で
```

Exact titles may differ depending on the Hanabira grammar source title, but the extension should show these four concepts clearly.

### API integration test

Start the backend, then run:

```bash
curl -s http://127.0.0.1:8000/analyze-text \
  -H 'Content-Type: application/json' \
  -d '{"text":"基本のコーディネイトを違う商品で組んでみてもいいかもね。","explain_grammar":false,"explain_sentence_tree":true,"grammar_question":""}'
```

Check the JSON response:

- `sentence_analysis.source` should be `ollama` when the local model completes successfully.
- `grammar_analysis` should be an empty string because automatic grammar prose is disabled.
- `grammar_matches` should include the four expected grammar concepts above once this case is fixed.

### Extension manual test

1. Start the backend with `./scripts/start-local.sh`.
2. Reload the Chrome extension from `chrome://extensions`.
3. Use typed text analysis with:

   ```text
   基本のコーディネイトを違う商品で組んでみてもいいかもね。
   ```

4. Confirm the side panel shows an AI sentence graph in `Sentence Analysis`.
5. Confirm `Matched Grammar` lists:

   - `Vてみる`
   - `Vてもいい`
   - `かも`
   - instrumental/means `で`

6. Click any grammar reference buttons that appear and confirm markdown loads when the match has a local markdown file.

### Implementation notes

This case is difficult for simple marker matching because `組んでみてもいい` stacks multiple constructions:

```text
組む -> 組んで + みる -> 組んでみて + も + いい
```

A robust matcher should support overlapping/nested grammar detections instead of stopping at the shortest marker (`ても`). It should also allow high-frequency particle grammar such as `で` only when the role is useful enough for learners, otherwise the UI may become noisy.
