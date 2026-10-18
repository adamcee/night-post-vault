---
title: Handheld Floor
id: handheld-floor
date: 2026-04-15
status: Active
tags: [concept, performance, handheld]
---
# Handheld Floor

The handheld floor is Night Post's minimum performance target: 30 fps at 800p on a handheld PC. If a scene misses the floor on the handheld, it gets changed until it meets it ([[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]], [[architecture/CONSTITUTION]] S2).

## Why a Handheld

61% of community survey respondents play on a handheld PC at least sometimes ([[research/market/community-survey-01]] [emerging]).

## How It Shapes the Game

- **Fog.** The volumetric fog shader dropped to 38 fps in Gloamwick, so a baked fog layer that held 30+ everywhere replaced it ([[research/technical/handheld-perf-benchmark]] [emerging], [[world/regions/gloamwick]]).
- **Text.** Letters must be readable at handheld size, which led to readable body text and a font toggle ([[decisions/product/PDR-P011-readable-letters|PDR-P011]], [[research/accessibility/letter-readability-audit]] [emerging]).
- **Controls.** [[ideas/one-handed-mode]] grew out of handheld play.
