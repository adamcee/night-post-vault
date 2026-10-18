---
title: Architecture
date: 2026-10-08
tags: [architecture, index]
---
# Architecture

Architecture holds Night Post's invariants and its game design docs. Design docs describe the game that results from the records in `decisions/`.

- [[architecture/CONSTITUTION]]: product and stack invariants. Breaking one requires a decision record.
- [[architecture/game-design-overview]]: the core loop from dusk pickup to dawn return, and how the systems fit together.

## Systems

- [[architecture/systems/parley]]: how Wren gets past people and creatures by talk, offers, or lantern light.
- [[architecture/systems/moon-and-paths]]: which paths connect which waymarks under each moon phase.
- [[architecture/systems/postmarks]]: stamps earned by delivery style and the abilities they unlock.
- [[architecture/systems/lantern-oil-economy]]: oil as the night's clock and money, and how satchel weight drains it.

## Interface

- [[architecture/ui/letter-reader]]: the screen that shows every letter, with the font toggle from [[decisions/product/PDR-P011-readable-letters|PDR-P011]].
