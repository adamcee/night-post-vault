---
title: "Handheld Performance Benchmark"
date: 2026-06-05
evidence-maturity: emerging
tags: [technical, performance, handheld, rendering, primary-research]
method: "Tomas ran a scripted 10-minute camera walk through three greybox areas on a handheld PC at 800p, three runs per area, with volumetric fog and then with baked fog."
---
# Handheld Performance Benchmark

The greybox averaged 52 frames per second (fps) on a handheld PC, but the volumetric fog shader pulled Gloamwick down to 38 fps with dips below 30. A baked fog layer held 30 fps or more everywhere; one device and a greybox build make this `[emerging]`.

## Method
- **Device.** Tomas used a handheld PC at 800p, the minimum target in [[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]], on battery with default power settings.
- **Build.** He tested the greybox build of 2026-06-02 with the frame rate capped at 60 fps.
- **Runs.** Tomas ran a scripted 10-minute camera walk through Thimble Cross, Gloamwick, and Sallow Ferry three times each, on 2026-06-03 and 2026-06-04. He logged frame times with the engine's built-in performance monitor.
- **Fog modes.** He ran every area with the volumetric fog shader, then with a baked fog layer (fog painted into a fixed texture instead of computed each frame).

## Findings
| Area | Volumetric fog average | Volumetric fog minimum | Baked fog average | Baked fog minimum |
|---|---|---|---|---|
| Thimble Cross | 60 fps | 48 fps | 60 fps | 50 fps |
| Gloamwick | 38 fps | 24 fps | 51 fps | 33 fps |
| Sallow Ferry | 58 fps | 44 fps | 59 fps | 47 fps |
| All three areas | 52 fps | 24 fps | 57 fps | 33 fps |

- **Average performance clears the floor.** With volumetric fog, the greybox averaged 52 fps across the three areas.
- **Gloamwick's fog breaks it.** Gloamwick's dense marsh fog averaged 38 fps and dipped to 24 fps during camera pans over glow-moss.
- **Baked fog holds.** With baked fog, every area stayed at 30 fps or above, with a lowest reading of 33 fps in Gloamwick.

## Limits
- **Greybox load.** Final art, characters, and particle effects will cost more frames than grey blocks.
- **One device.** Other handheld PCs may run hotter or slower.
- **Short runs.** Ten-minute runs do not show slowdown from heat over a long session.

## Reweave Triggers
- [[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]]: strengthened, with a fog change. The handheld floor of 30 fps at 800p holds if Gloamwick uses baked fog instead of the volumetric shader.
