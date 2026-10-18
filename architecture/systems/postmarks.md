---
id: postmarks
title: Postmarks System
date: 2026-05-27
status: Active
tags: [architecture, systems, progression, postmarks]
---
# Postmarks System
*Updated 2026-08-28 for the festival demo.*

Postmarks are Night Post's progression system: Odile stamps each delivery by how Wren made it, and stamps of one kind unlock abilities of that kind. The game rewards a style of play rather than raw experience points.

The term is defined in [[concepts/postmark]]. The system grew from [[ideas/postmark-badges]], which was absorbed into that concept.

## Four Kinds of Postmark
| Postmark | Earned by | Example |
|---|---|---|
| **Fast** | Delivering with time to spare before dawn. | Arriving with more than half a lantern of oil left. |
| **Careful** | Delivering with the letter unopened and undamaged. | Crossing the river at Sallow Ferry in the rain without wetting the satchel. |
| **Kind** | Delivering in a way that helps someone beyond the letter. | Ending a parley with an offer instead of a toll ([[architecture/systems/parley]]). |
| **Nosy** | Opening a sealed letter before delivering it. | Reading a smuggler's letter, then delivering it resealed ([[concepts/sealed-letter]]). |

One delivery can earn more than one postmark, except that careful and nosy exclude each other.

## Abilities Unlock in Three Tiers per Kind
Every five postmarks of one kind unlock the next tier of that kind, for 12 abilities in all.

| Kind | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| **Fast** | Walk faster with a light satchel. | Shortcut prompts at familiar waymarks. | Ledger scouts two waymarks a night instead of one. |
| **Careful** | One extra satchel slot. | Rain no longer smudges letters. | Lantern burns oil 10% slower. |
| **Kind** | A third talk line in some parleys. | Recipients sometimes pay in oil. | Some creatures let Wren pass with no verb at all. |
| **Nosy** | Read the sender's name without opening. | Reseal a letter so most recipients cannot tell. | Ledger hints at what a letter says before Wren opens it. |

## Design Rules for Postmarks
- **No wrong style:** every kind unlocks useful abilities, so a nosy courier and a careful one both progress.
- **No punishment:** opening letters earns nosy postmarks and social consequences, never a lost ability ([[decisions/product/PDR-P008-sealed-letters-can-be-opened|PDR-P008]]).
- **Visible record:** the stamp card in the office shows every postmark earned, so the player can see the courier they are becoming.
- **Kept small:** 12 abilities fit three people and an October 2027 launch (clause P4 of [[architecture/CONSTITUTION]]).

## Evidence So Far
- The letter-opening choice was the most discussed moment in the paper prototype, 5 of 5 players ([[research/playtests/pt-01-paper-prototype]] [emerging]). Nosy postmarks reward that choice instead of hiding it.
- The vertical slice included fast and kind postmarks only ([[prototype/specs/vertical-slice]]). The festival demo added all four ([[prototype/specs/festival-demo]]).
