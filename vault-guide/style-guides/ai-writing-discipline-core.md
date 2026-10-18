---
title: "AI Writing Discipline: Core Architecture"
id: style-core-001
date: 2026-04-06
status: Active
tags: [style-guide, writing-discipline, core, formatting]
---
# AI Writing Discipline: Core Architecture

## BLUF
Vault documents are written for the human owner first and the next AI session second. They follow ISO 24495-1 plain language and the rules below, which draw on Strunk & White and military correspondence practice.

## Scope
These rules cover every document in `decisions/`, `strategy/`, `architecture/`, `concepts/`, and `vault-guide/`, and any other vault document an AI agent writes or substantially edits. Research docs follow [[vault-guide/style-guides/research-paper-discipline]], which relaxes a few rules and keeps the rest.

Files under any `archive/` folder, including `drafts/archive/`, are exempt. So are `journal/` and untouched `_source-<name>.md` originals.

## Plain Language (ISO 24495-1:2023)
A document is in plain language when its readers can:
- **Get what they need** (relevant). Write for the reader's task and cut what doesn't serve it.
- **Find it easily** (findable). Put the main point first and use headings that say what each section contains.
- **Understand it** (understandable). Use familiar words, short sentences, and define terms on first use.
- **Use it** (usable). The reader can act on the document without asking for clarification.

## Structure and Formatting
- **Flat Heading Hierarchy:**
  - Use `#` for the document title and `##` for sections. Use `###` only when a section truly needs subsections.
- **Descriptive Headings:**
  - A heading says what the section contains ("Pricing Is Per Visit"), not a vague label ("Discussion").
- **No HTML:**
  - Write plain Markdown. No HTML tags, inline styles, or embedded markup.
- **Tables Only for Tabular Data:**
  - Use a table when the content has rows and columns that readers compare. Use a list for everything else.
- **Strict Frontmatter:**
  - Every vault document starts with YAML frontmatter holding `id`, `date` (`YYYY-MM-DD`), `status`, and `tags` as a list. Decision records use the fields in [[decisions/_BASES_SCHEMA]].
- **Table/List Preamble Ban:**
  - If a table or list is self-explanatory, do not precede it with a narrative paragraph.
  - The most allowed is one bold sentence stating what the table shows. If that sentence restates the section heading, delete it.

## Paragraphs
- **BLUF (Bottom Line Up Front):**
  - The core decision or insight must be the first sentence of the document and of each section. Zero introductions.
- **The Paragraph Ban:**
  - Limit standard paragraphs to a maximum of two sentences. If a thought requires more, use a bulleted list with bolded lead-in terms.
- **Concrete Before Abstract:**
  - Lead with the example ("collect the payment, then send the receipt"). Generalize only if the abstraction adds something the example did not.
- **Semantic Deduplication:**
  - Never stack near-synonymous adjectives ("continuous, formative, real-time, embedded"). Pick the most precise term; use it once.
  - If two sentences in the same section make the same claim in different words, delete the weaker one.
- **Em-Dash Rationing:**
  - Use one em-dash per paragraph at most. If a paragraph needs more, make the aside its own sentence or cut it.

## Sentences and Words
- **Active Voice:** Use active voice exclusively. Omit needless words.
- **Grammatical Completeness:**
  - Write complete, grammatically correct sentences. Short sentences are good. Fragments are not.
  - "Same structure, opposite goal." is not a sentence. "Both use the same structure but aim at opposite goals." is.
- **Prefer Simpler Language:**
  - Use the plainest word that carries the meaning. "Different" over "inverted," "uses" over "utilizes," "describes" over "articulates."
  - Terms of art are precise language, not complex language. The rule targets synonyms where the fancier word adds nothing.
- **Define Terms on First Use:**
  - Spell out an abbreviation or define a term of art the first time it appears in a document.
- **No Slop Words:**
  - Cut *delve, testament, tapestry, synergy, robust, landscape,* and *leverage*. These words are fine elsewhere, but in vault documents they signal unreviewed AI output.
- **No Hedging Stacks:**
  - State the claim at the confidence the evidence supports. Write "may fail," not "it might potentially be possible that it could fail."

## AI Silence
- **No Throat-Clearing:** Absolutely no openers such as "I have analyzed..."
- **No Meta-Commentary:**
  - The ban extends to document body text. Banned phrases include "This section covers," "As previously discussed," "It is worth noting," and "The following table shows."
  - Exception: a cross-reference to another vault doc is not meta-commentary. "See [[vault-guide/reweave-protocol]] for the full steps" is allowed.
- **No Closing Filler:**
  - End when the content ends. No closing summary that repeats the document, and no "In conclusion" or "Hope this helps."

## No Reification
- Do not name abstract observations. If two things differ, describe the difference in a sentence. Do not capitalize it, give it a heading, or declare it a principle.
- **The Slop Ladder:** AI prose often climbs three steps: (a) state an observation, (b) restate it with a metaphor or capitalized name, (c) declare it foundational. Keep (a) and delete (b) and (c).
  - (a) "The two tools optimize for different things." Keep.
  - (b) "Call it The Inversion." Delete.
  - (c) "The Inversion is the core principle of our approach." Delete.

## Rules by Document Type
- **ADR/PDR Scope Boundary:**
  - ADRs and PDRs record Context, Decision, and Consequences. They do not contain implementation specs, code examples, or step-by-step workflows.
  - Link implementation detail to a spec doc. A one-line snippet for illustration is fine; multi-line code blocks are not.
- **Strategy Docs Use Purpose, Method, End State:**
  - Frame a strategy around its purpose (why), method (how, in broad strokes), and end state (what done looks like). This is Commander's Intent from military doctrine.
- **Biographies Stay Short:**
  - A person's biography runs two lines at most: name, affiliation, and one relevant credential. Cut or footnote the rest.

## Tightening Checklist
The 10-point checklist that every AI-written or AI-edited document must pass lives in [[AGENTS]] under Writing Discipline. This page holds the rules and their reasons; `AGENTS.md` holds the gate.
