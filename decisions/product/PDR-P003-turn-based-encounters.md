---
title: "PDR-P003: Turn-Based Encounters With Forest Creatures"
doctype: PDR
id: PDR-P003
domain: product
status: superseded
date: 2026-04-22
tags: [encounters, combat, reweave-weakened]
constitution-clause: null
supersedes: null
superseded-by: "[[decisions/product/PDR-P009-parley-encounters]]"
---
# PDR-P003: Turn-Based Encounters With Forest Creatures

> **Superseded 2026-06-24** by [[decisions/product/PDR-P009-parley-encounters|PDR-P009]] after the parley prototype replaced combat.
>
> **Reweave 2026-05-22:** weakened by [[research/playtests/pt-02-greybox-encounters]] [emerging]: turn-based encounters averaged 4 minutes, 5 of 6 players said they clashed with the tone, and 4 of 6 walked around creatures to avoid them. Flagged for human review.
>
> **Reweave 2026-04-24:** early doubt from [[research/playtests/pt-01-paper-prototype]] [emerging]: 3 of 5 players said the paper "combat" felt like a different game.

## Context
Hollowmere's creatures block paths at night, and the team wanted the courier to face them. Turn-based fights need no fast reflexes, suit handheld play, and give satchel items a use.

## Decision
Encounters with forest creatures are turn-based. Wren has HP (hit points) and uses satchel items and her lantern as actions, and the night ends in failure if her HP reaches zero.

## Alternatives Considered
- **Real-time combat.** It needs animation and tuning work that three people cannot afford, and it clashes with a slow walking game.
- **No encounters.** The walks would lack tension, and the forest would stop feeling dangerous.
- **Stealth.** Sneaking past creatures suits a courier, but it needs patrol and detection systems.

## Consequences
- Tomas builds a combat system with turn order, HP, and item effects.
- Satchel items gain combat stats, which ties [[concepts/satchel-weight]] to fighting.
- A lost fight ends the night, which raises the stakes and can cost the player a night of deliveries.
