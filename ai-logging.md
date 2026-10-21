# AI-Use Logging (CS 483 Programming Assignment 2)

This repo's assignment instructions require attaching and reporting on any use
of LLMs. Follow this logging protocol throughout the session.

## When to log

After any exchange where you (Claude) provide meaningful help — explaining a
concept, suggesting code, debugging an error, reviewing my implementation —
append an entry to `llm_log.md` in the repo root. Do this proactively,
without waiting for me to ask. Create `llm_log.md` if it doesn't exist yet.

## Entry format

Append entries in this format, newest at the bottom:

```markdown
## [YYYY-MM-DD HH:MM]

**Context:** What file/function/problem we were working on.

**Prompt/question:** A short paraphrase of what I asked.

**What Claude did:** Explained a concept / suggested code / debugged an
error / reviewed logic — be specific about which.

**Outcome:** Did I use the suggestion as-is, adapt it, or reject it and
write my own version? Note any significant edits I made afterward.
```

## Reminders

- Log design discussions and debugging help, not just finished code
  Claude wrote — the assignment cares about *how* AI was used, not just
  final output.
- If I explicitly rewrite or diverge from a suggestion, note that in the
  Outcome field rather than leaving the entry looking like the suggestion
  was adopted unchanged.
- Keep entries honest and specific (e.g. "explained why the Sobel kernel
  orientation was flipped" is better than "helped with edge detection").
- This log only covers this Claude Code session. If I also used a separate
  chat tool (claude.ai, ChatGPT, etc.) for parts of the assignment, I'll
  paste those exchanges in manually — remind me if a gap seems likely.
