---
title: Vault Design Philosophy
id: vault-design-philosophy
date: 2026-04-06
status: Active
tags: [documentation, vault-administration, design-philosophy]
---
# Vault Design Philosophy

*A human reference for why the vault is organized this way. AI sessions don't need to load it at start.*

## Why the Vault Exists

The vault is the project's memory for humans and AI. Without it, each AI session starts fresh, repeats old questions, loses track of rejected alternatives, and drifts from standing decisions.

`AGENTS.md` is the entry point. It tells a fresh session what the project is, what's been decided, what's off-limits, and where everything lives.

## Design Principles

1. **Decisions are first-class objects.** Each important decision has its own doc (ADR or PDR).
2. **Research is traceable, not decorative.** Empirical claims in ADRs link back to specific vault research docs.
3. **Forward propagation + backward reweave.** New decisions push forward into plans; new research forces backward checks of existing decisions.
4. **AGENTS.md is a routing document, not an encyclopedia.**
5. **Wikilinks are structural.** Links let humans and AI agents navigate by following connections.
6. **Ideas have a home.** The `ideas/` directory captures raw product and technical ideas before they become decisions.

## Directory Structure Rationale

- **strategy/** and **decisions/** are separate because strategy states what you want, while decisions record what you chose.
- **concepts/** contains atomic definitions of key terms. It doesn't propose anything new.
- **ideas/** captures raw proposals until they are promoted, rejected, or absorbed.
- **research/** is evidence, not commitment.
- **architecture/** contains the system design docs, which are downstream of decisions.
- **prototype/** (or `src/`) contains implementation artifacts, downstream of architecture.

The flow: Research → Decisions → Architecture → Implementation.

## Protocols Summary

| Protocol | Direction | Trigger | Purpose |
|---|---|---|---|
| [[vault-guide/decision-propagation-protocol\|Decision Propagation]] | Forward | A new decision | Review the record in chat, then push it into the plan, invariants, and `AGENTS.md`. |
| [[vault-guide/reweave-protocol\|Reweave]] | Backward | New research, feedback, or an outside event | Check whether existing decisions still hold and record each verdict. |
| [[vault-guide/research-traceability\|Research Traceability]] | Linking | Writing or editing a decision, strategy, or design doc | Tie each empirical claim to a vault source with a maturity tag. |
| [[vault-guide/wikilink-discipline\|Wikilink Discipline]] | Linking | Any vault edit or file move | Link references to their canonical docs and keep broken links at zero. |
| [[vault-guide/ingestion-gate\|Ingestion Gate]] | Intake | Any AI-generated content | Stage it in `drafts/` and promote it only after tightening. |
| [[vault-guide/research-paper-workflow\|Research Paper Workflow]] | Intake | A new external source | Hold sources in a reference manager, literature notes, and select full texts. |
| [[vault-guide/session-logs\|Session Logs]] | Record | End of any session that changed the vault | Append to the history file and the weekly log. |
| [[vault-guide/implementation-plan-triage\|Plan Triage]] | Maintenance | About 200 open items, a major change in direction, or quarterly | Close done and stale tasks without reprioritizing. |
| [[vault-guide/vault-review-protocol\|Vault Review]] | Maintenance | Quarterly or after a long gap | Audit six dimensions and route findings to the ledger. |