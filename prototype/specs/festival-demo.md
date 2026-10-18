---
id: festival-demo
title: Festival Demo Spec
date: 2026-08-28
status: Done
tags: [prototype, spec, demo, festival, milestone]
---
# Festival Demo Spec
*Built 2026-08-31 to 2026-09-26. Shown at the online demo festival from 2026-09-29 to 2026-10-05.*

The festival demo is a free 40-minute build of Night Post for an online demo festival, made to grow wishlists and test the fixes from the vertical slice with strangers. It starts from the [[prototype/specs/vertical-slice]] and adds the fixes that playtest 4 called for.

## What the Demo Contains
- **Regions:** [[world/regions/thimble-cross]] and the first night route into [[world/regions/gloamwick]], as in the slice.
- **Nights:** two nights, with one [[concepts/moon-shift]] at the start of night two.
- **Letters:** the slice's six letters, trimmed and reordered, including two sealed letters.
- **Ending:** the demo closes on the second sealed letter, addressed to [[world/characters/bram-ashby]] at [[world/regions/sallow-ferry]], which the player can open or leave sealed.
- **Postmarks:** all four kinds, with tier 1 abilities ([[architecture/systems/postmarks]]).

## Changes Since the Slice
| Change | Why | Source |
|---|---|---|
| Fixed waymark landmarks at junctions | 6 of 10 slice players got lost after the first moon-shift. | [[research/playtests/pt-04-vertical-slice]] [emerging], [[architecture/systems/moon-and-paths]] |
| Readable letter body, handwritten header and signature | Handwritten body text failed 4.5:1 contrast at 800p. | [[research/accessibility/letter-readability-audit]] [emerging], [[decisions/product/PDR-P011-readable-letters]] |
| Font toggle in settings and reader | Players can switch the body text to a plainer, larger typeface. | [[architecture/ui/letter-reader]] |
| Shorter opening | The demo had to fit a festival session, well under the slice's 71-minute median. | [[research/playtests/pt-04-vertical-slice]] [emerging] |

## Done Criteria
- A new player finishes the demo in about 40 minutes.
- No more than 1 in 5 remote playtesters gets lost.
- The build holds 30 frames per second at 800p on the handheld floor ([[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]]).
- The demo ends with a wishlist prompt and no other store links.

## Result: Done, and the Fixes Worked
- **Playtest 5, 2026-09-25:** 12 remote players. 9 of 12 finished, 2 of 12 got lost, down from 6 of 10, and 5 of 12 turned on the font toggle; the median session was 38 minutes ([[research/playtests/pt-05-demo-build]] [emerging]).
- **Festival, 2026-09-29 to 2026-10-05:** 3,140 players tried the demo, 41% finished it, and wishlists rose from 1,900 to 6,450 ([[research/market/demo-festival-results]] [emerging]).
- **Comments:** players praised the letters and the tone, and 23 comments asked for a map. The request is open in [[ideas/foldable-map]].

The next milestone is Production in [[prototype/implementation-plan]].
