---
title: "ADR-T001: Godot 4 With GDScript"
doctype: ADR
id: ADR-T001
domain: technical
status: accepted
date: 2026-04-08
tags: [engine, godot, gdscript, tooling]
constitution-clause: S1
supersedes: null
superseded-by: null
---
# ADR-T001: Godot 4 With GDScript

## Context
Night Post needs an engine that three people can ship on PC and handheld PCs by October 2027. Tomas is the only programmer and also composes the music, so every hour spent fighting the engine comes out of composing time.

The game is 2D, with painted backgrounds, lantern lighting, and a lot of text. It has no physics puzzles, no networking, and no 3D characters.

## Decision
Build Night Post in Godot 4 and write all game code in GDScript, Godot's built-in scripting language. Export targets are Windows and Linux.

## Alternatives Considered
- **A commercial engine with C#.** It has a larger plugin store, but its fees and license terms sit outside the team's control. Its editor also runs slowly on Tomas's laptop.
- **Godot with C#.** C# runs heavy logic faster, but it adds a .NET runtime to every export and complicates Linux builds. Night Post's game logic is light.
- **A custom engine.** Tomas could fit it to the game exactly, but building it would take months that the writing and art need.

## Consequences
- The engine is free and open source, with no royalties or per-install fees.
- Godot's 2D renderer, tilemaps, and animation tools cover the game without third-party plugins.
- GDScript runs slower than C#, so expensive work such as path layouts for each moon phase lives in precomputed data, not runtime code.
- Any contractor must work in GDScript, and no C# or native-code modules enter the project.
- The decision adds clause S1 to [[architecture/CONSTITUTION]].
