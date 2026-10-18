---
title: "Night Palette Colorblind Test"
date: 2026-07-24
evidence-maturity: emerging
tags: [accessibility, color, art, palette, primary-research]
method: "Priya ran 12 game screenshots through deuteranopia and protanopia simulation filters and compared key pairs of colors side by side."
---
# Night Palette Colorblind Test

Under both deuteranopia and protanopia simulation, the red and green route lanterns look the same. Every other color pair Priya checked stayed distinct; a simulation filter is not a test with players, so the finding is `[emerging]`.

## Method
- **Terms.** Deuteranopia and protanopia are two forms of red-green color blindness. A simulation filter shifts an image's colors to approximate what a person with each condition sees.
- **Images.** Priya took 12 screenshots on 2026-07-22 and 2026-07-23 from the vertical slice in progress, covering Thimble Cross and the road to Gloamwick at three moon phases.
- **Check.** She ran each screenshot through both filters in her image editor and compared five color pairs that players must tell apart.

## Findings
| Color pair | Unfiltered | Deuteranopia | Protanopia |
|---|---|---|---|
| Red route lantern vs. green route lantern | Distinct | Indistinguishable | Indistinguishable |
| Amber waymark lantern vs. glow-moss | Distinct | Distinct | Distinct |
| Parchment letter vs. night ground | Distinct | Distinct | Distinct |
| Hushfolk pale-blue glow vs. lantern light | Distinct | Distinct | Distinct |
| Lantern oil gauge, full vs. low | Distinct | Distinct | Distinct |

- **Route lanterns fail.** The red and green route lanterns, which mark the two path choices at a fork, became the same muddy brown under both filters in all 12 screenshots.
- **The rest of the palette holds.** The other four pairs stayed distinct under both filters.

## Limits
- **Simulation, not people.** No player with color blindness has tested the palette yet.
- **Two conditions.** The test did not cover other forms of color blindness.
- **Screenshots only.** Moving lights and fog may look different in play.

## Reweave Triggers
- [[decisions/product/PDR-P005-painted-night-palette|PDR-P005]]: weakened. Red and green route lanterns were indistinguishable under both filters; they need distinct shapes, not only distinct colors. Flagged for Priya.
