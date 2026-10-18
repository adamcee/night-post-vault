---
title: "CONSTITUTION.md — Night Post Invariants"
id: CONSTITUTION
date: 2026-08-26
status: Active
tags: [architecture, invariants]
---
# CONSTITUTION.md — Night Post Invariants

*These invariants set what Night Post must never do. Breaking one requires a new decision record that supersedes the clause; "it would be easier" is not a reason.*

## Part I — Product & Domain Invariants

- **P1 — No death, no fail state from encounters.** Wren cannot die, and no encounter ends the night; a failed parley costs oil, time, or a detour. Players disliked turn-based combat in testing ([[research/playtests/pt-02-greybox-encounters]] [emerging]), and the tone depends on walks that never end in death. Added 2026-06-24 by [[decisions/product/PDR-P009-parley-encounters|PDR-P009]].
- **P2 — Every letter is readable at handheld size.** Every letter's body text meets 4.5:1 contrast and a comfortable size at 800p on a 7-inch screen, in every launch language. Letters carry the story, and the handwritten font failed this test ([[research/accessibility/letter-readability-audit]] [emerging]). Added 2026-08-26 by [[decisions/product/PDR-P011-readable-letters|PDR-P011]].
- **P3 — Offline, single-player, no microtransactions.** Night Post needs no account or connection, has one player, and sells once at a fixed price. Set when the vault was created on 2026-04-06; applied in [[decisions/rejected/PDR-P007-co-op-courier-mode|PDR-P007]], [[decisions/technical/ADR-T005-atomic-saves|ADR-T005]], and [[decisions/product/PDR-P010-price-18-dollars|PDR-P010]].
- **P4 — Scope fits three people and an October 2027 launch.** Any feature, region, or language must fit the team and the runway. Self-funding leaves no room for a slipped launch. Set when the vault was created on 2026-04-06; applied in [[decisions/product/PDR-P012-three-regions|PDR-P012]], [[decisions/rejected/PDR-P013-full-voice-acting|PDR-P013]], and [[decisions/product/PDR-P014-launch-languages|PDR-P014]].

## Part II — Stack Invariants

- **S1 — Godot 4 and GDScript only.** The project uses no other engine and no C# or native-code modules. One programmer must be able to maintain the whole codebase. Added 2026-04-08 by [[decisions/technical/ADR-T001-godot-4-engine|ADR-T001]].
- **S2 — 30 fps at 800p on the handheld floor.** Every scene holds 30 frames per second at 1280×800 on a handheld PC before it counts as done. Cutting effects late costs more than never adding them. Added 2026-04-15 by [[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]].
- **S3 — All text lives in plain-text files under version control.** Dialogue, letters, barks, and interface strings live in script files, never inside engine resources or images. The writer edits text directly, and translation needs a clean string export. Added 2026-04-29 by [[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]].

## Part III — Violation Protocol

If there is a genuine reason to break an invariant:
1. Stop. Do not implement the violation.
2. Create an ADR in `/decisions/technical/` or `/decisions/product/` that:
   - Names the specific CONSTITUTION clause being superseded
   - States the reason in full
   - Documents the alternatives considered
   - States the consequences
3. Get the ADR reviewed before implementing.
