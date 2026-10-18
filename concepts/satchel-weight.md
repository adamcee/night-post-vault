---
title: Satchel Weight
id: satchel-weight
date: 2026-04-14
status: Active
tags: [concept, economy, inventory]
---
# Satchel Weight

Satchel weight is the trade-off between how much Wren carries and how fast Wren walks. A full satchel holds more letters, offers, and spare oil, but it slows Wren down and makes the night shorter in practice ([[architecture/game-design-overview]]).

## How It Works in Play

- **Letters weigh something.** Taking more letters at dusk means more deliveries and a slower walk.
- **Offers weigh something.** Items for [[concepts/parley]] offers take space Wren could use for letters.
- **Oil weighs something.** Spare [[concepts/lantern-oil]] extends the night but slows the walk.
- **Fast deliveries reward light packing.** The fast [[concepts/postmark]] favours a light satchel.

## Decisions Behind It

- **No crafting.** Gathering and crafting were rejected because they add inventory busywork that fights the delivery loop, so the satchel stays a simple choice of what to carry ([[ideas/crafting-system]]).
- **One-handed play.** Satchel management must work with few inputs, which matters for [[ideas/one-handed-mode]].
