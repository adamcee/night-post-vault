---
title: Reweave Protocol
id: reweave-protocol
date: 2026-04-06
status: Active
tags: [protocol, vault-administration, research, consistency]
---
# Reweave Protocol

When new information arrives, check whether the decisions and plans already in the vault still hold. A decision made six weeks ago rested on six-week-old evidence.

The [[vault-guide/decision-propagation-protocol]] runs the other way: it pushes a new decision forward into the plan.

## Trigger

Run it when new information enters the vault: a research doc, test results, customer or reader feedback, competitor news, a strategy shift, or an outside event. Also run the backfill step whenever a session reads a research doc in full or substantially edits one.

## Steps

The task is not complete until every step is done or marked N/A.

1. **Find affected docs.** Search for decision records, strategy docs, and design docs the new information touches. Ask of each: *"If this doc were written today, would its conclusions change?"*
2. **Classify the impact** on each affected doc:
    - **Strengthened.** Add a link to the new source in the doc's rationale.
    - **Weakened.** Write a dated note into the affected doc and flag it for the human.
    - **Invalidated.** Leave the doc unchanged, flag it for the human, and propose a superseding record through the [[vault-guide/decision-propagation-protocol]].
3. **Write the weakened note into the target.** Add a dated note near the top of the affected doc, for example `> **Reweave 2026-10-17 (weakened):** [[research/new-source]] finds X, which undercuts the claim that Y.` Strengthened docs get the same note with `(strengthened)`.
4. **Add `## Reweave Triggers` to the new doc.** List each affected file as a `[[wikilink]]` with its verdict and a one-line impact. If nothing is affected, write `No existing docs affected.`
5. **Route action items.** Every task the reweave produces, including each flag for the human, goes to [[prototype/implementation-plan]]. Never leave action items in the research doc.
6. **Log the reweave.** Append the verdicts to the current week's log, as described in [[vault-guide/session-logs]].

## Rules

- **Backfill on touch.** A research doc read in full or substantially edited that lacks `## Reweave Triggers` gets one before the task closes. The backlog shrinks one touched doc at a time, with no separate cleanup project.
- **The verdict lives in the target.** Backlinks show that a research doc links to a decision, but not whether it weakened it. The dated note in the target is what a later reader of that decision sees.
- **Never change an invalidated doc silently.** Only the human decides whether to supersede a decision. The session proposes, flags, and stops.
- **No promotion without triggers.** A research doc cannot leave `drafts/` without a `## Reweave Triggers` section ([[vault-guide/ingestion-gate]]).
- **Reweave depends on links.** It finds affected docs through [[vault-guide/research-traceability]] and [[vault-guide/wikilink-discipline]].

## Common Failure

Sessions treat new research as standalone: they write the doc, cite its contents, and stop. The decisions it affects keep their old rationale, and nobody notices until a choice built on them fails.
