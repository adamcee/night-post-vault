---
title: Research Traceability
id: research-traceability
date: 2026-04-06
status: Active
tags: [protocol, vault-administration, research, evidence]
---
# Research Traceability

Every empirical claim in a decision, strategy, or design doc links to the vault research doc that supports it. Without these links, nobody can find which decisions depend on which evidence, and the [[vault-guide/reweave-protocol]] becomes guesswork.

**Format:** `claim text ([[research/source-doc]] [maturity-tag])`

## Trigger

Apply it whenever a session writes or edits a decision record, strategy doc, design doc, or research doc. Apply the backfill rule whenever a session touches an existing decision record for any reason.

## Steps

1. **Link each empirical claim** to the vault research doc that supports it, not to the external source. The vault doc already holds the relevant finding and its maturity tag.
2. **Mark findings and inferences.** A finding is a claim the source states directly, and it gets a plain link. An inference applies the source to this project, and it says so: `we read this to mean X for our context ([[research/source-doc]])`.
3. **Prefer the primary source.** When both a primary source doc and a secondary synthesis exist, link the primary. When only a secondary exists, mark the citation: `([[research/ai-report-name|secondary]])`.
4. **Tag maturity inline** with one of the four tags below, placed after the link.
5. **Flag what has no source.** A claim with no supporting research doc gets `[unsourced]`, so a later session knows to fill the gap or drop the claim.
6. **Set frontmatter on research docs.** Each research doc carries `evidence-maturity:` with one of the four tag names. An AI-generated synthesis or literature review carries `evidence-maturity: secondary` instead.

## Evidence Maturity Tags

| Tag | Meaning |
|---|---|
| `[established]` | Ten or more years, extensively replicated, foundational to the field. |
| `[supported]` | Multiple studies and strong grounding, with less than a decade of replication. |
| `[emerging]` | A single study or very recent work, not yet replicated. |
| `[theoretical]` | A conceptual framework without direct empirical validation in this context. |

## Rules

- **Never write a research doc from memory.** A research doc comes from source material the session can read, such as a paper, report, interview, dataset, or article. Training data is not a source.
- **Secondary is weaker.** A claim traced only to an AI synthesis rests on that synthesis's reading of the source. Look for the primary when the claim matters to a decision.
- **Backfill on touch.** Existing decision records don't need retroactive linking in one pass. Any session that touches one adds links for the claims it can verify, so coverage grows with use.
- **Tags make evidence queryable.** Frontmatter tags let a session list every `[emerging]` claim when replication arrives, then run a reweave on the decisions that cited it.
- **Primary sources get their own doc.** When a session reads a primary source, it checks that the source has a doc in `research/`, not only an interpretation. [[vault-guide/research-paper-workflow]] covers how sources enter the vault.

## Common Failure

An AI session writes a confident rationale with claims like *"decades of validation"* that link to nothing. The decision reads well and cannot be checked, and when contrary evidence arrives, nobody can find the decisions that relied on the claim.
