"""Model calls go through the local `claude` CLI on the user's subscription (DECISIONS 14:12), never the API key."""
from __future__ import annotations

import json
import os
import subprocess


class LLMError(RuntimeError):
    pass


def complete(prompt: str, timeout: int = 180) -> str:
    env = {k: v for k, v in os.environ.items() if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_BASE_URL")}
    proc = subprocess.run(
        ["claude", "-p", "--output-format", "json", "--tools", ""],
        input=prompt, capture_output=True, text=True, timeout=timeout, env=env,
    )
    if proc.returncode != 0:
        raise LLMError(f"claude exited {proc.returncode}: {proc.stderr[-500:]}")
    out = json.loads(proc.stdout)
    if out.get("is_error"):
        raise LLMError(str(out.get("result"))[:500])
    return out["result"]
