---
title: Vault Review Protocol
id: vault-review-protocol
date: 2026-04-06
status: Active
tags: [protocol, vault-administration, maintenance]
---
# Vault Review Protocol

A vault review audits six dimensions of the vault and routes every unfixed finding to the ledger, never to a standalone report file. Report files go stale, while ledger tasks get triaged, closed, and archived with everything else.

## Trigger

- **Every quarter.**
- **After any gap in work longer than about a month.**
- **When the session start finds drift**, such as load paths in [[AGENTS]] that don't exist or a link count that is no longer zero.

## Steps

1. **Prepare.** Run the session start protocol and bring the link checker to zero ([[vault-guide/wikilink-discipline]]). If the ledger hasn't been triaged this quarter, run [[vault-guide/implementation-plan-triage]] in the same session.
2. **Audit the six dimensions** in the table below. When the environment supports subagents, run one read-only subagent per dimension in parallel, and have each return findings without editing anything.
3. **Rate each finding** with the severity rubric below.
4. **Split the findings into two batches** before touching anything. The mechanical batch holds fixes with one right answer; the decision batch holds anything that changes a rule, schema, or standing decision.
5. **Fix the mechanical batch** in this session: path fixes, duplicate deletion, README index updates, ignore-list pruning, and checkbox routing. Run the link checker after every move or deletion.
6. **Draft the decision batch in chat.** New decision records, schema changes, and style-guide exceptions wait for human approval under the review-before-write rule in [[vault-guide/decision-propagation-protocol]].
7. **Route what's left.** Append one `## Vault Review YYYY-MM-DD: Routed Items` section to [[prototype/implementation-plan]], with every unfixed finding as a task grouped by dimension, each naming the session type that resolves it.
8. **Close the session.** Update [[AGENTS]] only where the review changed Vault Structure, Standing Decisions, or Task-Specific Context Loading. Log the session and run `vault-lint.py` ([[vault-guide/session-logs]]).

## The Six Dimensions

| Dimension | Scope | What to check |
|---|---|---|
| A. Structure | Folder tree, READMEs, pointer files | The tree matches Vault Structure in [[AGENTS]]; every folder README lists its files; every load path in Task-Specific Context Loading exists; skill scripts are documented in their `SKILL.md`; secrets are ignored by version control. |
| B. Decisions | `decisions/` | Frontmatter follows [[decisions/_BASES_SCHEMA]]; supersession links are reciprocal; status values are consistent; every record named in [[AGENTS]] exists; no multi-line code blocks. |
| C. Writing discipline | Every folder except `archive/` and `journal/` | Tightening checklist violations: long paragraphs, `###` headings, slop words, meta-commentary, em-dash clusters, orphan checkboxes, missing frontmatter. |
| D. Drafts and ledger | `drafts/`, `prompts/`, `prototype/` | Duplicate or orphaned drafts with no ledger task; stale hand-over notes; ledger date and open counts; superseded tasks still open; weekly logs match their template. |
| E. Research and graph | `research/`, links vault-wide | `evidence-maturity` and `## Reweave Triggers` present; primary sources have their own docs; `_source-` files sit beside their clean doc; orphans and dead ends; `.link-check-ignore` entries are still forward references. |
| F. Lifecycle | `concepts/`, `ideas/`, `strategy/` | Concepts define and ideas propose; every idea has a `resolved-by` value; ideas older than a quarter get a decision; `session-history.md` and the weekly logs agree. |

## Severity Rubric

- **Critical.** A fresh session would act on wrong information, such as a load path that doesn't exist or a broken hard constraint.
- **High.** Drift that costs a future session real time, such as stale indexes, unrouted drafts, or hidden broken links.
- **Medium.** Accuracy debt with no immediate cost, such as stale counts or missing README rows.
- **Low.** Cosmetic issues, such as empty files, stray binaries, or frontmatter spelling.

## Rules

- **Findings go to the ledger.** Never write a standalone review or audit report file.
- **Subagents stay read-only.** Parallel auditors report findings; only the main session edits, after consolidating them.
- **Mechanical fixes don't need approval; decisions do.** If a fix has more than one reasonable answer, it belongs in the decision batch.
- **Archives are exempt.** Files under any `archive/` folder skip the writing-discipline audit.
- **Treat automated counts as leads.** Scans for slop words and meta-commentary flag false positives, because filenames and rule text quote the banned phrases. Paragraph and checkbox counts are usually accurate.
- **Route the human's items to the ledger too.** Never write into `prototype/human-task-list.md`.

## Common Failure

A review produces a long findings report that nobody reopens. Six months later the next review rediscovers the same problems, because none of them became a ledger task.
