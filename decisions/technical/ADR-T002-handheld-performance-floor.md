---
title: "ADR-T002: A Handheld PC Is the Performance Floor"
doctype: ADR
id: ADR-T002
domain: technical
status: accepted
date: 2026-04-15
tags: [performance, handheld, platform, reweave-strengthened]
constitution-clause: S2
supersedes: null
superseded-by: null
---
# ADR-T002: A Handheld PC Is the Performance Floor

## Context
Night Post is a slow, text-heavy game that suits short sessions away from a desk. Ines and Tomas both play narrative games on handheld PCs and expected much of the audience to do the same, but no data existed when they wrote this record.

The weakest supported device limits every art and shader choice. Choosing that device late would mean redoing art.

## Decision
A handheld PC is the minimum target. Night Post must hold 30 fps (frames per second) at 800p (1280×800 pixels) on that device, and no scene counts as done until it passes there ([[concepts/handheld-floor]]).

## Alternatives Considered
- **Desktop PC as the floor, handheld as a stretch goal.** Art and effects would grow past what a handheld can run, and cutting them late costs more than never adding them.
- **60 fps at 800p.** Night Post has no fast action, and 60 fps would halve the frame time available for lighting and fog.
- **Handheld support after launch.** It would need a second art and optimization pass on the densest scenes.

## Consequences
- All text must be readable on a 7-inch screen, which later shaped [[decisions/product/PDR-P011-readable-letters|PDR-P011]].
- Every shader and particle effect needs a handheld measurement before it ships.
- The decision adds clause S2 to [[architecture/CONSTITUTION]].
- **Reweave 2026-06-05:** strengthened by [[research/technical/handheld-perf-benchmark]] [emerging]: the greybox averaged 52 fps on a handheld PC, but the volumetric fog shader dropped to 38 fps in Gloamwick. Fog moved to a baked layer, which held 30+ fps everywhere and leaves headroom for final art.
- **Reweave 2026-07-10:** strengthened by [[research/market/community-survey-01]] [emerging]: 61% of 214 respondents play on a handheld PC at least sometimes.
