---
title: "PDR-P009: Encounters Are Resolved by Parley"
doctype: PDR
id: PDR-P009
domain: product
status: accepted
date: 2026-06-24
tags: [encounters, parley, no-death, reweave-strengthened]
constitution-clause: P1
supersedes: "[[decisions/product/PDR-P003-turn-based-encounters]]"
superseded-by: null
---
# PDR-P009: Encounters Are Resolved by Parley

## Context
Forest creatures still block paths at night, and the walks still need tension. Turn-based fights did not do that job in testing, so the team prototyped a conversation-based alternative ([[ideas/talk-instead-of-fight]]).

## What Changed
[[decisions/product/PDR-P003-turn-based-encounters|PDR-P003]] was weakened on 2026-05-22. Turn-based encounters averaged 4 minutes, 5 of 6 players said they clashed with the tone, and 4 of 6 walked around creatures ([[research/playtests/pt-02-greybox-encounters]] [emerging]).

The parley prototype then won 7 of 8 players over the earlier encounters. The tone finding repeated pt-02, so the result is tagged supported ([[research/playtests/pt-03-parley-prototype]] [supported]).

## Decision
Encounters are resolved by parley: Wren talks, offers an item from her satchel, or shines her lantern ([[concepts/parley]]). Wren has no HP (hit points) and cannot die, and a failed parley costs lantern oil, time, or a detour, never the night ([[architecture/systems/parley]]).

## Alternatives Considered
- **Shorter turn-based fights.** Short fights still clash with the tone, and players still walk around them.
- **No encounters.** The walks would lose tension, and creatures would become scenery.
- **Stealth.** Players already avoided creatures, but stealth treats the forest's inhabitants as obstacles instead of characters.

## Consequences
- The combat system, HP, and item damage stats are cut. Satchel items become parley offers, and lantern oil gains a second use ([[concepts/lantern-oil]]).
- Encounters now need writing instead of balancing, which moves work from Tomas to Ines.
- The decision adds clause P1 to [[architecture/CONSTITUTION]].
- **Reweave 2026-10-06:** strengthened by [[research/market/demo-festival-results]] [emerging]: 41% of 3,140 demo players finished the demo, and comments praised the letters and tone.
