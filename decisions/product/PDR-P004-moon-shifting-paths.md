---
title: "PDR-P004: Paths Rearrange by Moon Phase"
doctype: PDR
id: PDR-P004
domain: product
status: accepted
date: 2026-05-05
tags: [moon-shift, navigation, level-design, reweave-weakened]
constitution-clause: null
supersedes: null
superseded-by: null
---
# PDR-P004: Paths Rearrange by Moon Phase

> **Reweave 2026-09-25:** strengthened by [[research/playtests/pt-05-demo-build]] [emerging]: after waymark landmarks went in, 2 of 12 players got lost, down from 6 of 10. The fix holds.
>
> **Reweave 2026-08-18:** weakened by [[research/playtests/pt-04-vertical-slice]] [emerging]: 6 of 10 players got lost after the first moon-shift. Moon-shift stays, and a plan task adds fixed waymark landmarks that never move ([[prototype/implementation-plan]], [[ideas/waymark-landmarks]]). Flagged for human review; not superseded.

## Context
Hollowmere is a forest whose paths rearrange with the moon. The team wanted route planning to be the skill players build, in place of combat or stats.

## Decision
Each night has a moon phase, and the paths between waymarks rearrange by phase ([[concepts/moon-shift]]). Layouts are made by hand, one per phase in each region, so players can learn them ([[architecture/systems/moon-and-paths]]).

## Alternatives Considered
- **Fixed paths.** They are easier to build and learn, but the forest loses its central mystery.
- **Procedural layouts.** [[decisions/rejected/ADR-T004-procedural-forest|ADR-T004]] rejected them because letters and landmarks need authored paths.
- **Random rearrangement each night.** Players could not plan routes, so mastery would turn into luck.

## Consequences
- Each region needs several layouts, which multiplies level work by the number of phases.
- Players need a way to orient after a shift, and waymarks serve as the anchor points ([[concepts/waymark]]).
- Planning a route by moon phase becomes the second step of the core loop ([[architecture/game-design-overview]]).
