---
name: vault-start
description: "Session bootstrap for the vault. MUST be invoked at the start of every AI session before any substantive work. Triggers: /vault-start, beginning of any session, or when AGENTS.md or a pointer file instructs you to run the startup protocol. Also use when you realize mid-session that you skipped the startup protocol."
---

# Vault Session Bootstrap

This skill runs the Session Start Protocol in `AGENTS.md`. It exists because `AGENTS.md` loaded as passive context doesn't reliably get the protocol executed, so every step below is a tool call: a fresh read or command, never a memory of a past session.

**Run every step in order. Don't skip or abbreviate any.** If you realize mid-session that you skipped this skill, run it now before continuing.

## Step 1: Read AGENTS.md

Read `AGENTS.md` in full with your environment's read tool (`read_file` or equivalent in a CLI, `obsidian_read` or equivalent over MCP), even if your tool already loaded it as context. Note the Last Session Checkpoint, Hard Constraints, Standing Decisions, Current Phase, and Post-Task Completion Gate, since they govern everything you do this session.

## Step 2: Read Your Tool's Pointer File

Read the pointer file for your tool: `CLAUDE.md` (Claude Code, Claude Desktop), `GEMINI.md` (Antigravity CLI, Gemini CLI), `.cursorrules` (Cursor), or `.windsurfrules` (Windsurf). Pointer files hold only tool mechanics, such as MCP tool names, write-size limits, and skill locations, and no project content.

## Step 2.5 (Antigravity or Gemini CLI Only): Sync Skills

Antigravity CLI reads skills from `.agents/skills/`; Gemini CLI uses `gemini skills list`. If either is missing a folder from `.claude/skills/`, run the `sync-skills` skill before continuing.

## Step 3: Find What Changed Since the Last Session

Take the last session date from the last `## YYYY-MM-DD` heading in `session-history.md`:
- **CLI:** `grep '^## ' session-history.md | tail -1`
- **MCP:** read `session-history.md` and take the last date heading, or search it for `## 20` and use the last match.

Then list the files changed since that date:
- **Git (preferred):** `git diff --name-status $(git log -1 --before="YYYY-MM-DD 00:00" --format=%H)`. The `00:00` matters: a bare date means that date at the current time of day, so a session run later the same day would find nothing.
- **No git:** `find . -type f -newermt "YYYY-MM-DD" ! -path "*/.git/*" ! -path "*/.obsidian/*"`
- **MCP without a modified-since filter:** search vault content for the date prefix, using the last session's month as the lower bound (`2026-10` for a last session in October). Repeat the search scoped to `prototype/implementation-logs/`. A bare date search also catches stray daily notes at the vault root.
- **None of these:** ask the user what changed.

Review the results and flag for the user:
- New or changed root-level files, including stray `YYYY-MM-DD.md` daily notes.
- New decision records in `decisions/`.
- New files in `drafts/` awaiting the ingestion gate.
- Changes to `architecture/` or `prototype/` that touch the current phase.

## Step 4: Identify the Session Type

Ask the user what kind of session this is, with your tool's question tool if it has one. Offer the types listed under Task-Specific Context Loading in `AGENTS.md`, such as planning, research, decision, strategy, writing, coding, or vault maintenance, plus **Other**.

## Step 5: Load Task-Specific Context

Read each file `AGENTS.md` lists for that session type under Task-Specific Context Loading.
- **Vault maintenance:** also read the README of any folder you will change. If you will edit a skill in `.claude/skills/`, read its `SKILL.md` first.
- **Other, or no listed type fits:** read `vault-guide/vault-design-philosophy.md`, list the files in the folder most relevant to the request, and read that folder's `README.md`.

## Step 6: Confirm Readiness

Tell the user, in a few sentences rather than a report:
- What changed since the last session, including anything you flagged in Step 3.
- What context you loaded for this session type.
- Anything odd about the vault's state that you noticed, such as blank pages, broken links, a stale Last Session Checkpoint, or a missing log entry.
- That you're ready to start.
