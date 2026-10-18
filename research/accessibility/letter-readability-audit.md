---
title: "Letter Readability Audit"
date: 2026-08-21
evidence-maturity: emerging
tags: [accessibility, readability, letters, handheld, primary-research]
method: "Priya and Ines rendered sample letters at 800p on a 7-inch handheld screen, measured text contrast against the parchment and text size in pixels, and read each one on the device."
---
# Letter Readability Audit

At 800p on a 7-inch screen, the handwritten font's body text fails the 4.5:1 contrast target on parchment and renders below a comfortable size. One audit on one device makes this `[emerging]`, but it explains what players showed in [[research/playtests/pt-04-vertical-slice]].

## Method
- **Device.** The audit used a handheld PC with a 7-inch screen at 800p (1280 × 800 pixels).
- **Samples.** Priya rendered four versions of the same 110-word letter in game on 2026-08-20.
- **Contrast.** Priya measured the contrast ratio between ink color and parchment color from screenshots with a contrast-checker tool. The target is 4.5:1 for normal text and 3:1 for large text ([[research/accessibility/text-contrast-and-size-standards]] [established]).
- **Size.** Priya measured rendered body text height in pixels. The team set a working minimum of 20 pixels after reading test letters on the device; no standard in the vault sets a size number, so this target is the team's own.

## Findings
| Sample | Contrast on parchment | Text size at 800p | Result |
|---|---|---|---|
| Handwritten font, body text, standard ink | 3.1:1 | 15 px | Fails contrast and size |
| Handwritten font, body text, faded ink | 2.4:1 | 15 px | Fails contrast and size |
| Handwritten font, header and signature | 3.1:1 | 28 px | Passes as large text |
| Readable typeface, body text, dark ink | 8.2:1 | 20 px | Passes contrast and size |

- **Handwritten body text fails.** Standard ink reaches 3.1:1 and faded ink 2.4:1, both below 4.5:1, and the text renders at 15 pixels.
- **Handwritten headers can stay.** At 28 pixels, the header and signature pass the 3:1 large-text target. Treating 28-pixel text as large text is our interpretation; the standards doc does not set the threshold.
- **A readable typeface passes.** The candidate body typeface reaches 8.2:1 at 20 pixels.
- **The numbers match pt-04.** Four of ten players squinted at handwritten letters in [[research/playtests/pt-04-vertical-slice]], all on handhelds ([emerging]).

## Limits
- **One device.** Other handheld screens differ in brightness and pixel density.
- **Screenshot contrast.** Measuring from screenshots ignores screen glare and brightness settings.
- **Team size target.** The 20-pixel minimum comes from three people reading on one device.

## Reweave Triggers
- [[decisions/product/PDR-P006-handwritten-letters|PDR-P006]]: invalidated. Handwritten body text fails the contrast target and the size target at handheld size. Flagged for Ines with a proposed superseding record, [[decisions/product/PDR-P011-readable-letters|PDR-P011]]: handwritten headers and signatures, a readable body typeface, and a font toggle.
