---
id: letter-reader
title: Letter Reader
date: 2026-05-15
status: Active
tags: [architecture, ui, letters, accessibility, typography]
---
# Letter Reader
*Rewritten 2026-08-26 for readable letters.*

The letter reader shows every letter in the game with a handwritten header and signature and a body set in a readable typeface ([[decisions/product/PDR-P011-readable-letters|PDR-P011]]). Every letter must be readable at handheld size, as clause P2 of [[architecture/CONSTITUTION]] requires.

## Why the Reader Changed
- **The first design failed on handhelds.** Letters were fully handwritten under [[decisions/product/PDR-P006-handwritten-letters|PDR-P006]], and 4 of 10 vertical-slice players on handhelds squinted at them ([[research/playtests/pt-04-vertical-slice]] [emerging]).
- **The audit confirmed it.** At 800p on a 7-inch screen, the handwritten body text failed the 4.5:1 contrast target on parchment and was below a comfortable size ([[research/accessibility/letter-readability-audit]] [emerging]).
- **The standard sets the target.** WCAG 2.2 success criterion 1.4.3 asks for at least 4.5:1 contrast for normal text and 3:1 for large text ([[research/accessibility/text-contrast-and-size-standards]] [established]).
- **Players use the toggle.** In the demo build, 5 of 12 players turned on the font toggle, which strengthened PDR-P011 ([[research/playtests/pt-05-demo-build]] [emerging]).

## Layout of a Letter
| Part | Typeface | Rule |
|---|---|---|
| **Header** (sender, place, date) | Handwritten, one per sender | Large text, at least 3:1 contrast on parchment. |
| **Body** | Readable serif | At least 4.5:1 contrast on parchment; at least 22 pixels tall at 800p. |
| **Signature** | Handwritten, matching the header | Large text, at least 3:1 contrast. |
| **Seal** (sealed letters only) | Wax seal art | Shows the sender's mark. |

- **One screen per letter:** a letter within the 120-word [[concepts/letter-budget]] fits one screen at 800p without scrolling.
- **Longer letters:** letters over the budget turn pages with the shoulder buttons. The writer sees a warning when a letter goes over budget ([[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]]).
- **Parchment:** the background texture is flattened behind the body text so the contrast stays even across the page.

## The Font Toggle
- **What it does:** switches the body text from the default serif to a plainer sans-serif one size larger. The header and signature stay handwritten.
- **Where it lives:** in the settings menu and as a button in the reader itself, so players find it when they need it.
- **Default:** the toggle starts off. The default body text already meets clause P2, and the toggle serves players who still find it hard to read.

## Opening a Sealed Letter
- A sealed letter shows only the header and the seal. To open it, the player holds the open button for one second, so nobody opens a letter by accident.
- Ledger comments when Wren breaks a seal, and the delivery earns a nosy postmark ([[architecture/systems/postmarks]]).
- What Wren reads can change later talk lines and what happens next. The consequences are social, never a game over ([[decisions/product/PDR-P008-sealed-letters-can-be-opened|PDR-P008]], [[concepts/sealed-letter]]).

## The Letter Case Keeps Every Read Letter
- Every letter Wren has read stays in the letter case, a menu sorted by region and by night.
- Opened sealed letters carry a broken-seal icon, so the player can see what they pried into.

## Localization Must Still Fit
- Spanish and German launch with English ([[decisions/product/PDR-P014-launch-languages|PDR-P014]]). Translated letters can run longer than the English, so the one-screen rule needs a check in each language.
- The readability audit has not been run on translated text yet. That check is a task in [[prototype/implementation-plan]].
