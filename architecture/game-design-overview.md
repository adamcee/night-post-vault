---
id: game-design-overview
title: Game Design Overview
date: 2026-04-07
status: Active
tags: [architecture, game-design, core-loop]
---
# Game Design Overview
*Updated 2026-09-08 for three regions.*

Night Post is a narrative adventure RPG (role-playing game) in which every quest is a letter to carry through a forest at night ([[decisions/product/PDR-P001-letters-are-the-quests|PDR-P001]]). The player wins knowledge, trust, and new abilities, and never loses the game.

## The Player Is Wren, the Newest Courier
- **Wren** ([[world/characters/wren]]) works for [[world/factions/the-night-post]] out of the Sorting House, the Night Post office in [[world/regions/thimble-cross]], run by [[world/characters/odile-marr]].
- **Ledger** ([[world/characters/ledger]]), a retired postal crow, scouts ahead and comments on what Wren does.
- **Hollowmere** ([[world/hollowmere]]) is the forest between the villages. Its paths rearrange with the phase of the moon.

## The Core Loop Is One Night
1. **Pick up letters at dusk.** Odile hands Wren the night's letters at the Sorting House counter. Each letter names a sender, a recipient, and a place.
2. **Plan a route by moon phase.** The phase decides which paths connect which [[concepts/waymark|waymarks]] tonight ([[architecture/systems/moon-and-paths]]).
3. **Deliver, parley, and choose whether to open.** Wren walks the route, meets people and creatures on the path, and resolves each meeting by [[concepts/parley]] ([[architecture/systems/parley]]). At any point she can open a [[concepts/sealed-letter]] and read it in the [[architecture/ui/letter-reader]].
4. **Return by dawn.** [[concepts/lantern-oil]] burns as she walks, so the oil left in the lantern is the night's clock ([[architecture/systems/lantern-oil-economy]]).
5. **Earn postmarks.** Odile stamps each delivery by how Wren made it: fast, careful, kind, or nosy. [[concepts/postmark|Postmarks]] unlock abilities ([[architecture/systems/postmarks]]).

## Nothing Ends the Game Early
- Encounters have no health and no death ([[decisions/product/PDR-P009-parley-encounters|PDR-P009]], clause P1 of [[architecture/CONSTITUTION]]).
- Opening a letter changes what people say and do, and never causes a game over ([[decisions/product/PDR-P008-sealed-letters-can-be-opened|PDR-P008]]).
- If the oil runs out before Wren is home, dawn breaks and Ledger leads her back, and the undelivered letters wait for the next night. The cost is a late delivery and fewer postmarks.

## Letters Carry the Story
- **Stories:** each delivery reveals a relationship, a secret, or a debt between villages. The game has no villain, only unpaid debts and old grudges.
- **Length:** letters keep to a 120-word soft limit, the [[concepts/letter-budget]], because letters under 120 words were read in full 88% of the time ([[research/narrative/letter-length-test]] [emerging]).
- **Script size:** about 86,000 words for three regions, of which letters are 58% ([[research/narrative/script-word-count]] [emerging]).
- **Format:** dialogue and letters live in plain-text files the writer edits directly ([[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]]).

## Three Regions, Played in Order
| Region | Role in the game | Main faction or figure |
|---|---|---|
| [[world/regions/thimble-cross]] | Tutorial region around the Night Post office. | Odile Marr and the Night Post |
| [[world/regions/gloamwick]] | Marsh town lit by glow-moss; oil and lantern stories. | [[world/factions/lamplighters-union]] and [[world/characters/the-quiet-lamplighter]] |
| [[world/regions/sallow-ferry]] | River crossing; smugglers' letters. | [[world/characters/bram-ashby]] and the Ashby family |

[[decisions/product/PDR-P012-three-regions|PDR-P012]] cut two regions, [[world/regions/cut/the-drowned-bell]] and [[world/regions/cut/the-high-briar]]. The Drowned Bell's best story moved to Sallow Ferry, and the High Briar became Gloamwick's edges.

The [[world/factions/the-hushfolk]] appear in every region. Their envoy, [[world/characters/mothwife-sel]], trades in secrets, and the Hushfolk never lie.

## Tone Is Cozy but Eerie
- **Cozy:** small human stories, warm lantern light, and a crow who complains.
- **Eerie:** a forest that moves when you are not looking, and moth-like folk who already know what is in your satchel.
- **Look:** painted 2D art in a limited night palette ([[decisions/product/PDR-P005-painted-night-palette|PDR-P005]]).
- **Sound:** music in layers that thin out on long walks and return at arrivals ([[decisions/technical/ADR-T006-adaptive-music-layers|ADR-T006]]).

## Length and Platform
- **Length:** 8 to 10 hours.
- **Platform:** PC, with a handheld PC as the minimum target at 30 frames per second and 800p ([[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]], [[concepts/handheld-floor]]).
- **Engine:** Godot 4 with GDScript ([[decisions/technical/ADR-T001-godot-4-engine|ADR-T001]]).
