---
title: Decisions
date: 2026-10-08
tags: [decisions, index]
---
# Decisions

Night Post's choices live here as Architecture Decision Records (ADRs) and Product Decision Records (PDRs). Each records context, the decision, alternatives considered, and consequences.

New records are drafted in chat and written only after Ines approves ([[vault-guide/decision-propagation-protocol]]). Frontmatter, status meanings, tags, and search recipes are in [[decisions/_BASES_SCHEMA]].

## Technical (ADRs)

- [[decisions/technical/ADR-T001-godot-4-engine|ADR-T001]]: Godot 4 with GDScript.
- [[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]]: a handheld PC at 30 fps and 800p is the minimum target.
- [[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]]: dialogue and letters live in plain-text script files.
- [[decisions/technical/ADR-T005-atomic-saves|ADR-T005]]: saves write to a temp file, then rename.
- [[decisions/technical/ADR-T006-adaptive-music-layers|ADR-T006]]: music thins out on long walks and returns at arrivals.

## Product (PDRs)

- [[decisions/product/PDR-P001-letters-are-the-quests|PDR-P001]]: every quest is a letter.
- [[decisions/product/PDR-P002-five-regions|PDR-P002]]: five regions. Superseded by PDR-P012.
- [[decisions/product/PDR-P003-turn-based-encounters|PDR-P003]]: turn-based encounters. Superseded by PDR-P009.
- [[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]]: paths rearrange by moon phase. Weakened 2026-08-18, still accepted.
- [[decisions/product/PDR-P005-painted-night-palette|PDR-P005]]: painted 2D in a limited night palette. Weakened 2026-07-27, still accepted.
- [[decisions/product/PDR-P006-handwritten-letters|PDR-P006]]: handwritten letter fonts. Superseded by PDR-P011.
- [[decisions/product/PDR-P008-sealed-letters-can-be-opened|PDR-P008]]: players may open sealed letters.
- [[decisions/product/PDR-P009-parley-encounters|PDR-P009]]: encounters are resolved by parley, with no death.
- [[decisions/product/PDR-P010-price-18-dollars|PDR-P010]]: the launch price is $18.
- [[decisions/product/PDR-P011-readable-letters|PDR-P011]]: a readable body typeface and a font toggle.
- [[decisions/product/PDR-P012-three-regions|PDR-P012]]: three regions; the Drowned Bell and the High Briar are cut.
- [[decisions/product/PDR-P014-launch-languages|PDR-P014]]: launch in English, Spanish, and German.

## Rejected

- [[decisions/rejected/ADR-T004-procedural-forest|ADR-T004]]: procedural forest generation.
- [[decisions/rejected/PDR-P007-co-op-courier-mode|PDR-P007]]: online two-player co-op.
- [[decisions/rejected/PDR-P013-full-voice-acting|PDR-P013]]: full voice acting, replaced by voiced barks.
