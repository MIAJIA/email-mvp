# AGENTS.md

Instructions for a coding agent (Claude Code, Codex, Cursor, ...) that has been asked to understand this
repository and run the demo. Read this file top to bottom before running anything. Every command below is run
from the **repository root**; commands that need another directory use a `( cd ... && ... )` subshell, so your
working directory never changes.

## What this is

email-mvp is a take-home MVP for **explainable personalized email drafting**. An offline pipeline reads the
emails the user sent and writes two profile layers to files: how they write each kind of email (scenario
styles) and how they write to each person (contact notes: greeting, honorifics, sign-off, language, facts).
Every entry carries quotes from the user's own emails, and code has checked that each quote is a verbatim
substring of the email it cites. Online, a FastAPI backend drafts an email for one recipient by calling the
local `claude` command line. The model only writes the email and tags each phrase with the key of the note it
used; the rationale, counts, quotes and strength on each highlight are filled in by code from the files. A
Vite + React front end shows the draft with three levels of disclosure: an underline in the text, a hover card
with the reason, and the original email when you open a quote.

Most data is synthetic. For how the context is built and what the model sees, read the section
[How the context is built](README.md#how-the-context-is-built) in README.md; it is not repeated here.

## Repository map

| Path | What it is |
| --- | --- |
| `backend/` | FastAPI app. `app/main.py` (routes), `app/generator.py` (prompt, tag parsing, highlights), `app/stores.py` (file-backed stores and the data path environment variables), `app/llm.py` (calls `claude -p`), `app/schema.py` (the API contract), `tests/`. |
| `frontend/` | Vite + React + TypeScript UI. `src/App.tsx` (compose page), `src/components/` (draft body, hover card, contacts page), `src/examples.ts` (prefilled demo requests), `src/api.ts` (reads `VITE_API_BASE`). |
| `pipeline/` | Offline extraction (`extract.py` calls the model; `verify.py` and `evaluate.py` do not). Its committed output in `pipeline/out/` is what the backend reads: `out/contacts/<email>.md` (33 contact notes) and `out/styles/<scenario>.json` (6 scenario styles). See `pipeline/README.md`. |
| `data/` | `emails/*.jsonl` (the sent emails), `external.json` (mock external context per recipient), `demo_scenarios.json`, `validate.py`. `ground_truth/` is the evaluation answer key: **do not read it** (see the rules below). |
| `recordings/` | Five recorded `POST /draft` request and response pairs, used by replay mode and the tests. |
| `fixtures/` | Generated fixtures checked by `scripts/check.sh`. |
| `scripts/check.sh` | Runs every repository check (see [Checks](#checks)). |

The backend only reads files; nothing is copied. Data locations can be changed with the environment variables
`EMAILS_DIR`, `CONTACTS_DIR`, `STYLES_DIR`, `EXTERNAL_FILE` and `STATUS_FILE` (see `backend/app/stores.py`).

## Rules for agents

- **Do not read `data/ground_truth/`, and do not read any `planted_*` field** in `data/emails/*.jsonl`. They are
  the answer key for evaluating the pipeline. Opening them to explain or "improve" a result is cheating. Only the
  checking scripts (`data/validate.py`, `pipeline/evaluate.py`) read them; running those is fine.
- **Start the backend with `RECORD=0`.** The default (`RECORD=1`) writes every live draft into `recordings/`,
  which changes tracked files.
- **Stop only processes you started**, by the PID or background task you own. Never use `pkill`, `killall` or
  `kill` by name or by port: other servers may be running on this machine. In Claude Code, this repository's
  `.claude/settings.json` denies `kill`, `pkill`, `killall` and `git clean` outright, so start servers as
  background tasks and stop them with the tool that stops a background task.
- **Do not push**, and do not commit unless the user asks you to.
- Do not rerun `pipeline/extract.py --force` unless asked: it makes about 40 model calls and rewrites
  `pipeline/out/`, which the recordings and fixtures depend on.

## Prerequisites

| Tool | Version | Check |
| --- | --- | --- |
| Python | **3.10 or newer** (tested with 3.12). macOS's `/usr/bin/python3` is 3.9 and cannot install the pinned packages. | `python3 --version` |
| Node.js | 18, 20, or 22 and newer (tested with 26) | `node --version` |
| `claude` (Claude Code CLI) | installed **and logged in**, needed only for live drafting | `claude --version` |

Live drafting runs `claude -p --output-format json --tools ""` as a subprocess, with `ANTHROPIC_API_KEY` and
`ANTHROPIC_BASE_URL` removed from its environment, so it uses the logged-in Claude subscription. To check that
`claude` works non-interactively:

```bash
echo "Reply with the word ok" | claude -p
```

Expected: `ok` (or similar) within a few seconds. Run inside this repository, it may first print a few
`Permission deny rule (.claude/settings.json): Write(...) is not matched ...` lines on stderr; they come from the
repository's agent settings and are harmless. If it asks you to log in, run `claude` once interactively and
log in, or skip live drafting and use [replay mode](#no-claude-replay-mode).

## Install

Backend (replace `python3` with `python3.12` or another 3.10+ interpreter if `python3 --version` is older):

```bash
( cd backend && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt )
```

Expected: ends with `Successfully installed ... fastapi-0.162.0 ... uvicorn-0.54.0`.

Front end:

```bash
( cd frontend && npm ci )
```

Expected: `added N packages` and no errors. Recent npm versions may warn that `esbuild` and `fsevents` have
install scripts "not yet covered by allowScripts"; the warning is harmless here and Vite still runs.

## Run the backend (live model)

Default ports are 8041 (backend) and 5181 (front end). If either is taken, pick any free port and use it
consistently in every command below, including `VITE_API_BASE`. Start the backend as a background process and
keep its PID:

```bash
( cd backend && RECORD=0 .venv/bin/uvicorn app.main:app --port 8041 )
```

Expected: `Uvicorn running on http://127.0.0.1:8041`. Then check it:

```bash
curl -s localhost:8041/health
```

Expected: `{"ok":true,"replay":false,"contract_revision":"0.3"}`.

```bash
curl -s localhost:8041/contacts | python3 -c "import json,sys; c=json.load(sys.stdin); print(len(c), [x['display_name'] for x in c][:3])"
```

Expected: `33 [...]`, the 33 contact notes in `pipeline/out/contacts/`.

Optional: draft one email with the real model from the command line. This takes **15 to 40 seconds**.

```bash
curl -s -X POST localhost:8041/draft -H 'Content-Type: application/json' -d '{"mode":"compose","to":"wang.jianhua@example.com","brief":"Confirm with Professor Wang when we can visit him at home next month, and ask if he would like us to bring anything."}' | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['subject']); print(''.join(s['text'] for s in d['segments'])); [print(h['strength'], h['layer'], h['label']) for h in d['highlights']]; print('warnings:', d['warnings'])"
```

Expected: a Chinese email that starts with `王老师：`, uses `您` and never `你`, and ends with `学生 Mia 敬上`.
The highlight list includes `strong person Greeting: "王老师"`, `strong person Formal "您"`,
`strong person Sign-off: "学生 Mia 敬上"` and several `weak person What you know: ...` facts. The wording changes on
every run.

## Run the front end

In a second background process:

```bash
( cd frontend && VITE_API_BASE=http://localhost:8041 npx vite --port 5181 )
```

Expected: `Local: http://localhost:5181/`. The Vite config uses `strictPort`, so a busy port fails instead of
moving to the next one. If `VITE_API_BASE` is unset, the front end calls `http://localhost:8041`.

Open http://localhost:5181 in a browser. The page shows a **To** picker (王建华 first) and a prefilled request.

## Demo walkthrough

Each **Generate draft** waits 15 to 40 seconds for the real model, and the wording and the highlighted phrases
differ on every run. Point at the highlights that actually appear. What to look for:

- **Solid underline** = strong: at least 3 of the user's emails support it and they are more than 30% of the
  emails in that group, or the user confirmed it with Keep.
- **Dashed underline** = weak: fewer emails, or external context (always weak, because it has a single mock
  source and does not come from the user's emails).
- The status line above the draft counts them, for example `5 backed by your emails · 3 to check`.
- **Hover** a highlight: a small card with a label and where it came from (`From your emails with ...`,
  `Your <scenario> style`, or `Recent context`). **Click** it: the card opens with the rationale, the quotes,
  **Show email** (the original email with the quote marked), and **Keep** / **Reject**.

The prefilled requests are in English (so the demo audience can follow), but the email is written in the
recipient's language, which comes from the contact note.

### 1. 王建华 (former advisor, formal Chinese)

Select **王建华 · advisor** (selected by default) and click **Generate draft**.

- The email is in Chinese and opens with `王老师：`, a **solid** greeting highlight. Hover it: `6 / 6`, "You
  addressed 王建华 as "王老师" in 6 of 6 emails."
- Every second-person pronoun is `您`, never `你`. Click a `您` highlight, then **Show email** to see the
  original sentence, for example `提前给您和李阿姨拜个早年`.
- The sign-off is `学生 Mia 敬上` (solid).
- Facts mentioned in only one or two emails (the planned visit, 普洱 tea, 李阿姨) are **dashed**.
- The calligraphy exhibition comes from external context (`社区公众号（mock）`) and is **dashed**.

### 2. Ethan Park (coach, casual English)

Select **Ethan Park · coach** and generate.

- English, opens with `Hi Ethan` or `Hey Ethan`, ends with `Best, Mia`. Contrast with 王建华: here almost
  nothing is solid, because the greeting appears in only 8 of 46 emails (below the 30% threshold). The status
  line often reads `0 backed by your emails`.
- The congratulations on the new baby and the Saturday walking group come from mock external context
  (Instagram, X) and are dashed; the card says `Recent context`.
- **Keep**: open a person-layer highlight (card subtitle `From your emails with Ethan Park`), click **Keep**. The
  underline turns solid at once and a toast says `Saved to Ethan Park's note.` The backend writes it to
  `backend/state/status.json`.
- **Reject**: on another person-layer highlight, click **Reject**. The underline disappears, the text stays, and
  the toast says `Won't use this for Ethan Park again.` On the next **Regenerate**, that entry is no longer
  offered to the model.
- Only person-layer entries are stored. Keep and Reject on a scenario habit (`Your ... style`) change the
  underline on screen only.

### 3. HOSHINOYA Kyoto (hotel, booking request)

Select **HOSHINOYA Kyoto (Kenji, Guest Relations) · hotel** and generate.

- English, addressed to `Kenji` (6 of 8 emails, solid).
- The request that Victor does not eat raw shellfish is a fact from one email (dashed).
- The autumn-leaves evening boat and the autumn tea gathering come from external context (the hotel's events
  page, mock), dashed, with source and date on the card.
- Scenario habits such as putting dates, nights and guests on one line come from all the user's hotel emails,
  not from this contact; their card says `Your vendor service style`.

### Failure case: the model cites a note that does not exist

Open http://localhost:5181/?inject=unknown_ref, pick any contact (Amy is prefilled for this case) and generate.
The backend renames one of the model's tags to a key that no note has. Expected: an amber warning above the
draft, `The model cited a note that does not exist ("fact:injected_unknown"); that text is shown without a
highlight.`, and that phrase is plain text with no underline. No reason is invented for it.

You may see more warnings of the same kind, for example `("soft_sentence_particles")`. Those are real mistakes by
the model (it sometimes cites a scenario habit without the `habit:` prefix), caught by the same fallback. They can
appear on any draft, not only with `inject`.

### Contacts page

The **Contacts** tab at the top lists every contact note with its entries, counts and quotes, so you can see
what the drafts draw on.

## No `claude`: replay mode

Without a logged-in `claude`, start the backend in replay mode instead. It serves the five drafts in
`recordings/` and never calls the model:

```bash
( cd backend && REPLAY=1 .venv/bin/uvicorn app.main:app --port 8041 )
```

`/health` then returns `"replay":true`. **Replay only matches a request that is identical to a recorded one**
(same recipient, mode, brief and `inject`). The front end's prefilled requests are now in English, while four of
the recordings were made with the original Chinese requests, so clicking **Generate draft** with the prefilled
text returns `404 no recording for case ...`. What works in replay mode:

- The failure case: open `/?inject=unknown_ref`, select **Amy**, generate. Its prefilled request matches
  `recordings/amy-wang-1a5bafc33e.json`.
- The other examples: replace the prefilled request with the recorded Chinese one before generating. Print them
  with:

```bash
python3 -c "import json,glob; [print(json.load(open(p))['request']['to'], '|', json.load(open(p))['request']['brief']) for p in sorted(glob.glob('recordings/*.json'))]"
```

Keep and Reject in replay mode return success but write nothing.

## Checks

```bash
scripts/check.sh
```

Runs five checks in order and stops at the first failure. Needs `backend/.venv` and `frontend/node_modules`
from [Install](#install). Expected last line: `check.sh: all checks passed at <time>.`

| Check | Command | What it verifies |
| --- | --- | --- |
| glossary | `scripts/check.sh __glossary` | No deprecated term is used in tracked files. The glossary is not committed, so a fresh clone prints `skipped`. |
| data-validate | `python3 -I data/validate.py` | Data integrity: message ids are unique, answer-key quotes are substrings of their emails, external context ids exist and are marked mock, and the demo scenarios resolve. |
| backend-tests | `cd backend && .venv/bin/python -m pytest -q` | Generator parsing, strength rules, replay, and the Keep/Reject feedback flow. No model calls. |
| frontend-build | `cd frontend && npx tsc -b && npx vite build` | The front end type-checks and builds. |
| fixtures-and-evidence | `cd backend && .venv/bin/python -m app.pipeline.make_fixtures --check` | `fixtures/drafts/` is up to date with `recordings/`, every fixture is a valid `Draft`, and every quote on every highlight is a verbatim substring of the email it cites. |

## Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| `No matching distribution found for fastapi==0.162.0` during install | Python is older than 3.10. Delete `backend/.venv` and recreate it with `python3.12 -m venv .venv` (or any 3.10+). |
| `address already in use` (uvicorn) or `Port 5181 is already in use` (Vite) | Another server has the port. Do not stop it. Pick a free port and pass it to both `--port` and `VITE_API_BASE`. |
| Generating takes 15 to 40 seconds | Normal: each draft is one real model call. The button shows `Writing as you would to ...` meanwhile. |
| `Could not write the draft: 502 ... model call failed: claude exited ...` | `claude` is missing, not on the backend's `PATH`, or not logged in. Run `echo hi \| claude -p` in the same shell; log in, or use replay mode. |
| `Could not load contacts: Failed to fetch` | The backend is not running, or `VITE_API_BASE` points at the wrong port. Restart Vite after changing it. |
| Keep or Reject shows `Could not save: 404 ... unknown draft or highlight` | Drafts live in the backend's memory, so a draft generated before the backend restarted is unknown to it. Click **Regenerate** and try again. |
| `404 no recording for case ...` | The backend runs with `REPLAY=1` and the request is not one of the recordings. See [replay mode](#no-claude-replay-mode). |
| Earlier Keep/Reject clicks still affect drafts | Feedback is an overlay in `backend/state/status.json` (git-ignored; the contact notes themselves are never rewritten). To reset, delete that file: `rm backend/state/status.json`. It is read on every request, so no restart is needed. |
| `git status` shows new files in `recordings/` | The backend was started without `RECORD=0`. Delete the new untracked files that `git status --short recordings/` lists (prefixed `??`), and restart with `RECORD=0`. |

## Stopping

Stop the two servers you started, by their PIDs or background tasks. Do not stop anything else.
