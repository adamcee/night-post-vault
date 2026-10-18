---
title: "Playtest 4: Vertical Slice"
date: 2026-08-14
evidence-maturity: emerging
tags: [playtest, vertical-slice, moon-shift, readability, handheld, primary-research]
method: "Ten players played the 90-minute vertical slice on handheld PCs or desktops while a facilitator watched and timed them."
---
# Playtest 4: Vertical Slice

Six of ten players got lost after the first moon-shift, and four of ten squinted at the handwritten letters, all of them on handhelds. Players took a median of 71 minutes to finish the 90-minute slice; one session with ten players makes these findings `[emerging]`.

## Method
- **Build.** The build was the [[concepts/vertical-slice]], covering Thimble Cross and the road to Gloamwick with six letters, two parleys, and one moon-shift (the point where paths between waymarks rearrange with the moon phase).
- **Players.** Ten adults (P1–P10) from the devlog newsletter took part, none from earlier playtests. Six played on handheld PCs and four on desktops.
- **Sessions.** Sessions ran in person from 2026-08-10 to 2026-08-13, with a 90-minute cap and a short interview after.
- **Measures.** Ines timed each run and marked a player as lost after three minutes of walking without progress or a request for help. Priya noted when a player leaned in or squinted at a letter.

## Findings
| Player | Device | Minutes to finish | Lost after first moon-shift | Squinted at letters |
|---|---|---|---|---|
| P1 | Handheld | 72 | Yes | Yes |
| P2 | Desktop | 58 | No | No |
| P3 | Handheld | 84 | Yes | Yes |
| P4 | Handheld | 66 | No | No |
| P5 | Desktop | 75 | Yes | No |
| P6 | Handheld | 88 | Yes | Yes |
| P7 | Desktop | 63 | No | No |
| P8 | Handheld | 70 | Yes | Yes |
| P9 | Handheld | 69 | No | No |
| P10 | Desktop | 80 | Yes | No |

- **The moon-shift lost most players.** 6/10 got lost after the first moon-shift. They had learned routes by path shape, and the shift removed the shapes they knew.
- **Handwritten letters were hard to read on handhelds.** 4/10 squinted at the handwritten letters, all four on handhelds. No desktop player squinted.
- **Finishing took a median of 71 minutes.** Every player finished, and the six who got lost took longer than the four who did not.

## Player Quotes
- **P3:** "The bridge was right here an hour ago. Where's the ferry road?"
- **P6:** "I'm holding this up to my nose. Does it say 'owe' or 'own'?"
- **P8:** "Can Ledger just tell me which way is north?"
- **P2:** "I loved the shift. I just followed the tailor's shop sign."

## Limits
- **One moon-shift.** The slice had a single shift, so it cannot show whether players learn the forest over several nights.
- **Squinting is a proxy.** Watching faces shows discomfort but does not measure text size or contrast; [[research/accessibility/letter-readability-audit]] measured those later.
- **Small device split.** Six handheld players is too few to rate how often handheld players struggle.

## Reweave Triggers
- [[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]]: weakened. Six of ten players got lost after the first moon-shift; flagged for Ines, not superseded.
- [[decisions/product/PDR-P006-handwritten-letters|PDR-P006]]: weakened. Four of ten players squinted at handwritten letters, all on handhelds.
- [[prototype/implementation-plan]]: added a task to place fixed waymark landmarks that stay put through every moon-shift.
