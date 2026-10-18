---
title: Gloamwick
date: 2026-04-10
status: canon
tags: [world, region, lamplighters, marsh]
---
# Gloamwick

Gloamwick is a marsh town lit by glow-moss and the home of the Lamplighters' Union, and it is where the oil dispute between the Union and the Night Post plays out. Since the three-region cut, its northern edge also holds what survived of the High Briar.

> "The moss knows when you're lying. So does your mother."
> — Gloamwick saying

## What the Player Does Here

- **Crosses the causeways.** Gloamwick sits on raised plank causeways over the marsh, and mire-geese guard several of them. Wren gets past by [[concepts/parley]].
- **Deals with the Union.** Wren buys or begs [[concepts/lantern-oil]] at the Wick House, the Union hall, and carries letters between the Union and the Post.
- **Walks the Briar Edge.** The thorn paths on the town's northern edge hold the briar hound and a handful of side letters from the cut High Briar.

## Places

- **The Wick House.** The Lamplighters' Union hall, built around the vats where tallow-reed is rendered into oil. The Quiet Lamplighter keeps a desk in the loft ([[world/characters/the-quiet-lamplighter]]).
- **The Moss Rows.** Streets lined with glow-moss beds, tended by gatherers like Lissa, who receives the Button Letter from Thimble Cross.
- **The Briar Edge.** A strip of thorn hedge and upland path north of the town, folded in from [[world/regions/cut/the-high-briar]].

## Letters and Relationships

- **The Oil Bill.** If Wren delivers the Post's sixty-first unpaid bill, the Union answers with a reply Odile won't want to read ([[world/characters/odile-marr]]).
- **The Quiet Lamplighter's letters.** The elder doesn't speak, so every conversation with the elder is a letter. These are the only letters in the game addressed to Wren.
- **June Tolley's letters.** June, a lamplighter and Maud Tolley's granddaughter, writes to Bram Ashby at [[world/regions/sallow-ferry]]. Her letters carry the Tolley story between the two regions.
- **Briar shepherd letters.** Short letters from shepherds who left the uplands, kept from the High Briar's script.

## Connections

- **West to Thimble Cross** by the marsh road ([[world/regions/thimble-cross]]).
- **South-west to Sallow Ferry** by the reed path, where smuggled oil travels the other way ([[world/regions/sallow-ferry]]).
- **Factions present.** The Union runs the town ([[world/factions/lamplighters-union]]). The Hushfolk avoid the brightest streets because glow-moss dims near lies and they find the attention tiresome ([[world/factions/the-hushfolk]]).

## Design Notes

- **Baked fog replaced volumetric fog.** On a handheld PC the greybox averaged 52 fps, but the volumetric fog shader dropped to 38 fps in Gloamwick, leaving little headroom above the 30 fps floor before final art; a baked fog layer held 30+ everywhere ([[research/technical/handheld-perf-benchmark]] [emerging]). Gloamwick now uses the baked layer, in line with [[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]] and [[concepts/handheld-floor]].
- **High Briar folded in.** The three-region cut moved the High Briar's best material to the Briar Edge rather than dropping it ([[decisions/product/PDR-P012-three-regions|PDR-P012]]).
- **Marsh soundscape.** Gloamwick's ambience draws on Tomas's wetland recordings of frogs, wind in reeds, and distant owls ([[research/audio/field-recording-trip]] [emerging]). The music thins out on long causeway walks and returns on arrival ([[decisions/technical/ADR-T006-adaptive-music-layers|ADR-T006]]).
- **Route lanterns differ by shape.** Red and green route lanterns are common here, and they now differ in shape as well as colour after the colourblind test ([[decisions/product/PDR-P005-painted-night-palette|PDR-P005]], [[research/accessibility/night-palette-colorblind-test]] [emerging]).
