---
title: "PDR-P007: Online Co-op Courier Mode (Rejected)"
doctype: PDR
id: PDR-P007
domain: product
status: rejected
date: 2026-06-02
tags: [multiplayer, co-op, networking, tone]
constitution-clause: P3
supersedes: null
superseded-by: null
---
# PDR-P007: Online Co-op Courier Mode (Rejected)

## Context
During greybox work the team discussed an online two-player mode, in which two couriers split one night's satchel of letters. Co-op could widen the audience and give friends a reason to play together.

## Decision
Rejected. Night Post stays a single-player game.

## Reasons for Rejection
- **Networking cost.** Online play needs session hosting, synced moon-shift and letter state, and testing across real connections. Tomas is the only programmer, and this work would take months from the game.
- **The solitary tone.** Wren walks the night alone with Ledger, and the eerie mood depends on that quiet. A second courier on voice chat turns the walk into a social outing.
- **Private choices.** Opening a sealed letter is the courier's private temptation ([[concepts/sealed-letter]]). With two players, one player makes that choice for both.
- **Constitution clause P3.** [[architecture/CONSTITUTION]] keeps Night Post offline and single-player.

## Alternatives Considered
- **Local co-op on one screen.** It removes the networking work, but it still breaks the solitary tone and doubles the interface on a 7-inch screen.
- **Ledger as a companion.** Accepted in spirit: the retired crow already scouts and comments, which gives Wren company without a second player ([[world/characters/ledger]]).

## Consequences
- Night Post needs no servers, accounts, or online features.
- Future sessions should not reopen multiplayer unless a new record supersedes clause P3.
