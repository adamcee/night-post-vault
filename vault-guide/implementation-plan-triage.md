---
title: Implementation Plan Triage
id: implementation-plan-triage
date: 2026-04-06
status: Active
tags: [protocol, vault-administration, maintenance, ledger]
---
# Implementation Plan Triage

Triage is a periodic cleanup of [[prototype/implementation-plan]] that closes finished tasks, removes stale ones, and moves reference content out. It keeps the ledger accurate and short enough for a session to read; it never changes what matters most.

## Trigger

- **The ledger passes about 200 open items.** A longer list is hard for a session to read and act on.
- **A major change in direction** leaves tasks that assume the old plan, tools, or scope.
- **Every quarter**, even without another trigger. Deadlines pass, files move, and work gets done without its checkbox being ticked.

## Steps

1. **Record the starting counts.** Count open tasks and lines: `grep -c '^- \[ \]' prototype/implementation-plan.md` and `wc -l prototype/implementation-plan.md`.
2. **Cross-check the weekly logs.** Read `prototype/implementation-logs/` for work that was logged but never ticked. Mark those tasks `[x]` with the date and the log that shows it.
3. **Check the files tasks mention.** A task that says "create X" or "move Y" may already be done, so confirm on disk before marking it. A task that names a file that no longer exists is stale; close it with a note.
4. **Flag superseded tasks.** After a change in direction, search for tasks that use the old tools, terms, or assumptions. Mark each `**SUPERSEDED**` with a link to the decision that replaced it.
5. **Flag overdue tasks.** Mark tasks whose deadline has passed `**OVERDUE**`, so the human can resolve or remove them.
6. **Move out reference content.** Narrative, contact tables, meeting notes, and background belong in their canonical vault docs, not the ledger. Leave a one-line provenance note in the ledger, such as `*(Moved to [[strategy/partners]], YYYY-MM-DD triage.)*`.
7. **Merge, don't sprawl.** Fold relocated or duplicate tasks into existing sections instead of creating new standalone ones.
8. **Record the result.** Add a row to the History table below with before and after counts and the main actions, then log the session ([[vault-guide/session-logs]]).

## Rules

- **No reprioritizing.** Triage finds stale, done, and misplaced tasks. Ranking what matters is the human's call.
- **Flag, don't force.** Merging overlapping sections or dropping a whole phase is a judgment call. List candidates for the human instead of doing it.
- **Shrink, don't grow.** Add a task only when the pass uncovers real missing work.
- **Every closure has evidence.** A task is marked done only with a log entry, a file on disk, or a decision record behind it.
- **Reweave after relocation.** If reference content moved to a new vault doc, run the [[vault-guide/reweave-protocol]] so links follow it.
- **The human's list is off limits.** Triage edits only the ledger, never `prototype/human-task-list.md`.

## Common Failure

The ledger grows past a few hundred items, half of them done or obsolete. Sessions stop trusting it, start tracking work elsewhere, and the vault loses its single list of what is next.

## History

| Date | Before | After | Key actions |
|---|---|---|---|
| YYYY-MM-DD | [open tasks] open / [lines] lines | [open tasks] open / [lines] lines | [What the pass closed, moved, merged, or flagged.] |
