---
id: lantern-oil-economy
title: Lantern Oil Economy
date: 2026-04-14
status: Active
tags: [architecture, systems, economy, lantern-oil, satchel-weight]
---
# Lantern Oil Economy
*Updated 2026-09-25 after the demo build playtest.*

Lantern oil is both the night's clock and its money: Wren burns it to walk and to shine, and she spends it to pay tolls and fares. Satchel weight sets how fast she burns it, so every item she carries trades against time.

Terms: [[concepts/lantern-oil]] and [[concepts/satchel-weight]].

## The Lantern Is the Clock
- **A full lantern holds 10 measures.** Wren starts each night with a full lantern from the Night Post office.
- **Walking costs 1 measure per path between waymarks**, or more with a heavy satchel.
- **Shining in a parley costs 2 measures** ([[architecture/systems/parley]]).
- **Dawn comes when the oil runs out.** The lantern's level on screen is the time left in the night, so every measure spent as money is also time spent.
- **Oil left on return** counts toward fast postmarks ([[architecture/systems/postmarks]]).

## Running Out Never Ends the Game
- When the oil runs out, dawn breaks and Ledger leads Wren home. Undelivered letters wait for the next night.
- The cost is a late delivery and fewer postmarks, never a lost save or a game over.
- This follows clause P1 of [[architecture/CONSTITUTION]]: nothing in the oil system creates a fail state.

## Oil as Money
| Source or sink | Amount | Where |
|---|---|---|
| Buy from the Lamplighters' Union at the Wick House | Up to 4 measures a night; the price in favors, such as carrying Union letters, depends on Wren's standing with the Union | [[world/regions/gloamwick]] |
| Ferry fare | 0 to 3 measures, depending on what Wren knows about Bram | [[world/regions/sallow-ferry]], paid to [[world/characters/bram-ashby]] |
| Parley toll | 1 to 3 measures | Any path |
| Recipient tip | 0 to 2 measures | Some deliveries; more with the tier 2 kind postmark |

The [[world/factions/lamplighters-union]] controls the oil supply and keeps the waymark lanterns lit. Their quarrel with [[world/factions/the-night-post]] over an oil bill unpaid for sixty-one years runs through the Gloamwick letters.

## Satchel Weight Trades Capacity Against Speed
| Load | Slots used | Oil per path |
|---|---|---|
| Light | 0–3 | 1 measure |
| Normal | 4–6 | 1 measure, walk 15% slower |
| Heavy | 7–8 | 2 measures |

- Letters weigh little, while parcels and parley items weigh more.
- A spare oil flask holds 3 measures and takes one slot, so extra night costs speed.
- Taking more letters in one night saves trips but costs oil. Choosing which letters to carry is part of route planning ([[architecture/systems/moon-and-paths]]).
- The careful postmark's extra slot raises the cap to 9.

## Tuning Status
These numbers held in the festival demo, where the median session was 38 minutes ([[research/playtests/pt-05-demo-build]] [emerging]). No playtest has measured oil use on its own, so the values are a design starting point for Production [unsourced].
