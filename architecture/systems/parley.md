---
id: parley
title: Parley System
date: 2026-06-24
status: Active
tags: [architecture, systems, parley, encounters]
---
# Parley System
*Updated 2026-08-31 with the open Ledger idea.*

Every encounter in Night Post is a parley: Wren gets past a person or creature by talking, offering something from her satchel, or shining her lantern ([[decisions/product/PDR-P009-parley-encounters|PDR-P009]]). There is no health, no damage, and no death, as clause P1 of [[architecture/CONSTITUTION]] requires.

The term itself is defined in [[concepts/parley]].

## Why Parley Replaced Combat
- **Turn-based encounters clashed with the tone.** They averaged 4 minutes, 5 of 6 players said they clashed with the tone, and 4 of 6 walked around creatures to avoid them ([[research/playtests/pt-02-greybox-encounters]] [emerging]).
- **Players preferred parley.** 7 of 8 players preferred the parley prototype to the earlier encounters ([[research/playtests/pt-03-parley-prototype]] [supported]).
- **History:** the idea started as [[ideas/talk-instead-of-fight]], and PDR-P009 superseded [[decisions/product/PDR-P003-turn-based-encounters|PDR-P003]].

## Three Verbs
| Verb | What Wren does | What it costs |
|---|---|---|
| **Talk** | Picks one of two or three lines. Lines change with what Wren has read and whom she has helped. | Time only. |
| **Offer** | Gives an item from the satchel, such as bread, a button, or a spare letter. | The item, which lightens the satchel ([[concepts/satchel-weight]]). |
| **Shine** | Raises the lantern to reveal, calm, or scare. | [[concepts/lantern-oil]] ([[architecture/systems/lantern-oil-economy]]). |

## Every Parley Ends in Passage
A parley always ends with Wren able to continue. What changes is the price and what she learns.
- **Clean pass:** the right verb opens the path at no extra cost and can earn a kind postmark ([[architecture/systems/postmarks]]).
- **Detour:** the path stays closed tonight, and Wren takes a longer route that burns more oil.
- **Toll:** the other side takes an item or oil and lets her through.
- **Secret:** some characters, the [[world/factions/the-hushfolk]] above all, let her pass in exchange for something she read in a sealed letter ([[concepts/sealed-letter]]).

## What Reading Letters Unlocks
- Opening a letter can add a talk line, because Wren now knows something private ([[decisions/product/PDR-P008-sealed-letters-can-be-opened|PDR-P008]]).
- Using that line is a social act with a social cost. The person may trust Wren less, and later letters can mention it.
- Hushfolk never lie, so what they say in a parley is always true, though it may be incomplete ([[world/factions/the-hushfolk]]).

## Encounter Budget
- **Length:** a parley takes under one minute, against the 4-minute turn-based encounters in [[research/playtests/pt-02-greybox-encounters]].
- **Density:** a night's route has two to four parleys, so walking and reading stay the main activities.
- **Writing:** parley lines live in the plain-text script files with the letters ([[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]]).

## Open Questions
- No playtest has tried a fourth verb. If the open idea [[ideas/ledger-upgrades]] is promoted, a Ledger action in parley is the first candidate to test.
