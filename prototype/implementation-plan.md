---
id: implementation-plan
title: Implementation Plan
date: 2026-04-06
status: Active
tags: [prototype, plan, ledger, production]
---
# Implementation Plan
*Updated: 2026-10-09*

This file is the AI ledger: every new action item lands here, and Ines moves items to [[prototype/human-task-list]] during her weekly review.

Item format: `- [ ] **Title**: what, and how you'll know it's done (session type)`, with `[~]` for in progress. Tasks that came from new evidence are marked `(reweave: [[research/...]])`.

## Now
- [~] **Choose a localization vendor**: compare vendors A, B, and C for Spanish and German, resuming from [[drafts/2026-10-09-resume-localization-vendors]]; done when Ines approves one vendor and the hand-over note is deleted (research) (reweave: [[research/localization/localization-cost-estimate]]).
- [ ] **Submit the Northern Arts Fund application**: ask for the localization cost so the launch languages don't draw on runway; done when it is submitted by 2026-11-30 ([[strategy/funding]]) (production).
- [ ] **Send the publisher follow-up**: send the publisher who asked for a follow-up the festival results and the three-region plan; done when the email is sent and any reply is logged (production) (reweave: [[research/market/publisher-pitch-feedback]]).
- [ ] **Finish Thimble Cross**: final art, script, and music for the tutorial region; done when it holds the handheld floor and Ines signs off the script, by 2027-01-29 ([[world/regions/thimble-cross]], [[strategy/release-plan]]) (writing, art, build).

## For the Owner: Keep, Drop, or Decide
- [ ] **Keep or drop the festival marketing plan**: [[drafts/ai-report-festival-marketing-plan]] was written for a festival that has passed; done when Ines says keep (tighten it for launch) or drop (delete it) (production).
- [ ] **Pick festival quotes for the store page**: store copy needs Ines's yes, so she chooses which comments about the letters and tone to use; done when she approves the copy (production) (reweave: [[research/market/demo-festival-results]]).

## Decisions Owed
- [ ] **Foldable map**: decide whether Night Post gets a map without undoing the mastery in [[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]], and resolve [[ideas/foldable-map]]. A PDR has been in draft in chat since 2026-10-09, one round of the usual two to four, and nothing is written yet; done when Ines approves the draft and the record is written (decision) (reweave: [[research/market/demo-festival-results]]).
  - **No map:** keeps learning the forest as the core mastery. It ignores 23 festival requests, though landmarks already cut getting lost to 2 of 12 ([[research/playtests/pt-05-demo-build]] [emerging]).
  - **A map Wren fills in by hand:** answers the requests and keeps the mastery. It adds a new screen that must stay readable at handheld size (clause P2).
  - **A full map that shows the paths:** answers the requests most directly. It removes the mastery that PDR-P004 protects.

## Drafts Awaiting Promotion
- [ ] **Tighten the festival marketing plan**: run [[drafts/ai-report-festival-marketing-plan]] through the ingestion gate, keeping only what applies to launch; done when it passes the promotion checklist or Ines drops it above. It was missed before the festival and moved here from Phase 4 on 2026-10-08 (writing).
- [ ] **Review the Hushfolk lore draft**: Ines checks [[drafts/ai-lore-hushfolk-expansion]] against [[world/factions/the-hushfolk]] and [[world/characters/mothwife-sel]]; done when approved parts move into `world/` and the rest is deleted (writing).

## Vault Maintenance

**Vault review 2026-10-08: routed items.** The session fixed the mechanical findings itself: folder READMEs, `###` headings in eight research docs, meta-commentary in the constitution, and the tag list ([[prototype/implementation-logs/2026-W41]]).
- [ ] **Source the regional pricing claim** (E. Research): the claim in [[decisions/product/PDR-P010-price-18-dollars|PDR-P010]] that storefront regional pricing lowers the price in Latin American markets is still `[unsourced]`; done when a research doc backs it with a link or the claim is cut (research).
- [ ] **Resolve or justify an old idea** (F. Lifecycle): [[ideas/letter-writing-minigame]] has been open since 2026-06-30, longer than a quarter; done when Ines resolves it or records why it stays open (design).
- [ ] **Run the first plan triage** (D. Ledger): the ledger has never been triaged, and the quarterly trigger is due; done when a row is added to the History table in [[vault-guide/implementation-plan-triage]] by 2026-12-31 (vault maintenance).
- [ ] **Scan `world/` and `prompts/`** (A. Structure): `vault-review-scan.py` skips both folders by default, so canon and prompts miss the writing-discipline scan; done when Ines approves adding them to the script's default folders and its `SKILL.md` says so (vault maintenance).

## Phase 1: Concept (Done, April 2026)
- [x] Write the core fantasy: a night courier whose every quest is a letter ([[decisions/product/PDR-P001-letters-are-the-quests|PDR-P001]]).
- [x] Choose Godot 4 with GDScript ([[decisions/technical/ADR-T001-godot-4-engine|ADR-T001]]).
- [x] Set the handheld PC as the minimum target ([[decisions/technical/ADR-T002-handheld-performance-floor|ADR-T002]]).
- [x] Draft the world: [[world/hollowmere]], five regions, and three factions ([[world/README]]).
- [x] Plan five regions ([[decisions/product/PDR-P002-five-regions|PDR-P002]], since superseded).
- [x] Run the paper prototype with five players ([[research/playtests/pt-01-paper-prototype]]).
- [x] Note the paper "combat" doubt for the greybox encounter test (reweave: [[research/playtests/pt-01-paper-prototype]]).
- [x] Store dialogue and letters as plain-text files with an in-house parser ([[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]]).

## Phase 2: Greybox (Done, May to June 2026)
- [x] Build hand-authored greybox paths for one region; procedural generation rejected ([[decisions/rejected/ADR-T004-procedural-forest|ADR-T004]]).
- [x] Build moon-phase path layouts with four phases ([[decisions/product/PDR-P004-moon-shifting-paths|PDR-P004]], [[architecture/systems/moon-and-paths]]).
- [x] Build turn-based encounters for playtest 2 ([[decisions/product/PDR-P003-turn-based-encounters|PDR-P003]], since superseded).
- [x] Replace turn-based encounters with a parley prototype (reweave: [[research/playtests/pt-02-greybox-encounters]]).
- [x] Run playtest 3 on the parley prototype ([[research/playtests/pt-03-parley-prototype]]).
- [x] Write [[architecture/systems/parley]] and remove health and death from the design ([[decisions/product/PDR-P009-parley-encounters|PDR-P009]]).
- [x] Replace volumetric fog with a baked fog layer in Gloamwick (reweave: [[research/technical/handheld-perf-benchmark]]).
- [x] Record wetland ambience for the night soundscape ([[research/audio/field-recording-trip]]).
- [x] Build the sealed-letter open action ([[decisions/product/PDR-P008-sealed-letters-can-be-opened|PDR-P008]]).
- [x] Add a word count and a 120-word warning to the script parser (reweave: [[research/narrative/letter-length-test]]).

## Phase 3: Vertical Slice (Done, July to August 2026, finished 2026-08-28)
- [x] Write the [[prototype/specs/vertical-slice]] spec.
- [x] Paint Thimble Cross and the first Gloamwick route in the night palette ([[decisions/product/PDR-P005-painted-night-palette|PDR-P005]]).
- [x] Give red and green route lanterns distinct shapes (reweave: [[research/accessibility/night-palette-colorblind-test]]).
- [x] Trim slice letters to the 120-word [[concepts/letter-budget]] (reweave: [[research/narrative/letter-length-test]]).
- [x] Build fast and kind postmarks with tier 1 abilities ([[architecture/systems/postmarks]]).
- [x] Switch saves to write-temp-then-rename (reweave: [[research/technical/save-corruption-test]]).
- [x] Split the music into layers that thin out on long walks (reweave: [[research/audio/music-listening-test]]).
- [x] Run the community survey ([[research/market/community-survey-01]]).
- [x] Set the launch price at $18 ([[decisions/product/PDR-P010-price-18-dollars|PDR-P010]]).
- [x] Run playtest 4 on the slice ([[research/playtests/pt-04-vertical-slice]]).

## Phase 4: Festival Demo (Done, September to 2026-10-05)
- [x] Write the [[prototype/specs/festival-demo]] spec.
- [x] Give every waymark in the demo a fixed landmark (reweave: [[research/playtests/pt-04-vertical-slice]]; absorbed [[ideas/waymark-landmarks]]).
- [x] Set letter bodies in a readable typeface and keep handwriting for headers and signatures (reweave: [[research/accessibility/letter-readability-audit]]).
- [x] Add the font toggle to settings and to the letter reader (reweave: [[research/accessibility/letter-readability-audit]]).
- [x] Pitch three publishers and log the feedback ([[research/market/publisher-pitch-feedback]]).
- [x] Re-plan for three regions and cut the Drowned Bell and the High Briar (reweave: [[research/production/scope-and-burn]]).
- [x] Move the Drowned Bell's best story to Sallow Ferry and fold the High Briar into Gloamwick's edges ([[decisions/product/PDR-P012-three-regions|PDR-P012]]).
- [x] Limit voice to barks and drop full voice acting (reweave: [[research/narrative/script-word-count]]).
- [x] Set launch languages to English, Spanish, and German ([[decisions/product/PDR-P014-launch-languages|PDR-P014]]).
- [x] Run playtest 5 on the demo build ([[research/playtests/pt-05-demo-build]]).
- [x] Ship the demo to the festival on 2026-09-29.
- *(Open task to tighten the festival marketing plan moved to Drafts Awaiting Promotion, 2026-10-08 vault review.)*

## Phase 5: Production (Current, from 2026-10-07)
- [x] Archive the festival build and tag it in version control.
- [x] Log festival results in [[research/market/demo-festival-results]].
- [ ] **Audit Spanish and German letters at 800p**: rerun the readability audit on translated letters; done when every sampled letter meets clause P2 of [[architecture/CONSTITUTION]] (research) (reweave: [[research/accessibility/letter-readability-audit]]).
- [ ] **Recheck runway**: compare runway with actual spend on 2026-12-05; done when the new count is in [[strategy/funding]] (production) (reweave: [[research/production/scope-and-burn]]).
- [ ] **Finish Gloamwick**: final art, script, and music, including the High Briar edges; done by 2027-03-26 ([[world/regions/gloamwick]]) (writing, art, build).
- [ ] **Finish Sallow Ferry**: final art, script, and music, including the moved Drowned Bell story; done by 2027-05-28 ([[world/regions/sallow-ferry]]) (writing, art, build).
- [ ] **Build the careful and nosy abilities**: tier 2 and tier 3 postmark abilities; done when all four postmark kinds unlock abilities in the build ([[architecture/systems/postmarks]]) (build).
- [ ] **Add landmarks in Gloamwick and Sallow Ferry**: give every waymark a fixed landmark, as in Thimble Cross; done when no waymark in either region lacks one (art) (reweave: [[research/playtests/pt-05-demo-build]]).
- [ ] **Record voiced barks**: short spoken reactions in English, Spanish, and German; done when every bark in the script has a take in all three languages ([[decisions/rejected/PDR-P013-full-voice-acting|PDR-P013]]) (audio).
- [ ] **Run playtest 6**: test a full three-region build on handhelds; done when the results are written up with [[prompts/playtest-synthesis]] (research).
