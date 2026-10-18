---
id: vertical-slice
title: Vertical Slice Spec
date: 2026-07-01
status: Done
tags: [prototype, spec, vertical-slice, milestone]
---
# Vertical Slice Spec
*Built 2026-07-06 to 2026-08-28. Tested from 2026-08-10 to 2026-08-13 in [[research/playtests/pt-04-vertical-slice]].*

The vertical slice is a 90-minute build of Night Post at near-final quality, made to prove that the core loop works before the team builds more content. A [[concepts/vertical-slice]] is one thin piece of the game finished through every layer: art, writing, music, systems, and saves.

## What the Slice Contains
- **Regions:** all of [[world/regions/thimble-cross]] and the first night route into [[world/regions/gloamwick]].
- **Nights:** two nights under different moon phases, so the player meets one [[concepts/moon-shift]] ([[architecture/systems/moon-and-paths]]).
- **Letters:** six letters, each within the 120-word [[concepts/letter-budget]], including two sealed letters ([[concepts/sealed-letter]]).
- **Parley:** two encounters using talk, offer, and shine ([[architecture/systems/parley]]).
- **Postmarks:** fast and kind only, with tier 1 abilities ([[architecture/systems/postmarks]]).
- **Oil and satchel:** the full oil and weight rules from [[architecture/systems/lantern-oil-economy]].
- **Characters:** Wren, Ledger, [[world/characters/odile-marr]], and [[world/characters/the-quiet-lamplighter]].
- **Letters on screen:** fully handwritten, as [[decisions/product/PDR-P006-handwritten-letters|PDR-P006]] set at the time ([[architecture/ui/letter-reader]]).

## Technical Requirements
- **Performance:** 30 frames per second at 800p on the handheld floor ([[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]]), with baked fog in Gloamwick ([[research/technical/handheld-perf-benchmark]] [emerging]).
- **Saves:** write to a temp file, then rename ([[decisions/technical/ADR-T005-atomic-saves|ADR-T005]]).
- **Music:** two layers that thin out on long walks and return at arrivals ([[decisions/technical/ADR-T006-adaptive-music-layers|ADR-T006]]).
- **Script:** all text in plain-text files loaded by the in-house parser ([[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]]).
- **Colorblind lanterns:** route lanterns use distinct shapes as well as color ([[research/accessibility/night-palette-colorblind-test]] [emerging]).

## Done Criteria
- A new player can finish the slice in 90 minutes or less without help.
- No encounter can end the game (clause P1 of [[architecture/CONSTITUTION]]).
- The build holds 30 frames per second on the handheld through the whole slice.
- Ten playtesters play it, and the results go in a research doc.

## Result: Done, With Two Problems Found
Playtest 4 ran on the feature-complete slice from 2026-08-10 to 2026-08-13 with 10 players and was written up on 2026-08-14, and the median player finished in 71 minutes ([[research/playtests/pt-04-vertical-slice]] [emerging]). The team fixed bugs for two more weeks and closed the milestone on 2026-08-28.

- **Players got lost:** 6 of 10 got lost after the first moon-shift. This weakened [[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]] and led to fixed waymark landmarks.
- **Handheld players squinted:** 4 of 10 on handhelds squinted at the handwritten letters. With [[research/accessibility/letter-readability-audit]], this led [[decisions/product/PDR-P011-readable-letters|PDR-P011]] to supersede PDR-P006.

Both fixes went into the [[prototype/specs/festival-demo]].
