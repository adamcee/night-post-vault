---
title: "Script Word Count"
date: 2026-09-10
evidence-maturity: emerging
tags: [narrative, script, word-count, scope, localization]
method: "Ines counted written script words with the parser's word-count report and estimated unwritten content from region outlines at the average length of written letters and scenes."
---
# Script Word Count

The planned script runs to 142,000 words for five regions and about 86,000 words for three, and letters make up 58% of the words. Most of the count is still an estimate from outlines, so the findings are `[emerging]`.

## Method
- **Written words.** The script parser from [[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]] counted 31,000 words already written in the script files on 2026-09-09.
- **Planned words.** For unwritten content, Ines multiplied the outline's count of letters and scenes by the average length of written ones: 105 words per letter and 240 words per scene.
- **Shared text.** Menus, the tutorial, Ledger's comments, and postmark descriptions count once, outside any region.

## Findings
| Part of the script | Five-region plan | Three-region plan |
|---|---|---|
| Shared text (menus, tutorial, Ledger, postmarks) | 12,000 | 12,000 |
| Thimble Cross | 18,000 | 18,000 |
| Gloamwick | 24,000 | 24,000 |
| Sallow Ferry | 22,000 | 22,000 |
| The Drowned Bell | 34,000 | 6,000 (best story moved to Sallow Ferry) |
| The High Briar | 32,000 | 4,000 (folded into Gloamwick's edges) |
| **Total** | **142,000** | **86,000** |

- **Five regions.** The full plan needs 142,000 words.
- **Three regions.** Cutting the Drowned Bell and the High Briar, while keeping the Drowned Bell's best story and the High Briar's edges, brings the plan to about 86,000 words.
- **Letters dominate.** Letters are 58% of the words in both plans, about 50,000 words in the three-region plan.

## Limits
- **Mostly estimated.** Only 31,000 words exist; the rest assumes unwritten letters match the average length of written ones.
- **Letter budget pressure.** The 105-word average sits under the 120-word soft limit in [[concepts/letter-budget]], but later letters may run longer.
- **Unplanned lines.** Village chatter and creature reactions are not yet outlined, so the count leaves them out.

## Reweave Triggers
- [[decisions/product/PDR-P012-three-regions|PDR-P012]]: feeds. Cutting two regions removes about 56,000 words, from 142,000 to about 86,000.
- [[decisions/rejected/PDR-P013-full-voice-acting|PDR-P013]]: feeds. Full voice acting would cover about 86,000 words even after the cut.
- [[decisions/product/PDR-P014-launch-languages|PDR-P014]]: feeds. Each launch language means translating about 86,000 words.
