---
title: "PDR-P006: Letters Appear in Handwritten Fonts"
doctype: PDR
id: PDR-P006
domain: product
status: superseded
date: 2026-05-15
tags: [letters, typography, ui, reweave-invalidated]
constitution-clause: null
supersedes: null
superseded-by: "[[decisions/product/PDR-P011-readable-letters]]"
---
# PDR-P006: Letters Appear in Handwritten Fonts

> **Superseded 2026-08-26** by [[decisions/product/PDR-P011-readable-letters|PDR-P011]] after the readability audit showed that handwritten body text fails contrast and size targets on a handheld.
>
> **Reweave 2026-08-21:** invalidated by [[research/accessibility/letter-readability-audit]] [emerging]: at 800p on a 7-inch screen, the handwritten font's body text failed the 4.5:1 contrast target on parchment and was below a comfortable size. Flagged for human review with a proposed superseding record.
>
> **Reweave 2026-08-14:** weakened by [[research/playtests/pt-04-vertical-slice]] [emerging]: 4 of 10 players on handhelds squinted at the handwritten letters.

## Context
Letters are the quests ([[decisions/product/PDR-P001-letters-are-the-quests|PDR-P001]]), and each sender should feel distinct before the player reads a word. Odile Marr writes in a tidy office hand, and Bram Ashby writes in a cramped, hurried one ([[world/characters/odile-marr]], [[world/characters/bram-ashby]]).

## Decision
Every letter appears on parchment in a handwritten font chosen for its sender ([[architecture/ui/letter-reader]]).

## Alternatives Considered
- **One clean typeface for all letters.** It is easy to read, but every sender looks the same.
- **Hand-drawn letter images.** They are the most personal option, but text inside images cannot be translated or resized, and it would break clause S3 of [[architecture/CONSTITUTION]].

## Consequences
- Priya picks a handwriting font for each recurring sender.
- Readability depends on each font, and nobody has measured the fonts at handheld size.
