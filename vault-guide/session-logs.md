---
title: Session Logs
id: session-logs
date: 2026-04-06
status: Active
tags: [protocol, vault-administration, logs]
---
# Session Logs

Every session that changes the vault appends one line to `session-history.md` and one section to the current weekly log. Both files are append-only, so a crashed or concurrent session can never erase another session's record.

- **`session-history.md`** at the vault root: one line per session under its date. The session start protocol reads its last heading to find what changed.
- **`prototype/implementation-logs/YYYY-Www.md`**: one file per ISO week, with a short section per session describing what changed and why.

## Trigger

Run it at the end of any session that wrote to the vault, and whenever a protocol says to log its result.

## Steps

1. **Find today's date and ISO week.** Run `date +%F` and `date +%G-W%V`.
2. **Append to `session-history.md`.** If today's `## YYYY-MM-DD` heading is missing, append it first. Then append one line in the form `- (agent, session type) what changed`.
3. **Append to the weekly log.** If this week's file doesn't exist, create it with frontmatter and a `# Implementation Log YYYY-Www` title. Then append a section headed `## YYYY-MM-DD (agent, session type)` with bullets for files changed, decisions made, reweave verdicts, and action items routed.
4. **Update the checkpoint.** Rewrite the Last Session Checkpoint in [[AGENTS]] in one or two sentences. It is the one log-like text that is replaced, not appended.
5. **Run the lint.** Run `python3 .claude/skills/vault-maintenance/vault-lint.py` and fix every failure before closing.

## Appending Safely

Append with a single shell command or an MCP append tool, never by reading the file and writing it back.

```bash
grep -q "^## 2026-10-17$" session-history.md || printf '\n## 2026-10-17\n' >> session-history.md
printf -- '- (claude-code, research) Added research/pricing-survey and reweaved two strategy docs.\n' >> session-history.md
```

Over MCP, use the append tool for each line. In web chat, give the user the line to paste at the end of the file.

## Rules

- **Append only.** Never rewrite, reorder, or reformat either log. A session that rewrites the file can erase entries another session added minutes earlier.
- **Past weeks are closed.** A weekly file is never edited after its week ends.
- **Correct forward.** Fix a wrong entry with a dated correction note in the current week's file that names the old entry, such as `Correction to 2026-10-03 entry: the survey had 40 responses, not 400.`
- **The lint enforces it.** `vault-lint.py` fails when either log lost lines since the last commit, or when a heading is malformed. Users without Python check by eye that the diff only adds lines.
- **One line means one line.** The history entry names the agent, the session type, and what changed; the detail goes in the weekly log.
- **The logs agree.** Every session in `session-history.md` has a section in that week's log, and the reverse.

## Common Failure

A session rebuilds `session-history.md` from its own copy, silently dropping lines a parallel session appended. The next session start then reads the wrong last date and misses changes.
