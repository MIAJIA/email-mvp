"""Offline extraction: one `claude -p` call per contact (with enough emails) and per scenario.

Raw model replies are cached in pipeline/out/raw/ so verify.py can be rerun without model calls.

Usage:
  python3 pipeline/extract.py                 # extract what is not cached yet, then verify
  python3 pipeline/extract.py --force         # re-extract everything
  python3 pipeline/extract.py --only a@b.com  # one contact (repeatable)
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (RAW, call_claude, group_by_recipient, group_by_scenario, load_emails,  # noqa: E402
                    parse_json_block, safe_name)
from prompts import CONTACT_PROMPT, SCENARIO_PROMPT, format_email  # noqa: E402
import verify  # noqa: E402

MIN_EMAILS = 3          # contacts with fewer emails fall back to the scenario style
MAX_CONTACT_EMAILS = 40  # most recent ones; `total` is the number shown to the model
MAX_SCENARIO_EMAILS = 30


def evenly(items: list, k: int) -> list:
    if len(items) <= k:
        return items
    step = len(items) / k
    return [items[int(i * step)] for i in range(k)]


def contact_job(email: str, msgs: list[dict]) -> dict:
    msgs = msgs[-MAX_CONTACT_EMAILS:]
    prompt = CONTACT_PROMPT.format(email=email, n=len(msgs), emails="\n\n".join(format_email(m) for m in msgs))
    return {"kind": "contacts", "name": email, "prompt": prompt,
            "meta": {"email": email, "to_name": msgs[-1].get("to_name"),
                     "message_ids": [m["message_id"] for m in msgs]}}


def scenario_job(scenario: str, msgs: list[dict]) -> dict:
    msgs = evenly(msgs, MAX_SCENARIO_EMAILS)
    prompt = SCENARIO_PROMPT.format(scenario=scenario, n=len(msgs),
                                    emails="\n\n".join(format_email(m, with_prev=False, max_body=1000) for m in msgs))
    return {"kind": "styles", "name": scenario, "prompt": prompt,
            "meta": {"scenario": scenario, "message_ids": [m["message_id"] for m in msgs]}}


def run_job(job: dict) -> tuple[str, str]:
    path = RAW / job["kind"] / f"{safe_name(job['name'])}.json"
    t0 = time.time()
    reply = call_claude(job["prompt"])
    try:
        extraction = parse_json_block(reply)
    except Exception:  # keep the reply so a bad parse can be inspected, verify treats it as empty
        extraction, job["meta"]["unparsed_reply"] = {}, reply
    path.write_text(json.dumps({**job["meta"], "extraction": extraction}, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")
    return job["name"], f"{time.time() - t0:.0f}s"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", action="append", default=[])
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--no-styles", action="store_true")
    args = ap.parse_args()

    emails = load_emails()
    (RAW / "contacts").mkdir(parents=True, exist_ok=True)
    (RAW / "styles").mkdir(parents=True, exist_ok=True)

    jobs = []
    for email, msgs in group_by_recipient(emails).items():
        if len(msgs) >= MIN_EMAILS and (not args.only or email in args.only):
            jobs.append(contact_job(email, msgs))
    if not args.no_styles and not args.only:
        for scenario, msgs in group_by_scenario(emails).items():
            jobs.append(scenario_job(scenario, msgs))
    if not args.force:
        jobs = [j for j in jobs if not (RAW / j["kind"] / f"{safe_name(j['name'])}.json").exists()]

    print(f"{len(emails)} emails; {len(jobs)} claude -p calls to make", flush=True)
    failed = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(run_job, j): j["name"] for j in jobs}
        for fut in as_completed(futures):
            try:
                name, took = fut.result()
                print(f"  ok   {name} ({took})", flush=True)
            except Exception as exc:  # one failed contact must not sink the batch
                failed.append(futures[fut])
                print(f"  FAIL {futures[fut]}: {exc}", flush=True)
    print(f"claude -p calls: {len(jobs)}, failed: {len(failed)} {failed}", flush=True)
    verify.build_all()


if __name__ == "__main__":
    main()
