#!/usr/bin/env bash
set -euo pipefail

BACKEND_HOST="${BACKEND_HOST:-127.0.0.1}"
BACKEND_PORT="${BACKEND_PORT:-8000}"
STOP_OLLAMA="${STOP_OLLAMA:-0}"
OLLAMA_BIN="${OLLAMA_BIN:-ollama}"

stop_backend() {
  local pattern="uvicorn app:app --host $BACKEND_HOST --port $BACKEND_PORT"
  local pids=""

  if command -v pgrep >/dev/null 2>&1; then
    pids="$(pgrep -f "$pattern" || true)"
  fi

  if [[ -z "$pids" ]] && command -v fuser >/dev/null 2>&1; then
    pids="$(fuser "$BACKEND_PORT/tcp" 2>/dev/null || true)"
  fi

  if [[ -z "$pids" ]]; then
    echo "No backend process found for $BACKEND_HOST:$BACKEND_PORT"
    return
  fi

  echo "Stopping backend process(es): $pids"
  kill $pids 2>/dev/null || true

  for _ in {1..20}; do
    local still_running=""
    for pid in $pids; do
      if kill -0 "$pid" 2>/dev/null; then
        still_running=1
        break
      fi
    done
    [[ -z "$still_running" ]] && return
    sleep 0.2
  done

  echo "Backend did not exit after SIGTERM; sending SIGKILL"
  kill -9 $pids 2>/dev/null || true
}

stop_ollama() {
  if [[ "$STOP_OLLAMA" != "1" && "${STOP_OLLAMA,,}" != "true" && "${STOP_OLLAMA,,}" != "yes" ]]; then
    echo "Leaving Ollama running. Set STOP_OLLAMA=1 to stop it too."
    return
  fi

  if command -v "$OLLAMA_BIN" >/dev/null 2>&1; then
    echo "Stopping Ollama"
    pkill -f "$OLLAMA_BIN serve" 2>/dev/null || true
  else
    echo "Ollama command not found; skipping Ollama shutdown"
  fi
}

stop_backend
stop_ollama
