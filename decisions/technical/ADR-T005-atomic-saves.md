---
title: "ADR-T005: Saves Write to a Temp File, Then Rename"
doctype: ADR
id: ADR-T005
domain: technical
status: accepted
date: 2026-08-01
tags: [saves, reliability, handheld]
constitution-clause: null
supersedes: null
superseded-by: null
---
# ADR-T005: Saves Write to a Temp File, Then Rename

## Context
Handheld PCs sleep, run out of battery, and get switched off in the middle of a save. A corrupted save in Night Post erases letters opened, postmarks earned, and relationships built, and players will not replay those hours.

Tomas tested the risk directly. In 500 simulated power cuts during a save, direct writes corrupted 2 files and write-temp-then-rename corrupted none ([[research/technical/save-corruption-test]] [emerging]).

## Decision
Every save writes to a temporary file in the save folder, then renames it over the previous save. A power cut leaves either the old save or the new one, never a mix of both.

## Alternatives Considered
- **Direct writes.** They are the simplest option, and the test showed they corrupt saves.
- **Direct writes plus a backup copy.** A backup recovers most failures, but it can also be caught mid-write, and restoring it needs its own logic and menu.
- **Cloud saves as the safety net.** Clause P3 of [[architecture/CONSTITUTION]] keeps Night Post offline, so the local save must hold up on its own.

## Consequences
- Each save costs one extra file operation, which players will not notice at Night Post's save size.
- The temporary file must sit on the same drive as the save, or the rename stops being a single step.
- The zero-corruption result comes from one test [emerging], so the team should repeat it on the release build and on each supported handheld ([[concepts/handheld-floor]]).
