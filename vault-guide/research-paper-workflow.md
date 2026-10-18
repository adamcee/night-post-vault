---
title: Research Paper Workflow
id: research-paper-workflow
date: 2026-04-06
status: Active
tags: [protocol, vault-administration, research, workflow]
---
# Research Paper Workflow

External sources enter the vault through three layers: a reference manager holds every source, literature notes hold the human's reading of sources actually read, and full-text markdown holds the few sources a session must check word for word. Each layer is added only when it is needed.

A source here is anything a vault doc may cite: an academic paper, an industry report, a book, a standard, a long article, or an interview transcript.

## Trigger

Apply it when a source enters the project that a vault doc will cite, when the human finishes reading a source, or when a reweave or traceability check needs the original text.

## The Three Layers

- **Reference manager (every source).** Stores the files, bibliographic metadata, and a stable citation key for each source, and is where the human reads and highlights. Any reference manager works; Zotero is a free, widely used option.
- **Literature notes (sources actually read).** One note per source the human has read, in `research/literature-notes/<citekey>.md`. It holds the human's synthesis, a "Relevance to Vault" section linking the decisions it informs, and the highlights. A plugin can import highlights from the reference manager, but the synthesis is the human's own writing.
- **Full-text markdown (select sources only).** A markdown conversion of the whole source in `research/sources/<citekey>.md`, so a session can check a claim against the original. Use any PDF-to-markdown converter; Marker and MinerU are two open-source options.

## Steps

1. **Add the source to the reference manager.** Every source the vault cites or may cite goes here, with its citation key.
2. **Write or update the research doc.** The doc in `research/` extracts the findings that matter to the project and follows [[vault-guide/research-traceability]] and [[vault-guide/style-guides/research-paper-discipline]].
3. **Create a literature note after reading.** Import highlights if a plugin is available, then the human writes the synthesis and the relevance section. Set `evidence-maturity` after reading, not before.
4. **Convert the full text only when needed.** Convert a source when its evidence is `[emerging]`, when it sits under a contested decision or reweave, when the research doc may have lost methods or limits, or when the project needs cross-source synthesis at the level of specific findings.
5. **Set the frontmatter and links.** Give each literature note and conversion the fields below, and link the three layers to each other and to the decisions they inform.

## Frontmatter Fields

```yaml
---
id: citekey
date: YYYY-MM-DD
status: Active
tags: [literature-note]          # or [source-text]
source-type: literature-note     # literature-note or full-text-conversion
original-file: <path or reference-manager link to the original file>
citekey: authorYear
evidence-maturity: supported     # set after reading
tool: <converter name>           # full-text conversions only
---
```

A research doc with a full-text conversion also gets `source-path: research/sources/<citekey>` in its frontmatter.

## When to Add a Source to Each Layer

| Situation | Reference manager | Literature note | Full text |
|---|---|---|---|
| Source cited in a vault doc | Yes | When read | Only to verify a claim |
| Source being read now | Yes | Yes | Only if emerging or contested |
| Emerging source central to a decision | Yes | Yes | Yes |
| Established background source | Yes | When read | Rarely |
| Source found during a reweave that contradicts a decision | Yes | Yes | Yes |

## Rules

- **The human writes the synthesis.** A literature note records what the human understood and questioned. An AI session may import highlights and draft the relevance links, but it never writes the synthesis in the human's voice.
- **AI summaries stay secondary.** An AI-generated summary of a source keeps `evidence-maturity: secondary` and links to the literature note once one exists.
- **Add layers as needed.** Start with the reference manager, add literature notes as sources get read, and add conversions only when a check needs them.
- **Conversions are evidence, not prose.** A full-text conversion is exempt from tightening but keeps its frontmatter, and it never replaces the research doc.
- **Large files stay out of the vault.** Original PDFs and media live in the reference manager; the vault links to them through `original-file`.

## Common Failure

The vault cites AI summaries of sources nobody has read, and no one can check whether a finding says what the summary claims. A reweave then compares new evidence against a summary's reading instead of the source.
