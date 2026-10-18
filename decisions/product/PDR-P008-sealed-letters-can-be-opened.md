---
title: "PDR-P008: Players May Open Sealed Letters"
doctype: PDR
id: PDR-P008
domain: product
status: accepted
date: 2026-06-10
tags: [letters, choice, consequences, reweave-strengthened]
constitution-clause: null
supersedes: null
superseded-by: null
---
# PDR-P008: Players May Open Sealed Letters

## Context
In the paper prototype, the letter-opening choice was the most discussed moment for all 5 players ([[research/playtests/pt-01-paper-prototype]] [emerging]). Reading another person's mail is the courier's one temptation, and it gives players a reason to care what letters say.

## Decision
Wren may open any sealed letter ([[concepts/sealed-letter]]). What she reads changes what people say to her and what happens next, and the consequences are always social, such as lost trust, gossip, or a closed door. Opening a letter never ends the game.

## Alternatives Considered
- **Sealed letters stay sealed.** It is simpler to write, but it removes the most discussed moment from the paper test.
- **Getting caught as a failure.** If being caught cost the delivery or Wren's job, players would reload saves to undo it or never open letters at all.
- **Opening with no consequences.** Players would open everything, and the choice would mean nothing.

## Consequences
- Ines writes two versions of every reaction that depends on a letter: one for a sealed delivery and one for an opened delivery.
- The "nosy" postmark rewards opening, so the progression system treats curiosity as a valid way to play ([[concepts/postmark]]).
- The dialogue parser needs conditions on letter state ([[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]]).
- **Reweave 2026-06-19:** strengthened by [[research/playtests/pt-03-parley-prototype]] [supported]: 7 of 8 players preferred parley to the earlier encounters. We read this to mean players favor social consequences over combat ones, which supports keeping letter consequences social.
