---
title: "ADR-T003: Dialogue and Letters Live in Plain-Text Script Files"
doctype: ADR
id: ADR-T003
domain: technical
status: accepted
date: 2026-04-29
tags: [dialogue, writing-pipeline, version-control, parser, reweave-strengthened]
constitution-clause: S3
supersedes: null
superseded-by: null
---
# ADR-T003: Dialogue and Letters Live in Plain-Text Script Files

## Context
Ines writes every letter and conversation, and she rewrites constantly. She needs to change text without opening the Godot editor or waiting on Tomas.

Night Post branches on letter state, such as whether Wren opened a letter ([[concepts/sealed-letter]]). Dialogue needs simple conditions, not a full scripting language.

## Decision
Dialogue and letters live in plain-text script files under version control. Ines edits them in any text editor, and a small in-house parser that Tomas maintains loads them into the game.

## Alternatives Considered
- **A node-graph dialogue plugin.** Graphs show branches visually, but they save to engine resource files that produce unreadable diffs and merge conflicts.
- **Spreadsheets.** Translators like them, but branching dialogue reads poorly in rows, and Ines would lose the flow of a scene.
- **An existing open-source dialogue language.** It does far more than Night Post needs, and its syntax would tie the project to someone else's release schedule.

## Consequences
- Every text change shows up as a readable diff, so Ines can review her own rewrites line by line.
- Tomas owns the parser, which keeps the syntax small: speaker lines, choices, and conditions on letter state and postmarks.
- Translation needs an export step that pulls strings out of the script files, which became work under [[decisions/product/PDR-P014-launch-languages|PDR-P014]].
- The decision adds clause S3 to [[architecture/CONSTITUTION]].
- **Reweave 2026-06-26:** strengthened by [[research/narrative/letter-length-test]] [emerging]: letters under 120 words were read in full 88% of the time, and letters over 200 words were skimmed or skipped 64% of the time. The parser now reports each letter's word count against the 120-word [[concepts/letter-budget]].
