---
title: "Text Contrast and Size Standards"
date: 2026-08-19
evidence-maturity: established
tags: [accessibility, readability, standards, external]
method: "Ines read the published WCAG 2.2 success criterion 1.4.3 and the Game Accessibility Guidelines and recorded only the points below."
---
# Text Contrast and Size Standards

WCAG 2.2 requires text contrast of at least 4.5:1 for normal text and 3:1 for large text, and the Game Accessibility Guidelines recommend clear, adjustable text. Both are published external standards, so this doc is tagged `[established]`.

## Method
- **Sources.** Ines read the Web Content Accessibility Guidelines (WCAG) 2.2 at https://www.w3.org/TR/WCAG22/ and the Game Accessibility Guidelines at https://gameaccessibilityguidelines.com/.
- **Scope.** Ines recorded only the two points below, which bear on letter text in Night Post.

## Findings
- **Contrast.** WCAG 2.2 success criterion 1.4.3, Contrast (Minimum), requires a contrast ratio of at least 4.5:1 for normal text and 3:1 for large text ([WCAG 2.2](https://www.w3.org/TR/WCAG22/)).
- **Clear, adjustable text.** The Game Accessibility Guidelines recommend that game text be clear and adjustable ([Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/)).

## Limits
- **Two points only.** This doc does not summarize the rest of either standard.
- **Applying them is our call.** Using these targets for letters on a handheld screen is the team's interpretation, which [[research/accessibility/letter-readability-audit]] puts to use.

## Reweave Triggers
- [[decisions/product/PDR-P011-readable-letters|PDR-P011]]: supports (pending). The 4.5:1 contrast target and the advice on adjustable text back a readable body typeface and a font toggle; the record was written on 2026-08-26.
- [[architecture/CONSTITUTION]]: supports (pending) principle P2, "Every letter is readable at handheld size," added on 2026-08-26. The 4.5:1 target gives P2 a number to test against.
