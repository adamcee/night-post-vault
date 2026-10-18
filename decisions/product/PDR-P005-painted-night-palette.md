---
title: "PDR-P005: Painted 2D Art With a Limited Night Palette"
doctype: PDR
id: PDR-P005
domain: product
status: accepted
date: 2026-05-12
tags: [art-direction, palette, accessibility, reweave-weakened]
constitution-clause: null
supersedes: null
superseded-by: null
---
# PDR-P005: Painted 2D Art With a Limited Night Palette

> **Reweave 2026-07-27:** weakened by [[research/accessibility/night-palette-colorblind-test]] [emerging]: under deuteranopia and protanopia simulation filters (two forms of red-green color blindness), the red and green route lanterns were indistinguishable. The palette stays, and red and green route lanterns get distinct shapes ([[prototype/implementation-plan]]). Flagged for human review; not superseded.

## Context
Night Post happens entirely at night, so the art must read in darkness without turning muddy. Priya is a painter, and a painted 2D style uses her strongest skill.

## Decision
Night Post uses painted 2D backgrounds and sprites in a limited night palette of deep blues, moss greens, and lantern ambers. Lantern light is the brightest thing on screen, and route lanterns use color to mark paths.

## Alternatives Considered
- **Low-poly 3D.** Priya would have to learn a new toolset, and real-time lights cost frames on the handheld floor ([[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]]).
- **Pixel art.** It is cheap to animate, but it cannot carry the soft glow-moss and fog that the setting needs.
- **A full day palette.** It reads more easily but loses the night mood. A day-night cycle was later proposed and rejected because it doubles background art ([[ideas/full-day-night-cycle]]).

## Consequences
- Every screen must stay readable with few colors, so light and dark contrast does work that hue does in brighter games.
- A small palette makes color-only signals risky, which the colorblind test later confirmed.
- Painted scenes cannot tile, which supports hand-placed paths ([[decisions/rejected/ADR-T004-procedural-forest|ADR-T004]]).
