---
title: Foldable Map
id: foldable-map
date: 2026-10-06
status: idea
tags: [navigation, ui, festival-feedback]
resolved-by: null
---
# Foldable Map

Give Wren a paper map that folds out of the satchel and fills in as Wren learns the forest. It would mark waymarks and their landmarks once visited, and let the player pencil in which paths connect under which moon.

## Why It Came Up

During the demo festival, 23 comments asked for a map ([[research/market/demo-festival-results]] [emerging]). The same results showed 41% of 3,140 demo players finished the demo.

## Open Questions

- **Mastery.** Learning the forest is the core mastery ([[concepts/moon-shift]], [[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]]). A map that shows paths for the player would remove it, so a map the player fills in by hand is the safer version.
- **Already better.** Waymark landmarks cut lost players from 6 of 10 to 2 of 12 ([[research/playtests/pt-05-demo-build]] [emerging]). The map may matter less than festival comments suggest.
- **Readability.** A map has to stay readable at handheld size ([[architecture/CONSTITUTION]] P2, [[concepts/handheld-floor]]).
- **Scope.** A new UI screen competes with region work in Production ([[prototype/implementation-plan]]).
