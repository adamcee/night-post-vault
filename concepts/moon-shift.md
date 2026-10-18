---
title: Moon-Shift
id: moon-shift
date: 2026-05-05
status: Active
tags: [concept, navigation, moon]
---
# Moon-Shift

A moon-shift is the change in which paths connect which waymarks when the moon phase changes from one night to the next. Learning how Hollowmere rearranges under each phase is the core mastery of Night Post ([[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]]).

## How It Works in Play

- **One phase per night.** Each night has a single moon phase, shown when Wren picks up letters at dusk.
- **Paths move, waymarks don't.** The phase sets which paths join which [[concepts/waymark|waymarks]], while the waymarks stay in place ([[world/hollowmere]]).
- **Planning is the skill.** Players plan a route at dusk from what they remember about the current phase, then adjust on the road. Ledger scouts ahead to help ([[world/characters/ledger]]).

The rules live in [[architecture/systems/moon-and-paths]].

## Changes Since It Was Introduced

- **Players got lost.** In playtest 4, 6 of 10 players got lost after the first moon-shift ([[research/playtests/pt-04-vertical-slice]] [emerging]). PDR-P004 was weakened on 2026-08-18, not superseded.
- **Fixed landmarks fixed most of it.** Waymarks gained landmarks that never change ([[ideas/waymark-landmarks]]). In playtest 5, 2 of 12 players got lost ([[research/playtests/pt-05-demo-build]] [emerging]).
- **Paths are authored.** Every arrangement is hand-made, since procedural generation was rejected ([[decisions/rejected/ADR-T004-procedural-forest|ADR-T004]]).
- **Open question.** [[ideas/foldable-map]] proposes a map, which players asked for at the demo festival.
