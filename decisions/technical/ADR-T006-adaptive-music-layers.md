---
title: "ADR-T006: Music Plays in Layers That Thin Out on Long Walks"
doctype: ADR
id: ADR-T006
domain: technical
status: accepted
date: 2026-08-10
tags: [audio, music, soundscape]
constitution-clause: null
supersedes: null
superseded-by: null
---
# ADR-T006: Music Plays in Layers That Thin Out on Long Walks

## Context
Night Post has long walks between villages, and continuous music wears listeners out. On a 30-minute route, 7 of 9 listeners found continuous music tiring after about 20 minutes, and all 9 liked the music returning at arrivals ([[research/audio/music-listening-test]] [emerging]).

Tomas also has 41 usable field-recording takes from two nights at a wetland reserve, including frogs, wind in reeds, and distant owls ([[research/audio/field-recording-trip]] [emerging]). Those takes can carry a walk without music.

## Decision
Each region's music is written in layers. On a long walk the layers drop out one at a time until only the soundscape remains, and the full piece returns when Wren reaches a village or delivers a letter.

## Alternatives Considered
- **Continuous looping tracks.** They are the simplest to compose, but the listening test showed fatigue at about 20 minutes.
- **Silence between places, with short arrival cues.** Silence removes fatigue, but the walks lose the eerie mood the tone needs.
- **Generative music.** It never repeats, but building it would take Tomas's programming time away from game systems.

## Consequences
- Tomas composes each piece as stems (separate instrument tracks) that must sound complete at any layer count, which takes longer per track.
- The game needs a walk timer and crossfades between layers, which Tomas builds together with the soundscape player.
- Arrivals carry more weight, so each delivery in the core loop gets a musical return ([[architecture/game-design-overview]]).
- Both audio findings come from small groups [emerging], so the layer timing stays easy to tune.
