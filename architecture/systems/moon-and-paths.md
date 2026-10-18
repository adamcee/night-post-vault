---
id: moon-and-paths
title: Moon and Paths System
date: 2026-05-05
status: Active
tags: [architecture, systems, moon-shift, navigation, waymarks]
---
# Moon and Paths System
*Updated 2026-09-25 after the waymark landmark fix.*

Each night has a moon phase, and the phase decides which paths connect which waymarks in [[world/hollowmere]] ([[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]]). Learning those layouts is the main skill the game teaches, and fixed landmarks keep players from getting lost while they learn.

Terms: a [[concepts/moon-shift]] is the change of path layout between phases, and a [[concepts/waymark]] is a lantern post at a junction.

## Four Phases, Four Layouts
- **Phases:** new, waxing, full, and waning. The phase advances one step each night, so a full cycle takes four nights.
- **Layouts:** each region has one hand-authored path layout per phase. Paths connect waymarks, and a moon-shift swaps which pairs connect.
- **Hand-authored, not generated:** letters and landmarks need authored paths, so procedural forest generation was rejected ([[decisions/rejected/ADR-T004-procedural-forest|ADR-T004]]).
- **Telling the phase:** the moon shows in the sky on every screen, and Ledger names the phase at dusk.

## Fixed Landmarks Stop Players Getting Lost
In the vertical slice, 6 of 10 players got lost after the first moon-shift ([[research/playtests/pt-04-vertical-slice]] [emerging]). That weakened PDR-P004 on 2026-08-18, though the team kept the decision and added landmarks instead of superseding it.

- **What a landmark is:** a large shape at a waymark that looks the same under every phase, such as a split oak, a stone well, or a boot nailed to the post. Paths move, and landmarks do not.
- **Where they go:** every waymark has its own landmark, so no two junctions look alike ([[concepts/waymark]]).
- **Result:** in the demo build, 2 of 12 players got lost, down from 6 of 10 ([[research/playtests/pt-05-demo-build]] [emerging]).
- **Origin:** the fix started as [[ideas/waymark-landmarks]] and was absorbed into [[prototype/implementation-plan]].

## Waymark Lanterns Mark Routes
- **Who lights them:** the [[world/factions/lamplighters-union]] keeps the waymark lanterns lit. Their quarrel with the Night Post over oil shapes stories in [[world/regions/gloamwick]].
- **Color and shape:** route lanterns use color and a distinct shape, because red and green lanterns were indistinguishable under deuteranopia and protanopia filters ([[research/accessibility/night-palette-colorblind-test]] [emerging]). This weakened [[decisions/product/PDR-P005-painted-night-palette|PDR-P005]] on 2026-07-27.

## Route Planning Before Each Night
- At dusk Wren sees tonight's letters and the phase. The player plans from memory and from Ledger's scouting, with no full map.
- Ledger can fly ahead to one waymark per night and report which paths connect there ([[world/characters/ledger]]).
- Longer routes burn more [[concepts/lantern-oil]] ([[architecture/systems/lantern-oil-economy]]).

## Map Requests Are an Open Question
- 23 festival comments asked for a map ([[research/market/demo-festival-results]] [emerging]).
- A full map of every phase would remove the skill PDR-P004 is built on. The request waits in [[ideas/foldable-map]] until the evaluation task in [[prototype/implementation-plan]] is done.
- Any map must keep text readable at handheld size (clause P2 of [[architecture/CONSTITUTION]]) and hold 30 frames per second on the [[concepts/handheld-floor]].

## Performance Note
Volumetric fog dropped to 38 frames per second in Gloamwick on a handheld PC, and a baked fog layer held 30 or more everywhere ([[research/technical/handheld-perf-benchmark]] [emerging]). Night scenes use the baked layer.
