# Offline extraction pipeline

Turns `data/emails/*.jsonl` (emails Mia wrote) into the two profile layers the app reads:

- **Contact notes** — `out/contacts/<email>.md`: Markdown with frontmatter matching `ContactNote` (contract 0.2):
  `address_as`, `honorific`, `sign_off`, `language` (each `{value, count, total, status, evidence}`), `facts`,
  `edges`, `external`. Two additive keys: `address_as_by_context` (greeting per context: private / default /
  formal) and `core_connection` (`{text, evidence}`).
- **Scenario styles** — `out/styles/<scenario>.json`: `{scenario, habits: [{id, description, count, total,
  status, evidence}]}`.

The results are committed, so the app never calls the model for extraction. Only online drafting does.

## Steps

| Script | What it does | Calls the model? |
|---|---|---|
| `extract.py` | Groups emails by recipient (contacts with >= 3 emails) and by scenario (`category`); one `claude -p` call per group, in parallel; caches raw replies in `out/raw/`; then runs `verify.py`. | yes |
| `verify.py` | Keeps an evidence quote only if it is a verbatim substring of the `body` of the email it cites (and that email went to this contact). Drops a field, fact, edge or habit with no evidence left. Computes `count` (distinct verified emails) and `total` (emails shown). Attaches `data/external.json` by email. Writes `out/contacts/`, `out/styles/`, `out/verify_report.md`. | no |
| `evaluate.py` | Compares notes with `data/ground_truth/people.json`: address accuracy, honorific accuracy, fact recall. Writes `out/eval.md`. | no |

The pipeline never reads `data/ground_truth/` or any `planted_*` field (`common.load_emails` drops them on
load); only `evaluate.py` reads ground truth.

## Rerun

```bash
python3 -I pipeline/extract.py            # extract groups not cached in out/raw/, then verify
python3 -I pipeline/extract.py --force    # re-extract everything (about 40 claude -p calls)
python3 -I pipeline/extract.py --only wang.jianhua@example.com --force
python3 -I pipeline/verify.py             # re-verify cached raw replies, no model calls
python3 -I pipeline/evaluate.py
```

`claude -p` runs with `ANTHROPIC_API_KEY` removed from its environment, so it uses the local Claude
subscription rather than API billing. Requires Python 3.10+ and PyYAML.
