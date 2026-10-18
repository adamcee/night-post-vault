---
title: "PDR-P014: Launch in English, Spanish, and German"
doctype: PDR
id: PDR-P014
domain: product
status: accepted
date: 2026-09-22
tags: [localization, languages, budget, launch]
constitution-clause: P4
supersedes: null
superseded-by: null
---
# PDR-P014: Launch in English, Spanish, and German

## Context
Spanish and German were the top two non-English languages requested in the community survey ([[research/market/community-survey-01]] [emerging]). Vendors quoted $0.11–$0.16 per word, so each language costs about $9,500–$13,800 at 86,000 words ([[research/localization/localization-cost-estimate]] [emerging]).

The 86,000-word figure assumes the three-region script ([[research/narrative/script-word-count]] [emerging]). Every word Ines adds raises the cost of each translation.

## Decision
Night Post launches in English, Spanish, and German. Other languages come after launch.

## Alternatives Considered
- **English only.** It is the cheapest option, but it ignores the two languages players asked for most.
- **More languages at launch.** Each added language costs another $9,500–$13,800, which a self-funded team cannot cover before revenue arrives.
- **Community translation.** It is free, but the team cannot review quality in languages it does not read.

## Consequences
- The two translations cost about $18,900–$27,500 in total ([[strategy/funding]]).
- The script files need a string export step, as noted in [[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]], and text must freeze before translation starts.
- Handwritten header fonts must include Spanish and German characters such as ñ, ü, and ß, and every translated letter must stay readable at handheld size under clause P2.
- The decision keeps scope within clause P4 of [[architecture/CONSTITUTION]].
