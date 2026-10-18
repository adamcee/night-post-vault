---
title: Decision Records Schema
date: 2026-04-06
tags: [decisions, schema, index]
---
# Decision Records Schema

Frontmatter for every ADR and PDR, used by Obsidian Bases and by plain text search.

## Frontmatter

Copy this into every new decision record:

```yaml
---
doctype: ADR  # or PDR
id: ADR-T001  # PDR-P001 for product decisions
domain: technical  # or product
status: accepted  # proposed, accepted, superseded, rejected, deprecated
date: YYYY-MM-DD
tags: [kebab-case, topics]
constitution-clause: null  # e.g. S1 or P3, if the record touches a CONSTITUTION clause
supersedes: null  # "[[decisions/...]]"
superseded-by: null
---
```

Night Post records also carry a `title:` field equal to the H1, which the published site uses as the page name.

## Status Meanings

- **proposed**: drafted in chat, not yet approved. Records aren't written to disk in this state unless the owner asks.
- **accepted**: in force. A record amended with a dated note stays `accepted`.
- **superseded**: fully replaced by a newer record named in `superseded-by`.
- **rejected**: evaluated and declined; lives in `decisions/rejected/`.
- **deprecated**: no longer relevant, with nothing replacing it.

## Naming

`ADR-T001-short-title.md` and `PDR-P001-short-title.md`, numbered in the order they're written. Rejected records keep their number and move to `rejected/`.

## Tags

Keep a short, shared tag list so searches work. Add new tags here before using them.

**Reweave state**
- `reweave-strengthened`: later evidence supports the record.
- `reweave-weakened`: later evidence cuts against it, and the record carries a dated note.
- `reweave-invalidated`: evidence overturned it and a newer record superseded it.

**Game design**
- `core-fantasy`: what the player is and does, at the highest level.
- `quests`: how quests are built and handed out.
- `letters`: letters as quests, objects, and on-screen text.
- `choice`: player choices with lasting effects.
- `consequences`: what follows a choice, socially or mechanically.
- `encounters`: meetings with forest creatures and folk.
- `combat`: fighting systems, now removed from the design.
- `parley`: resolving encounters by talk, items, or lantern light.
- `no-death`: records that keep Wren alive (constitution clause P1).
- `moon-shift`: paths that rearrange by moon phase.
- `navigation`: finding the way through Hollowmere.
- `level-design`: how paths, waymarks, and routes are authored.
- `procedural-generation`: generated rather than hand-placed content.
- `multiplayer`: more than one player.
- `co-op`: two players working together.
- `networking`: online connections of any kind.
- `tone`: cozy-but-eerie mood and the solitary courier fantasy.

**World and scope**
- `world`: Hollowmere canon in `world/`.
- `regions`: which regions are in the game.
- `scope`: how much game three people can make by October 2027.
- `runway`: months of money left.
- `budget`: spending on vendors, recording, and contractors.

**Art, text, and interface**
- `art-direction`: the painted look of the game.
- `palette`: the limited night colors.
- `accessibility`: colorblind, contrast, and size needs.
- `typography`: fonts and text size.
- `ui`: screens and on-screen readers.

**Audio**
- `audio`: all sound work.
- `music`: the score and how it plays.
- `soundscape`: ambient field recordings.
- `voice`: spoken lines and barks.

**Technical**
- `engine`: the game engine choice.
- `godot`: Godot 4 specifics.
- `gdscript`: the scripting language.
- `tooling`: editors and in-house tools.
- `parser`: the in-house script parser.
- `dialogue`: dialogue files and their format.
- `writing-pipeline`: how text moves from the writer into the build.
- `version-control`: Git and Git LFS.
- `performance`: frame rate and memory targets.
- `handheld`: handheld PC hardware limits.
- `platform`: which devices the game ships on.
- `saves`: save files and their safety.
- `reliability`: guarding against crashes and data loss.

**Business**
- `business`: revenue and money decisions.
- `pricing`: the launch price.
- `launch`: launch plans and dates.
- `localization`: translating the game.
- `languages`: which languages ship.

## Search Recipes

- Accepted decisions: `grep -rl "status: accepted" decisions/`
- Everything rejected: `grep -rl "status: rejected" decisions/`
- Records touching a constitution clause: `grep -rl "constitution-clause: P3" decisions/`
- Records that replaced others: `grep -rL "supersedes: null" decisions/`
- Records later evidence weakened: `grep -rl "reweave-weakened" decisions/`
