---
title: Wikilink Discipline
id: wikilink-discipline
date: 2026-04-06
status: Active
tags: [protocol, vault-administration, linking]
---
# Wikilink Discipline

Every reference to another vault document is a `[[wikilink]]` to its canonical location, written as a vault-root-relative path such as `[[vault-guide/reweave-protocol]]`. Links let humans and AI sessions navigate by following connections instead of running full-text searches.

A link costs seconds to add. A missing link costs a search every time someone needs that connection, and the [[vault-guide/reweave-protocol]] cannot find a reference that is only prose.

## Trigger

Apply it whenever a session writes or edits a vault document. Run the verification step whenever a session creates, edits, or moves links or files.

## Steps

1. **Link what the document references.**
    - **Empirical claims** link to the supporting research doc ([[vault-guide/research-traceability]]).
    - **Decision references** link to the specific ADR or PDR.
    - **Terms** link to the concept note in `concepts/` that defines them.
    - **Other cross-references** link to the canonical doc, not a vague description of it.
2. **Use the full path from the vault root.** Write `[[decisions/technical/ADR-T001-name]]`, not `[[ADR-T001-name]]`, so the link stays unambiguous when two folders hold similar names.
3. **Verify every target.** Run `python3 .claude/skills/vault-links/vault-link-check.py <files>` on the files you changed, or with no arguments for the whole vault.
4. **Fix each broken link.** Correct the path, link the nearest real note (often a folder's `README`), or record an intended forward reference in `.link-check-ignore`.

## Checking Links Without Python

Users without Python can verify links by hand. For each link, confirm a file exists at `<target>.md` from the vault root, using the file explorer, `ls`, or a search for the filename.

In Obsidian, a link to a missing note renders in a faded color, and the Obsidian CLI `unresolved` command lists them all.

## Forward References

A link to a note that doesn't exist yet is allowed when it is intended. Flag it inline, as in `[[strategy/pricing]] (does not exist yet; create it after the pricing decision)`, and add the target to `.link-check-ignore` at the vault root.

The ignore file holds one target per line, `#` comments, and a `# Last triaged: YYYY-MM-DD` line near the top. Each vault review removes entries that now exist or are no longer wanted, then updates that date ([[vault-guide/vault-review-protocol]]).

## Rules

- **Don't link a doc to itself.**
- **Don't link common words** that happen to match a filename.
- **Don't link inside YAML frontmatter or code blocks.** Tools don't resolve them there.
- **Link a folder through its README.** A folder path doesn't resolve as a note, so write `[[decisions/technical/README|decisions/technical/]]`.
- **Escape the alias pipe inside tables.** Write `[[path/note\|label]]`, or the table breaks at the pipe.
- **A broken link is worse than none.** It claims a connection that doesn't exist. Once the checker reports zero, any new result is a regression to fix in the same session.
- **Move files with a tool that rewrites links.** Use the Obsidian move command (in the app, the CLI `move`, or an MCP move tool). A shell `mv`, `git mv`, or copy-then-delete leaves every link pointing at the old path; the repair is in [[vault-guide/ingestion-gate]].
- **The ignore file is not a hiding place.** It holds only intended forward references, never broken links someone didn't want to fix.

## Common Failure

AI sessions mention other work in prose, such as *"as the strategy doc says,"* without a link. The reference never appears in backlinks or the graph, so reweave and traceability both miss it.
