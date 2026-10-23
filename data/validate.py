"""Validate the context data line's data. Run: python3 -I data/validate.py

Checks:
  1. message_id is globally unique across data/emails/*.jsonl
  2. every planted fact quote / planted address is a substring of the body; planted_honorific matches "您"
  3. every evidence in ground_truth/people.json points to an existing email and its quote is a substring
  4. every external id referenced exists in ground_truth/external.json and is marked mock
  5. no forbidden topic appears in synthetic_relationship.jsonl
  6. every expected highlight in demo_scenarios.json resolves to a ground-truth entry
Prints a summary table per person at the end. Exit code 1 on any failure.
"""
import json
import pathlib
import sys
from collections import Counter

DATA = pathlib.Path(__file__).resolve().parent
EMAILS = DATA / "emails"
GT = DATA / "ground_truth"

# style_spec.md forbidden topics: left uncovered so the demo can show `inferred` highlights.
FORBIDDEN_TOPICS = {
    "travel_with_baby": ["婴儿床", "婴儿推车", "安全座椅", "crib", "stroller", "car seat"],
    "declining_invitation": ["婉拒", "去不了", "不能参加", "没法参加", "decline", "can't make it to the party"],
    "congratulating_job_change": ["恭喜", "祝贺", "升职", "congrat", "promotion", "new job"],
    "job_search": ["求职", "面试", "招聘", "简历", "内推", "interview", "resume", "hiring", "job offer"],
    "medical_pregnancy": ["医院", "看病", "心理", "怀孕", "hospital", "pregnan", "therapy"],
    "finance_tax": ["税务", "报税", "征信", "贷款", "tax return", "credit score"],
}
LAYERS = {"person", "scenario", "external", "inferred"}
STRENGTHS = {"strong", "weak"}

errors = []


def fail(msg):
    errors.append(msg)


def check(name, fn):
    before = len(errors)
    fn()
    n = len(errors) - before
    print(f"[{'PASS' if n == 0 else 'FAIL'}] {name}" + (f" ({n} errors)" if n else ""))


# ---------- load ----------
emails = {}
by_file = {}
dup_ids = []
for path in sorted(EMAILS.glob("*.jsonl")):
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    by_file[path.name] = rows
    for r in rows:
        if r["message_id"] in emails:
            dup_ids.append((path.name, r["message_id"]))
        emails[r["message_id"]] = r
people = json.loads((GT / "people.json").read_text(encoding="utf-8"))["people"]
external = json.loads((GT / "external.json").read_text(encoding="utf-8"))
ext_by_id = {x["id"]: x for x in external["items"]}
rel = by_file.get("synthetic_relationship.jsonl", [])


def check_evidence(where, evs):
    for e in evs:
        mid, quote = e.get("message_id"), e.get("quote")
        if mid not in emails:
            fail(f"{where}: message_id {mid} not found")
        elif not quote or quote not in emails[mid]["body"]:
            fail(f"{where}: quote not in body of {mid}: {quote!r}")


# ---------- checks ----------
def c_unique():
    for f, mid in dup_ids:
        fail(f"duplicate message_id {mid} in {f}")


def c_planted():
    if not rel:
        fail("data/emails/synthetic_relationship.jsonl missing or empty")
    for r in rel:
        mid, body = r["message_id"], r["body"]
        for k in ("planted_address", "planted_honorific", "planted_facts"):
            if k not in r:
                fail(f"{mid}: missing {k}")
        if r.get("planted_address") and r["planted_address"] not in body:
            fail(f"{mid}: planted_address {r['planted_address']!r} not in body")
        if r.get("planted_honorific") is True and "您" not in body:
            fail(f"{mid}: planted_honorific=True but no 您 in body")
        if r.get("planted_honorific") is False and "您" in body:
            fail(f"{mid}: planted_honorific=False but 您 in body")
        for pf in r.get("planted_facts", []):
            if pf["quote"] not in body:
                fail(f"{mid}: planted fact {pf['fact_id']} quote not in body: {pf['quote']!r}")


def c_people():
    fact_ids = Counter()
    for p in people:
        pid = p["id"]
        check_evidence(f"{pid}.core_connection", p["core_connection"]["evidence"])
        if not p["core_connection"]["evidence"]:
            fail(f"{pid}.core_connection has no evidence")
        for a in p["address_as"]:
            check_evidence(f"{pid}.address_as[{a['context']}]", a["evidence"])
            for e in a["evidence"]:
                if e.get("message_id") in emails and a["value"] not in e["quote"]:
                    fail(f"{pid}.address_as[{a['context']}]: quote does not contain {a['value']!r}")
        check_evidence(f"{pid}.honorific", p["honorific"]["evidence"])
        if p["honorific"]["uses_nin"] and not p["honorific"]["evidence"]:
            fail(f"{pid}.honorific uses 您 but has no evidence")
        if "sign_off" in p:
            check_evidence(f"{pid}.sign_off", p["sign_off"]["evidence"])
        for f in p["facts"]:
            fact_ids[f["id"]] += 1
            if not f["evidence"]:
                fail(f"{pid}.{f['id']} has no evidence")
            check_evidence(f"{pid}.{f['id']}", f["evidence"])
        for e in p["edges"]:
            check_evidence(f"{pid}.edge->{e['to']}", e["evidence"])
    for fid, n in fact_ids.items():
        if n > 1:
            fail(f"fact id {fid} used {n} times")
    known = set(fact_ids)
    for r in rel:
        for pf in r.get("planted_facts", []):
            if pf["fact_id"] not in known:
                fail(f"{r['message_id']}: planted fact {pf['fact_id']} not in people.json")


def c_external():
    if external.get("_mock") is not True:
        fail("external.json is not marked _mock: true")
    for x in external["items"]:
        for k in ("id", "text", "source_label", "date"):
            if not x.get(k):
                fail(f"external {x.get('id')}: missing {k}")
        if x.get("mock") is not True:
            fail(f"external {x['id']}: not marked mock")
        if "mock" not in x["source_label"]:
            fail(f"external {x['id']}: source_label does not say mock")
    pids = {p["id"] for p in people}
    for p in people:
        for xid in p.get("external", []):
            if xid not in ext_by_id:
                fail(f"{p['id']}: external {xid} not found")
            elif ext_by_id[xid]["person_id"] != p["id"]:
                fail(f"{p['id']}: external {xid} belongs to {ext_by_id[xid]['person_id']}")
    for x in external["items"]:
        if x["person_id"] not in pids:
            fail(f"external {x['id']}: unknown person_id {x['person_id']}")


def c_forbidden():
    for r in rel:
        text = (r["body"] + "\n" + (r.get("prev") or "")).lower()
        for topic, words in FORBIDDEN_TOPICS.items():
            for w in words:
                if w.lower() in text:
                    fail(f"{r['message_id']}: forbidden topic {topic} ({w!r})")


def c_demo():
    path = DATA / "demo_scenarios.json"
    if not path.exists():
        fail("data/demo_scenarios.json missing")
        return
    demo = json.loads(path.read_text(encoding="utf-8"))
    by_email = {p["email"]: p for p in people}
    for s in demo["scenarios"]:
        p = by_email.get(s["to"])
        if p is None:
            fail(f"{s['id']}: recipient {s['to']} not in people.json")
            continue
        facts = {f["id"] for f in p["facts"]}
        contexts = {a["context"] for a in p["address_as"]}
        for h in s["expected_highlights"]:
            layer, ref, strength = h.get("layer"), h.get("ref"), h.get("strength")
            where = f"{s['id']}: {h.get('text_hint')!r}"
            if layer not in LAYERS:
                fail(f"{where}: bad layer {layer}")
            if strength not in STRENGTHS:
                fail(f"{where}: bad strength {strength}")
            if layer == "inferred":
                if ref is not None:
                    fail(f"{where}: inferred highlight must have ref null")
                continue
            kind, rid = ref["kind"], ref["id"]
            ok = {
                "fact": lambda: rid in facts,
                "external": lambda: rid in ext_by_id and rid in p.get("external", []),
                "address_as": lambda: rid in contexts,
                "honorific": lambda: rid == p["id"] and bool(p["honorific"]["uses_nin"]),
                "sign_off": lambda: rid == p["id"] and "sign_off" in p,
                "core_connection": lambda: rid == p["id"],
                "habit": lambda: layer == "scenario",
            }.get(kind, lambda: False)()
            if not ok:
                fail(f"{where}: ref {kind}:{rid} does not resolve")
            if layer == "external" and kind != "external":
                fail(f"{where}: external layer must ref an external item")


check("message_id globally unique", c_unique)
check("planted fields match bodies", c_planted)
check("ground-truth evidence quotes are verbatim", c_people)
check("external context exists and is mock", c_external)
check("no forbidden topic in synthetic_relationship", c_forbidden)
check("demo scenario highlights resolve", c_demo)

# ---------- summary ----------
counts = Counter(r["to"] for r in emails.values())
print()
print(f"emails: {len(emails)} ({', '.join(f'{k}={len(v)}' for k, v in by_file.items())}); people: {len(people)}; external: {len(ext_by_id)}")
print("| person | address_as | uses 您 | facts | emails | external |")
print("|---|---|---|---|---|---|")
for p in people:
    address = " / ".join(f"{a['context']}: {a['value']}" for a in p["address_as"])
    nin = {True: "yes", False: "no", "formal_only": "formal only"}[p["honorific"]["uses_nin"]]
    print(f"| {p['display_name']} | {address} | {nin} | {len(p['facts'])} | {counts[p['email']]} | {len(p.get('external', []))} |")

print()
if errors:
    for e in errors:
        print("ERROR", e)
    print(f"FAILED: {len(errors)} errors")
    sys.exit(1)
print("ALL CHECKS PASSED")
