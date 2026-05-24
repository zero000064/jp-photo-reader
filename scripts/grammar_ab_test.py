#!/usr/bin/env python3
import json
import time
import urllib.error
import urllib.request
from pathlib import Path


OLLAMA_URL = "http://127.0.0.1:11434/api/chat"

MODELS = [
    "qwen3:32b",
    "hf.co/mmnga/tokyotech-llm-Llama-3.1-Swallow-8B-Instruct-v0.3-gguf:Q4_K_M",
    "hf.co/XpressAI/shisa-v2.1-unphi4-14b-GGUF:Q4_K_M",
    "hf.co/alfredplpl/llm-jp-3-13b-instruct-gguf:Q4_K_M",
]

SYSTEM = (
    "You are a precise Japanese grammar analyst. Answer in English. "
    "Be concise but explicit. Identify grammar points, particles, conjugations, "
    "literal meaning, natural meaning, and learner pitfalls. Do not invent context. Do not include hidden reasoning, chain-of-thought, or thinking traces."
)

PROMPTS = [
    {
        "id": "wa_ga_contrast",
        "text": (
            "Analyze the grammar of this sentence: "
            "私は寿司は好きですが、刺身はあまり食べません。 "
            "Focus especially on the repeated は and why 私は and 寿司は are both used."
        ),
    },
    {
        "id": "te_oku_ba_conditional",
        "text": (
            "Analyze the grammar of this sentence: "
            "出かける前に、電気を消しておけばよかった。 "
            "Explain ておく, ばよかった, and the nuance of regret."
        ),
    },
    {
        "id": "causative_passive",
        "text": (
            "Analyze the grammar of this sentence: "
            "子どものころ、母に野菜を食べさせられた。 "
            "Explain the causative-passive form and the roles of 母に and 野菜を."
        ),
    },
    {
        "id": "rashii_souda_youna",
        "text": (
            "Compare these four sentences grammatically and semantically: "
            "雨が降るらしい。雨が降りそうだ。雨が降るそうだ。雨が降るようだ。"
        ),
    },
]


def chat(model: str, prompt: str) -> dict:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt + "\n\nLimit the answer to 450 words."},
        ],
        "stream": False,
        "think": False,
        "options": {
            "temperature": 0,
            "top_p": 0.9,
            "num_ctx": 4096,
            "num_predict": 450,
        },
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        OLLAMA_URL, data=data, headers={"Content-Type": "application/json"}
    )
    start = time.time()
    try:
        with urllib.request.urlopen(request, timeout=900) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return {
            "ok": False,
            "error": exc.read().decode("utf-8", errors="replace"),
            "elapsed_sec": round(time.time() - start, 3),
        }
    except Exception as exc:
        return {"ok": False, "error": repr(exc), "elapsed_sec": round(time.time() - start, 3)}

    return {
        "ok": True,
        "elapsed_sec": round(time.time() - start, 3),
        "eval_count": body.get("eval_count"),
        "eval_duration": body.get("eval_duration"),
        "content": body["message"]["content"],
    }


def main() -> None:
    output_dir = Path("tmp")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "grammar_ab_test_results.json"

    results = []
    for model in MODELS:
        for prompt in PROMPTS:
            print(f"RUN {model} :: {prompt['id']}", flush=True)
            result = chat(model, prompt["text"])
            results.append({"model": model, "prompt": prompt, "result": result})
            output_path.write_text(
                json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            print(
                f"DONE ok={result['ok']} elapsed={result['elapsed_sec']}s",
                flush=True,
            )

    print(output_path)


if __name__ == "__main__":
    main()
