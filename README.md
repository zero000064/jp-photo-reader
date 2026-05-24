# Japanese Photo Reader

Local-first Chrome extension for reading Japanese text in webpage images. It captures an image area, runs local OCR, tokenizes the recognized Japanese, looks up dictionary entries, and explains grammar with a local Ollama model.

## Features

- Select an area of a webpage image and recognize Japanese text with Manga-OCR.
- Analyze typed Japanese text from the extension popup.
- View token structure with per-token dictionary entries.
- Highlight recognized text in the result panel for dictionary lookup and Google search.
- Ask follow-up grammar questions without rerunning OCR or full grammar analysis.
- Keep all OCR, dictionary lookup, and grammar analysis local.

## Project Layout

- `backend/`: FastAPI service for OCR, tokenization, JMdict lookup, and Ollama grammar analysis.
- `extension/`: Manifest V3 Chrome extension UI and content scripts.
- `scripts/start-local.sh`: Starts Ollama when needed, ensures the default model exists, installs backend dependencies, checks CUDA by default, and runs the backend.

## Requirements

- Linux with Python 3.12 recommended.
- Chrome or Chromium-based browser.
- Ollama installed and reachable at `http://127.0.0.1:11434`.
- CUDA-capable GPU for Manga-OCR by default.
- The default grammar model:

```bash
ollama pull hf.co/XpressAI/shisa-v2.1-unphi4-14b-GGUF:Q4_K_M
```

You can override the grammar model with `OLLAMA_TEXT_MODEL`.

## Quick Start

```bash
./scripts/start-local.sh
```

Keep that terminal open while using the extension. The backend runs at `http://127.0.0.1:8000`.

If you need to override settings:

```bash
OLLAMA_TEXT_MODEL=hf.co/XpressAI/shisa-v2.1-unphi4-14b-GGUF:Q4_K_M \
BACKEND_PORT=8000 \
./scripts/start-local.sh
```

## Load The Extension

1. Open `chrome://extensions`.
2. Enable Developer mode.
3. Click Load unpacked.
4. Select the `extension/` directory from this project.

Reload the extension after changing files in `extension/`. Refresh already-open webpages so the updated content script is loaded.

## Basic Use

1. Start the local backend with `./scripts/start-local.sh`.
2. Click the extension toolbar button.
3. Click Select area.
4. Drag over Japanese text in a webpage image.
5. The side panel shows recognized text, token structure, dictionary entries for each token, and grammar analysis.

## Typed Text Analysis

Use the Analyze typed text box in the popup to analyze Japanese text directly. Clicking Analyze text runs full tokenization, dictionary lookup, and automatic grammar analysis.

The grammar question box is not sent during Analyze text. This keeps normal analysis cheaper and avoids extra LLM calls.

## Grammar Questions

After analyzing an image or typed text, type a question in the Grammar question box and press Enter. This sends only the current recognized text plus the question to the backend. The existing recognized text, token structure, dictionary results, and automatic grammar analysis stay unchanged; only the Grammar Question Answer section updates.

## Dictionary Lookup

The Structure section includes dictionary matches for each token when available. Particles, auxiliaries, punctuation, and unknown terms may show no dictionary entry.

You can also highlight recognized text in the side panel to run a dictionary lookup for the selection. The result includes a Google search link.

## Optional Full JMdict Setup

The app runs without a local JMdict database, but definitions will be limited. To build the local SQLite dictionary:

```bash
mkdir -p backend/data
curl -L http://ftp.edrdg.org/pub/Nihongo/JMdict_e.gz -o backend/data/JMdict_e.gz
gzip -dc backend/data/JMdict_e.gz > backend/data/JMdict_e.xml
python backend/import_jmdict.py backend/data/JMdict_e.xml backend/data/jmdict.sqlite
```

Restart the backend after importing. Files in `backend/data/` are local data and should not be committed.

## Manual Backend Startup

```bash
python -m pip install -r backend/requirements.txt
python -m pip install -r backend/requirements-manga-ocr.txt
cd backend
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Useful environment variables:

```bash
export OLLAMA_URL=http://127.0.0.1:11434
export OLLAMA_TEXT_MODEL=hf.co/XpressAI/shisa-v2.1-unphi4-14b-GGUF:Q4_K_M
export MANGA_OCR_REQUIRE_CUDA=1
```

Set `MANGA_OCR_REQUIRE_CUDA=0` only if you intentionally want CPU fallback.

## API Checks

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Analyze text:

```bash
curl http://127.0.0.1:8000/analyze-text \
  -H "Content-Type: application/json" \
  -d "{"text":"母に野菜を食べさせられた。","explain_grammar":true}"
```

Answer a follow-up grammar question without rerunning full analysis:

```bash
curl http://127.0.0.1:8000/answer-grammar-question \
  -H "Content-Type: application/json" \
  -d "{"text":"母に野菜を食べさせられた。","grammar_question":"What does 母に mark?"}"
```

Direct Ollama test:

```bash
curl http://127.0.0.1:11434/api/generate \
  -H "Content-Type: application/json" \
  -d "{"model":"hf.co/XpressAI/shisa-v2.1-unphi4-14b-GGUF:Q4_K_M","prompt":"Say hello in one sentence.","stream":false}"
```

## Security Notes

- Keep the backend and Ollama bound to `127.0.0.1`.
- Do not expose this backend directly to a network.
- Do not commit local dictionary databases, benchmark outputs, model files, cache directories, or machine-specific notes.
