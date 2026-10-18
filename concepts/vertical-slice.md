---
title: Vertical Slice
id: vertical-slice
date: 2026-07-01
status: Active
tags: [concept, production, milestone]
---
# Vertical Slice

A vertical slice is a short section of the game, built to near-final quality, that shows every core system working together. Night Post's slice was built in July and August and finished on 2026-08-28 ([[prototype/specs/vertical-slice]]).

## How Night Post Used It

- **Test the full loop.** The slice ran the whole night from dusk pickup to dawn postmarks ([[architecture/game-design-overview]]).
- **Playtest it.** Ten players played a 90-minute slice, with a median of 71 minutes to finish ([[research/playtests/pt-04-vertical-slice]] [emerging]).
- **Find what breaks.** 6 of 10 got lost after the first moon-shift and 4 of 10 on handhelds squinted at handwritten letters. Those findings weakened [[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]] and led to [[decisions/product/PDR-P011-readable-letters|PDR-P011]].

## Where It Sits in Production

The slice came after the greybox prototype and before the festival demo ([[prototype/specs/festival-demo]], [[prototype/implementation-plan]]).
