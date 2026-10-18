---
title: "Localization Cost Estimate"
date: 2026-09-17
evidence-maturity: emerging
tags: [localization, translation, cost, budget]
method: "Ines collected written per-word quotes from three translation vendors and multiplied them by the three-region script count; an AI tool drafted a report that was then tightened."
source: "[[research/localization/_source-localization-cost-estimate]]"
---
# Localization Cost Estimate

Three vendors quoted $0.11 to $0.16 per word, so translating the 86,000-word script costs about $9,500 to $13,800 per language. Three quotes from one round make this `[emerging]`.

## Method
- **Quotes.** Ines requested written quotes from three translation vendors in early September, called Vendor A, B, and C in the vault. Each received the same brief and a 2,000-word sample of letters and dialogue.
- **Word count.** The estimate uses about 86,000 words, the three-region total from [[research/narrative/script-word-count]] [emerging].
- **Cost.** Each cost is the per-word rate multiplied by 86,000, rounded to the nearest $100 in the summary.

## Findings
| Vendor | Rate per word | Cost per language at 86,000 words | Includes |
|---|---|---|---|
| Vendor A | $0.11 | $9,460 | Translation only |
| Vendor B | $0.13 | $11,180 | Translation and one review pass |
| Vendor C | $0.16 | $13,760 | Translation, review, and in-game text check |

- **Per-word range.** Quotes ran from $0.11 to $0.16 per word.
- **Per-language cost.** Each language costs about $9,500 to $13,800.
- **Two languages.** Spanish and German together would cost about $18,900 to $27,500.
- **Price follows checking.** The higher quotes include a second translator's review and a check of the text in the running game.

## Limits
- **Three quotes.** Other vendors may quote outside this range.
- **Estimated words.** Most of the 86,000 words are not yet written, so the final count may move.
- **Text only.** The quotes cover written text, not voice recording or later patches.

## Provenance
An AI tool turned Ines's quote notes into a report, which was tightened through the ingestion gate on 2026-09-17. The untouched original is [[research/localization/_source-localization-cost-estimate]]; tightening removed an invented statistic (that each added language lifts sales by 26%) and corrected the per-language cost, which the original computed from the old five-region count of 142,000 words.

## Reweave Triggers
- [[decisions/rejected/PDR-P013-full-voice-acting|PDR-P013]]: feeds. Text translation alone costs $9,500 to $13,800 per language, before any recorded voice.
- [[decisions/product/PDR-P014-launch-languages|PDR-P014]]: feeds. Two launch languages beyond English cost about $18,900 to $27,500.
