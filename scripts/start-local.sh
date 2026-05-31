#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BACKEND_DIR="$ROOT_DIR/backend"

OLLAMA_URL="${OLLAMA_URL:-http://127.0.0.1:11434}"
OLLAMA_TEXT_MODEL="${OLLAMA_TEXT_MODEL:-hf.co/DevQuasar/shisa-ai.shisa-v2-qwen2.5-32b-GGUF:Q3_K_M}"
MANGA_OCR_REQUIRE_CUDA="${MANGA_OCR_REQUIRE_CUDA:-1}"
OLLAMA_BIN="${OLLAMA_BIN:-ollama}"
OLLAMA_LOG="${OLLAMA_LOG:-/tmp/jp-photo-reader-ollama.log}"

if [[ -z "${PYTHON:-}" && -x "$HOME/anaconda3/envs/jp-photo-reader312/bin/python" ]]; then
  PYTHON="$HOME/anaconda3/envs/jp-photo-reader312/bin/python"
else
  PYTHON="${PYTHON:-python}"
fi
BACKEND_HOST="${BACKEND_HOST:-127.0.0.1}"
BACKEND_PORT="${BACKEND_PORT:-8000}"

OLLAMA_PID=""

cleanup() {
  if [[ -n "$OLLAMA_PID" ]] && kill -0 "$OLLAMA_PID" 2>/dev/null; then
    kill "$OLLAMA_PID"
  fi
}
trap cleanup EXIT

need_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing required command: $1" >&2
    exit 1
  fi
}

wait_for_ollama() {
  for _ in {1..60}; do
    if curl -fsS "$OLLAMA_URL/api/tags" >/dev/null 2>&1; then
      return 0
    fi
    sleep 1
  done

  echo "Ollama did not become reachable at $OLLAMA_URL" >&2
  echo "Ollama log: $OLLAMA_LOG" >&2
  exit 1
}

ensure_ollama() {
  need_command curl

  if curl -fsS "$OLLAMA_URL/api/tags" >/dev/null 2>&1; then
    echo "Ollama is already running at $OLLAMA_URL"
    return
  fi

  need_command "$OLLAMA_BIN"
  echo "Starting Ollama at $OLLAMA_URL"
  "$OLLAMA_BIN" serve >"$OLLAMA_LOG" 2>&1 &
  OLLAMA_PID="$!"
  wait_for_ollama
}

ensure_model() {
  local model="$1"

  if "$OLLAMA_BIN" list | awk '{print $1}' | grep -Fx "$model" >/dev/null 2>&1; then
    echo "Model available: $model"
    return
  fi

  echo "Pulling model: $model"
  "$OLLAMA_BIN" pull "$model"
}

ensure_ollama
ensure_model "$OLLAMA_TEXT_MODEL"

cd "$ROOT_DIR"
"$PYTHON" -m pip install -r backend/requirements-manga-ocr.txt

if [[ "${MANGA_OCR_REQUIRE_CUDA,,}" != "0" && "${MANGA_OCR_REQUIRE_CUDA,,}" != "false" && "${MANGA_OCR_REQUIRE_CUDA,,}" != "no" ]]; then
  "$PYTHON" -c 'import sys, torch; ok = torch.cuda.is_available(); print(f"torch CUDA available: {ok}"); sys.exit(0 if ok else 1)'
fi

cd "$BACKEND_DIR"
echo "Starting backend at http://$BACKEND_HOST:$BACKEND_PORT"
OLLAMA_URL="$OLLAMA_URL" \
OLLAMA_TEXT_MODEL="$OLLAMA_TEXT_MODEL" \
MANGA_OCR_REQUIRE_CUDA="$MANGA_OCR_REQUIRE_CUDA" \
"$PYTHON" -m uvicorn app:app --host "$BACKEND_HOST" --port "$BACKEND_PORT"
