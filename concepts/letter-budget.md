---
title: Letter Budget
id: letter-budget
date: 2026-06-26
status: Active
tags: [concept, writing, letters]
---
# Letter Budget

The letter budget is a soft limit of 120 words for the body of any in-game letter. Letters under 120 words get read in full; long letters get skimmed or skipped.

## Evidence

- **The test.** Nine players read 24 letters ([[research/narrative/letter-length-test]] [emerging]).
- **Under 120 words.** Players read letters under 120 words in full 88% of the time.
- **Over 200 words.** Players skimmed or skipped letters over 200 words 64% of the time.

## How It Works

- **Soft, not hard.** A letter may go over 120 words when the story needs it, but the writer should cut first and justify the rest.
- **Checked by tooling.** Letters live in plain-text script files, and the parser reports each letter's word count ([[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]]).
- **Fits the screen.** Short letters also fit the [[architecture/ui/letter-reader]] at handheld size without much scrolling ([[decisions/product/PDR-P011-readable-letters|PDR-P011]], [[architecture/CONSTITUTION]] P2).

## Why It Matters for Scope

Letters are 58% of the planned script's words ([[research/narrative/script-word-count]] [emerging]). Every word cut from a letter also cuts localization cost ([[decisions/product/PDR-P014-launch-languages|PDR-P014]]).
