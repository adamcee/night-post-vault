---
title: "PDR-P013: Full Voice Acting (Rejected)"
doctype: PDR
id: PDR-P013
domain: product
status: rejected
date: 2026-09-18
tags: [audio, voice, localization, budget]
constitution-clause: P4
supersedes: null
superseded-by: null
---
# PDR-P013: Full Voice Acting (Rejected)

## Context
The team weighed full voice acting while it budgeted translation. The three-region script runs about 86,000 words, and letters make up 58% of them ([[research/narrative/script-word-count]] [emerging]).

Translation alone costs $0.11–$0.16 per word, or about $9,500–$13,800 per language at 86,000 words ([[research/localization/localization-cost-estimate]] [emerging]). Voice would come on top of that for every language.

## Decision
Rejected. Night Post voices barks only: short lines such as greetings, reactions, and Ledger's calls. Letters and conversations stay as text.

## Reasons for Rejection
- **Cost scales with word count.** Voice cost grows with every word recorded, and the script is about 86,000 words.
- **Localization multiplies it.** Each translated language would need its own cast and recording sessions.
- **Letters are read.** Most of the script is letters, which the player reads at their own pace as written documents.
- **Late rewrites get expensive.** Ines rewrites until late in production, and recorded lines would either freeze the text early or need re-recording.

## Alternatives Considered
- **Voice the main characters only.** Odile Marr, Bram Ashby, and Mothwife Sel still carry a large share of the dialogue, and voiced characters beside silent ones feel uneven.
- **Voice English only.** Spanish and German players would get a lesser version of the game.

## Consequences
- Barks need a small cast and short sessions, and the bark list lives in the script files with all other text (clause S3).
- The decision keeps scope within clause P4 of [[architecture/CONSTITUTION]].
- Future sessions should not reopen full voice acting unless the budget changes.
