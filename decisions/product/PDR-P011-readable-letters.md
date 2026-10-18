---
title: "PDR-P011: Letters Use a Readable Body Typeface"
doctype: PDR
id: PDR-P011
domain: product
status: accepted
date: 2026-08-26
tags: [letters, typography, accessibility, ui, reweave-strengthened]
constitution-clause: P2
supersedes: "[[decisions/product/PDR-P006-handwritten-letters]]"
superseded-by: null
---
# PDR-P011: Letters Use a Readable Body Typeface

## Context
Letters carry most of Night Post's story, and the handheld floor puts them on a 7-inch screen ([[concepts/handheld-floor]]). [[decisions/product/PDR-P006-handwritten-letters|PDR-P006]] set every letter in a handwritten font, and that choice failed at handheld size.

## What Changed
On 2026-08-14, 4 of 10 vertical-slice players on handhelds squinted at the handwritten letters ([[research/playtests/pt-04-vertical-slice]] [emerging]). The readability audit followed on 2026-08-21.

At 800p on a 7-inch screen, the handwritten body text failed the 4.5:1 contrast target on parchment and was below a comfortable size ([[research/accessibility/letter-readability-audit]] [emerging]). WCAG 2.2 (Web Content Accessibility Guidelines) success criterion 1.4.3 sets at least 4.5:1 contrast for normal text ([[research/accessibility/text-contrast-and-size-standards]] [established]).

## Decision
Handwritten styles appear only in letter headers and signatures. Body text uses a readable typeface that meets 4.5:1 contrast on parchment at 800p, and a font toggle in the letter reader lets players change the body typeface ([[architecture/ui/letter-reader]]).

## Alternatives Considered
- **Keep handwriting and darken the parchment.** Contrast could pass, but the audit also found the text too small, and handwritten letterforms stay hard to read at small sizes.
- **Larger handwritten fonts.** Fewer words fit on screen, so most letters would need scrolling.
- **One plain typeface for everything.** It reads well, but senders lose their identity.

## Consequences
- Sender identity moves to headers, signatures, paper, and seals.
- Every letter must pass the contrast and size check before it ships.
- The decision adds clause P2 to [[architecture/CONSTITUTION]].
- **Reweave 2026-09-25:** strengthened by [[research/playtests/pt-05-demo-build]] [emerging]: 5 of 12 remote players turned on the font toggle.
