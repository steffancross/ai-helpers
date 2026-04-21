# ai-helpers

Small CLI that runs predefined LLM prompt flows.

## Install

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
uv tool install .
```

This puts `ai` on your PATH in an isolated env. Re-run the same command after pulling changes to reinstall.

## Setup

```bash
cp .env.example .env
# edit .env and paste your ANTHROPIC_API_KEY
```

`ai` loads `.env` from the current working directory (or any parent), so run it from the project dir or a dir that has one.

## Flows

### `anki` — Japanese flashcard entry

```bash
ai anki 訳
ai anki          # prompts for the word
```

Outputs a plain-text block in the exact Anki format (word / reading / meaning / furigana / sentence / sentence meaning / sentence furigana / optional notes). Paste straight into Anki.

### `coverletter` — company-specific sentence options

```bash
ai coverletter --company Stripe --interest "love their infra team"
# paste the job description, then Ctrl-D
```

Reads the job description from stdin. Outputs 5 distinct 1–2 sentence candidates to drop into the `COMPANY LINE` slot in your base cover letter.

You can also pipe it in:

```bash
pbpaste | ai coverletter --company Stripe
```

## Adding a new flow

1. Create `ai_helpers/prompts/<name>.md` — system prompt, then `---` on its own line, then the user-message template with `{placeholders}`.
2. Create `ai_helpers/flows/<name>.py` with a `run_<name>(...)` function that loads the prompt, renders it, and calls `call_llm`.
3. Re-export it from `ai_helpers/flows/__init__.py`.
4. Add a subcommand in `ai_helpers/cli.py`.
5. `uv tool install .` to reinstall.

## Architecture notes

- `ai_helpers/llm.py` is the only file that imports `anthropic`. Swapping providers is a one-file change.
- Flow functions (`run_anki`, `run_coverletter`) take plain args and return strings. The CLI layer is a thin wrapper around them, so a future web UI can import and call the same functions.
