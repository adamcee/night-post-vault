---
title: "Letter Length Test"
date: 2026-06-26
evidence-maturity: emerging
tags: [narrative, letters, reading, word-count, primary-research]
method: "Nine players read 24 letters of three lengths in the greybox while Ines recorded whether each letter was read in full, skimmed, or skipped."
---
# Letter Length Test

Players read letters under 120 words in full 88% of the time, and skimmed or skipped letters over 200 words 64% of the time. Nine players in one round make this `[emerging]`.

## Method
- **Letters.** Ines wrote 24 letters in three length bands: eight under 120 words, eight of 120 to 200 words, and eight over 200 words.
- **Players.** Nine adults (P1–P9) from the devlog newsletter played in person from 2026-06-22 to 2026-06-25.
- **Task.** Each player delivered all 24 letters in the greybox and could open and read each one, giving 72 readings per length band.
- **Coding.** Ines watched reading time and scrolling, then asked one recall question per letter. A letter counted as read in full if the player answered the recall question and spent at least the time a slow reader needs.

## Findings
| Letter length | Readings | Read in full | Skimmed or skipped |
|---|---|---|---|
| Under 120 words | 72 | 63 (88%) | 9 (12%) |
| 120–200 words | 72 | 39 (54%) | 33 (46%) |
| Over 200 words | 72 | 26 (36%) | 46 (64%) |

- **Short letters get read.** Players read letters under 120 words in full 88% of the time.
- **Long letters get skimmed.** Players skimmed or skipped letters over 200 words 64% of the time.
- **Reading drops before 200 words.** The middle band fell to 54% read in full, so the drop starts above 120 words.

## Player Quotes
- **P2:** "If it fits on the screen, I read it."
- **P6:** "The long ones felt like homework, so I read the first line and the signature."
- **P9:** "I read the long one from Odile because I wanted to know what she owed."

## Limits
- **Test letters.** Ines wrote the letters for the test, so some long letters may simply have been duller.
- **Greybox reading.** Players read without art, music, or the finished letter screen.
- **Recall as a proxy.** Answering one question does not prove a player read every line.

## Reweave Triggers
- [[concepts/letter-budget]]: created. A soft limit of 120 words per letter, from the 88% full-read rate under 120 words.
- [[decisions/technical/ADR-T003-plain-text-dialogue-files|ADR-T003]]: informs tooling. The script parser should report each letter's word count so Ines can check the budget while writing.
