---
title: "Save Corruption Test"
date: 2026-07-31
evidence-maturity: emerging
tags: [technical, saves, reliability, primary-research]
method: "Tomas scripted 500 simulated power cuts during saving for each of two save methods and checked every save file afterward."
---
# Save Corruption Test

In 500 simulated power cuts during a save, writing directly to the save file corrupted 2 files, while writing to a temp file and then renaming it corrupted none. One test rig on one device makes this `[emerging]`.

## Method
- **Rig.** Tomas wrote a script that starts a save and kills the game process at a random moment during the write, which simulates a power cut. The script then restarts the game and loads the save.
- **Methods.** Method A writes over the save file directly. Method B writes to a temp file, then renames it over the old save in one step.
- **Runs.** Tomas ran 500 cuts for each method on a handheld PC from 2026-07-29 to 2026-07-30.
- **Check.** A save counts as corrupted if it fails its checksum or the game cannot load it.

## Findings
| Save method | Cuts | Corrupted saves | Result after a cut |
|---|---|---|---|
| A: direct write | 500 | 2 | Two saves would not load; the player would lose all progress. |
| B: write to temp file, then rename | 500 | 0 | Every save loaded, either the new one or the one before it. |

- **Direct writes can destroy a save.** Two of 500 cuts left a save the game could not load.
- **Temp-then-rename protects it.** No cut corrupted a save under method B. A cut before the rename left the previous save intact, so the player loses at most one save's progress.

## Limits
- **Killed process, not lost power.** Killing the process does not reproduce a real power loss, where the disk may not finish writing what the system has cached.
- **One device.** The test ran on one handheld PC with one storage type.
- **Rare failures.** A failure rate below 1 in 500 would not show up in this test.

## Reweave Triggers
- [[decisions/technical/ADR-T005-atomic-saves|ADR-T005]]: led to this record, written on 2026-08-01. Saves write to a temp file and then rename it.
