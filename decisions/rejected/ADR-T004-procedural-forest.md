---
title: "ADR-T004: Procedural Forest Generation (Rejected)"
doctype: ADR
id: ADR-T004
domain: technical
status: rejected
date: 2026-05-01
tags: [procedural-generation, level-design, moon-shift]
constitution-clause: null
supersedes: null
superseded-by: null
---
# ADR-T004: Procedural Forest Generation (Rejected)

## Context
Hollowmere's paths rearrange with the moon, and Tomas proposed generating the forest layout procedurally each night. A generator promised endless variety and would spare Priya from painting every path.

## Decision
Rejected. Every path, waymark, and landmark in Hollowmere is placed by hand.

## Reasons for Rejection
- **Letters point to places.** A letter that says "the house past the split oak" needs that oak on that path every time the player reads it.
- **Painted scenes do not tile.** Priya paints each background as one scene, and a generator would need modular tiles that break the painted look.
- **Learning the forest is the mastery.** Players can only learn a layout that repeats, and random layouts would turn route planning into luck.
- **Testing cost.** Tomas would have to prove that every generated layout lets Wren reach every letter before dawn.

## Alternatives Considered
- **Hand-made layouts for each moon phase.** A small set of authored layouts keeps variety and stays learnable. The team adopted this approach in [[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]].
- **Procedural decoration only.** Scattering grass and glow-moss inside authored paths is allowed, because it changes no route.

## Consequences
- Priya paints more backgrounds, so the number of regions drives the art budget, a factor later in [[decisions/product/PDR-P012-three-regions|PDR-P012]].
- Fixed landmarks stay possible, which later gave players a way to orient after a shift ([[concepts/waymark]]).
- Future sessions should not reopen procedural layouts to save art time ([[concepts/moon-shift]]).
