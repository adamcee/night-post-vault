---
title: Ingestion Gate
id: ingestion-gate
date: 2026-04-06
status: Active
tags: [protocol, vault-administration, drafts, writing-discipline]
---
# Ingestion Gate

AI-generated content lands in `drafts/` first and enters the vault only after passing the promotion checklist. Untightened AI prose costs every later reader time, and later sessions copy its style.

## Trigger

Apply it to any AI-generated content meant for the vault: research reports, syntheses, competitive or market analyses, long drafts, and outputs pasted in from another AI tool. It also applies when a session must stop mid-task and leave a hand-over note.

## Steps

1. **Land it in `drafts/`.** Save new AI content as `drafts/<name>.md`, never directly in `research/`, `strategy/`, or another vault folder.
2. **Fix errors instead of annotating them.** Correct factual mistakes, remove invented claims, and rewrite misframed sections. Save the untouched original as `_source-<name>.md` in the same folder as the clean doc.
3. **Run the promotion checklist** below until every item passes.
4. **Promote with a link-rewriting move.** Move the file from `drafts/` to its vault folder with the Obsidian move command (in the app, the CLI `move`, or an MCP move tool), which updates every link to it.
5. **Run the follow-on protocols.** A promoted research doc triggers the [[vault-guide/reweave-protocol]], and any action items go to [[prototype/implementation-plan]].

## Promotion Checklist

- [ ] **Tightening checklist.** The doc passes the checklist in [[AGENTS]] and the rules in [[vault-guide/style-guides/ai-writing-discipline-core]], or [[vault-guide/style-guides/research-paper-discipline]] for research docs.
- [ ] **Slop purge.** The slop words named in the style guide (*delve, testament, tapestry, synergy, robust, landscape, leverage*) are gone or replaced with plain words.
- [ ] **Meta-commentary removed.** No *"This section covers,"* *"As previously discussed,"* *"It is worth noting,"* or *"The following table shows."*
- [ ] **Paragraphs compressed.** No paragraph runs past two sentences, except single-thought paragraphs in research docs.
- [ ] **Reweave Triggers.** A research doc has a `## Reweave Triggers` section, even if it reads `No existing docs affected.`

## Repairing a Bad Move

If someone promoted a file with `mv`, `git mv`, or copy-then-delete, links still point at the old `drafts/` path. Search for the old path (`grep -rl "drafts/<name>" --include="*.md" .`), retarget each link to the new path, and run the link checker from [[vault-guide/wikilink-discipline]].

After a copy-then-delete that left both copies in place, retarget the links first, then delete the `drafts/` copy.

## Hand-Over Notes

A session that must stop before finishing writes `drafts/YYYY-MM-DD-resume-<topic>.md`. It lists what is done, what comes next, open questions, and the files touched, so the next session resumes without re-reading the whole task.

The next session reads the note, finishes the work, and deletes the note when the task closes. Hand-over notes never get promoted.

## Rules

- **No cruft.** The vault-facing doc is accurate, not a record of mistakes. A doc that says *"warning: this section is wrong"* is a to-do, so fix the section and keep the original in `_source-<name>.md`.
- **Originals stay beside the clean doc.** The `_source-<name>.md` file sits in the same folder as the promoted doc, for citation and audit.
- **Never `mv` or copy-then-delete a vault file.** Use a move that rewrites links, and repair right away if a plain move happens.
- **Checkboxes don't survive promotion.** Task checkboxes in a draft are routed to the ledger or removed before it moves.
- **The gate applies to every model.** Content from any AI tool, including the one running the session, passes the same checklist.

## Common Failure

A session pastes a long AI report straight into `research/` because it looks useful. Every later session reads its hedges and padding as the project's voice, and its errors sit unflagged next to verified evidence.
