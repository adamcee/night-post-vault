---
title: "AI Writing Discipline: Research Docs"
id: style-research-001
date: 2026-04-06
status: Active
tags: [style-guide, writing-discipline, research]
---
# AI Writing Discipline: Research Docs

## BLUF
Research docs may use longer, single-thought paragraphs and more precise vocabulary than other vault docs, because sustained arguments break apart under the two-sentence rule. Every other rule in [[vault-guide/style-guides/ai-writing-discipline-core]] still applies.

## Scope
These rules cover docs in `research/` that synthesize external sources, including literature notes and AI-generated research reports after promotion. All other vault writing follows [[vault-guide/style-guides/ai-writing-discipline-core]].

Full-text conversions in `research/sources/` are evidence, not prose, and are exempt from tightening ([[vault-guide/research-paper-workflow]]).

## Paragraphs
- **Single-Thought Paragraphs Are Allowed:**
  - A paragraph may run past two sentences when it develops one continuous thought.
  - If a paragraph introduces several separate data points, switch to a bulleted list.
- **Every Word Earns Its Place:**
  - Longer prose is not looser prose. Cut padding, corporate filler, and dead jargon as strictly as in any other doc.

## Openings
- **The First Sentence States the Finding:**
  - Open with the core finding or its relevance to the project, never with background.
  - Not "Professor X has studied Y for thirty years." Instead: "X's study of Y shows that Z, which supports our plan to do W."
- **Biographies Stay Short:**
  - Give a researcher's name, affiliation, and one credential in two lines at most. Cut or footnote the rest.
- **Executive Summaries Run 12 Lines or Fewer:**
  - Use bullets with bold lead-in terms.

## Vocabulary
- **Precise Words Over Simple Ones When They Differ:**
  - Prefer plain words, but use a more exact term when it carries meaning the plain word would lose. Terms of art are precise, not complex.
- **The Slop Purge Still Applies:**
  - Cut *delve, testament, tapestry, synergy, robust, landscape,* and *leverage*.

## Cleanup Pass on AI Reports
AI-generated research reports arrive with abstract-style openings, narrative preambles before tables, and repetitive framing. Before promotion, each one gets this pass on top of the [[vault-guide/ingestion-gate]]:

1. **Replace the abstract-style opening** with a sentence that states the finding.
2. **Delete preambles** before tables and lists that explain themselves.
3. **Deduplicate adjective clusters** down to the single most precise term.

The report keeps `evidence-maturity: secondary` in its frontmatter ([[vault-guide/research-traceability]]).

## Structure
Research docs keep the vault's structural rules: strict YAML frontmatter with `evidence-maturity`, flat `##` headings, plain Markdown with no HTML, and a `## Reweave Triggers` section ([[vault-guide/reweave-protocol]]).
