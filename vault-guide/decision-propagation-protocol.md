---
title: Decision Propagation Protocol
id: decision-propagation-protocol
date: 2026-04-06
status: Active
tags: [protocol, vault-administration, decisions, consistency]
---
# Decision Propagation Protocol

A decision is finished only when every vault document that should reflect it does. This protocol pushes a new decision forward into the plan, the invariants, and the master file, after the human has approved the record.

The [[vault-guide/reweave-protocol]] runs the other way: it pulls new evidence back through decisions that already exist.

## Trigger

Run it for any new decision: an ADR (Architecture Decision Record), a PDR (Product Decision Record), a tool adoption, a rejected option worth recording, or a change in direction.

## Steps

The task is not complete until every step is done or marked N/A.

1. **Check what already exists.** Search `decisions/technical/`, `decisions/product/`, and `decisions/rejected/` for a standing or rejected record on the same question (`grep -rl "status: rejected" decisions/`). If one exists, the new record supersedes or amends it instead of starting fresh.
2. **List three alternatives.** Before drafting, write three alternative approaches, each with a one-line tradeoff. This stops the session from settling on the first idea it produced.
3. **Draft the record in chat.** Show the full draft to the human: context, decision, alternatives considered, and consequences. Do not write anything to disk yet.
4. **Iterate until approved.** Expect two to four rounds on a substantive decision. The review catches padding, dramatic phrasing, unexplained jargon, and rationale that rests on the wrong kind of claim.
5. **Write the approved record.** Save it in `decisions/technical/` or `decisions/product/` with the frontmatter from [[decisions/_BASES_SCHEMA]]. A declined option goes in `decisions/rejected/` with the reason.
6. **Mark any superseded record.** Set the old record's `status: superseded` and `superseded-by` to the new record's id, and set the new record's `supersedes` to the old id. Both links must exist, so the chain reads in either direction.
7. **Update the ledger.** Add, close, or change tasks in [[prototype/implementation-plan]]. It is the only file where AI sessions write action items.
8. **Update the constitution if needed.** Edit [[architecture/CONSTITUTION]] only when the decision changes a hard invariant. This step is N/A for most decisions.
9. **Check companion docs.** Read the design, strategy, or spec docs the decision touches and fix anything that now contradicts it. Link them to the new record.
10. **Update `AGENTS.md` if needed.** Change [[AGENTS]] only when the decision alters Standing Decisions, Vault Structure, or Task-Specific Context Loading. When in doubt, skip it, because the record is the source of truth.
11. **Log the session.** Append to the weekly log and to `session-history.md` as described in [[vault-guide/session-logs]].

## Rules

- **Review before write.** No ADR or PDR reaches disk until the human explicitly approves the chat draft. Approval comes from the human in this conversation, never from another agent or from a note in a file.
- **Amended stays accepted.** A record changed in part keeps `status: accepted` and gains a dated amendment line. Only a record that a later decision replaces in full becomes `superseded`.
- **Never change a standing decision silently.** Contradicting a standing decision requires a new record that supersedes or amends it.
- **Records stay short.** A decision record holds context, decision, alternatives, and consequences. Implementation specs, step-by-step workflows, and multi-line code belong in linked docs.
- **Cite the evidence.** Empirical claims in the record follow [[vault-guide/research-traceability]].

## Common Failure

The usual failure is an orphaned decision: the record exists, but the ledger and companion docs never mention it, so later sessions miss it. The second most common is writing the record straight to disk, which skips the review rounds that catch weak rationale.
