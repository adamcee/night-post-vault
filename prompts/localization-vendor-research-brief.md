---
title: Localization Vendor Research Brief
date: 2026-10-09
status: Active
tags: [prompts, research-brief, localization]
target-model: Gemini deep research
---
# Localization Vendor Research Brief

Run this brief in a deep-research tool to learn how small game teams compare localization vendors, before Ines chooses between the three quotes in [[research/localization/localization-cost-estimate]]. The report comes back as an AI synthesis: it lands in `drafts/`, passes the [[vault-guide/ingestion-gate]], and enters `research/localization/` tagged `secondary` until primary sources back it.

The 2026-10-09 session that left [[drafts/2026-10-09-resume-localization-vendors]] wrote it, and the next session runs it before resuming that comparison.

## Prompt

```markdown
# Research brief: comparing game localization vendors

## 1. Context
- Night Post is a narrative adventure game for PC and handheld PCs, made by a self-funded team of three. It launches in October 2027 in English, Spanish, and German.
- The script is about 86,000 English words, 58% of them in-game letters. Text lives in plain-text script files under version control, not in engine resources.
- Every letter must stay readable at 800p on a 7-inch screen in every language, so translated text that runs longer than English matters.
- The team holds written per-word quotes from three vendors, called A, B, and C:
  - A: $0.11 per word, translation only.
  - B: $0.13 per word, translation plus one review pass by a second translator.
  - C: $0.16 per word, translation, review, and a check of the text in the running game.
- Decision this informs: which vendor to hire for Spanish and German, and what to ask each vendor before signing.

## 2. Questions (answer these and only these)
1. What do "translation", "review" (editing by a second linguist), and "linguistic quality assurance" (checking text in the running game) each catch that the others miss?
2. For a text-heavy narrative game, what share of a localization budget do review and in-game checking usually take?
3. How much longer do Spanish and German text run than English, on average and at the high end?
4. What should a team send a vendor up front: glossary, style guide, character notes, context screenshots, word limits?
5. What contract terms matter for a small team: rates for later patches, minimum fees, ownership of translation memory, turnaround, and revision rounds?
6. What warning signs suggest a vendor will deliver poor game text?

## 3. Sources
- Prefer, in order: published localization industry standards and glossaries; talks and postmortems by game localization staff; guides published by professional translator associations.
- Ignore vendor marketing pages, rate-card listicles, and anything about machine translation or voice recording.
- Name no vendors, games, or studios in the report. Describe practices, not companies.

## 4. Output format
Return one markdown file:
- YAML frontmatter with `title`, `date`, `tags: [localization, vendors]`, and `evidence-maturity: secondary`.
- A two-sentence summary that answers the decision question first.
- One `##` section per question above, in order. In each, list findings with a citation (title and URL) after every claim, then any inferences under a bold **Inference** label.
- A `## Questions to Ask Each Vendor` section with at most eight questions.
- A closing `## Reweave Triggers` section naming which of these the findings may affect: the launch-languages decision, the full-voice-acting rejection, the funding plan, and the readable-letters rule.

## 5. Constraints
- Keep the report under 1,500 words. Stop researching a question once two independent sources agree.
- If you cannot find a source for a claim, mark it [unsourced] rather than inventing a citation.
- If a question has no good answer in the sources, say so in one sentence and move on.
- Do not recommend vendor A, B, or C. Give the criteria; the team makes the choice.
```

## After It Returns

- **Gate first.** Save the report as `drafts/localization-vendor-practices.md` and tighten it before it moves to `research/localization/`.
- **Then resume.** Pick up the comparison from [[drafts/2026-10-09-resume-localization-vendors]] and run the [[vault-guide/reweave-protocol]] on the new doc.
