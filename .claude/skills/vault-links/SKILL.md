---
name: vault-links
description: "Checks that every [[wikilink]] in the vault resolves, and adds wikilinks to plain-text mentions of note names. Use after creating or editing wikilinks, after moving or renaming notes, after batch-adding documents, during vault maintenance, or when the user says 'check links', 'broken links', or 'auto-link'."
---

# Vault Linking Tools

Two Python 3 scripts keep the vault's wikilinks healthy: `vault-link-check.py` finds links that point nowhere, and `vault-autolink.py` turns plain-text mentions of note names into links. Both find the vault root by walking up from the current directory to the folder holding `AGENTS.md`, so run them from anywhere inside the vault.

## Link Checker (`vault-link-check.py`)

The checker reports every `[[wikilink]]` whose target doesn't exist. It needs only the Python standard library.

```bash
python3 .claude/skills/vault-links/vault-link-check.py                  # every file in the vault
python3 .claude/skills/vault-links/vault-link-check.py path/to/file.md  # specific files
python3 .claude/skills/vault-links/vault-link-check.py --json           # machine-readable output
```

| Exit code | Meaning |
|---|---|
| 0 | All links resolve. |
| 1 | Broken links found; each is listed as `file:line [[link]] → target not found`. |
| 2 | No `AGENTS.md` found above the current directory, or none of the named files exist. |

**How links resolve.** A link resolves when its target matches a note's vault-root-relative path (`[[decisions/product/PDR-P001-name]]`) or bare filename (`[[PDR-P001-name]]`), ignoring case. Aliases (`[[path|text]]`), escaped table pipes (`[[path\|text]]`), heading refs (`[[path#Heading]]`), block refs (`[[path#^id]]`), and attachments named with their extension (`[[map.png]]`) all work.

**What it skips.** Links inside frontmatter, fenced code blocks, and inline code are ignored. Files in `archive/` and `journal/` folders and untouched originals (`_source-*.md`) aren't checked, but links pointing into them still resolve. Change `EXEMPT_DIRS` or `EXEMPT_FILE_PREFIXES` at the top of the script to adjust this.

**Ignore file.** `.link-check-ignore` at the vault root lists intentional forward references, one per line. A line is an exact target (`prototype/specs/future-spec`) or a prefix ending in `*` (`research/interviews/*`), matched without case; `#` starts a comment.

**When to run it:**
- After creating or editing wikilinks, on the files you touched (the Post-Task Completion Gate requires this).
- After moving or renaming notes with plain `mv`.
- During any vault maintenance session, on the whole vault.

**Fixing a broken link.** Correct the typo, point the link at the nearest real note (often a folder `README`), or add the target to `.link-check-ignore` if the note is planned. Once the vault reports zero broken links, treat any new one as a regression to fix in the same session.

**Tests.** `test_vault_link_check.py` holds 46 unit tests that build throwaway vaults in a temp directory:

```bash
python3 .claude/skills/vault-links/test_vault_link_check.py -v
```

## Auto-Linker (`vault-autolink.py`)

The auto-linker finds plain-text mentions of note filenames and frontmatter `aliases`, then wraps them in `[[full/relative/path]]` or `[[path|matched text]]`. It matches strings mechanically, so always preview and read the diff before applying.

```bash
pip3 install pyyaml                                            # one-time
python3 .claude/skills/vault-links/vault-autolink.py preview   # show the diff, write nothing (default)
python3 .claude/skills/vault-links/vault-autolink.py apply     # write the changes
git diff                                                       # review, then revert any bad link
```

| Exit code | Meaning |
|---|---|
| 0 | Preview shown, changes applied, or nothing to change. |
| 1 | Unknown mode, `pyyaml` missing, or no `AGENTS.md` found. |

**What it never touches.** It never edits or links to `journal/`, `session-history.md`, `prototype/implementation-logs/`, `prototype/human-task-list.md`, any `archive/` folder, or `_source-*.md` originals. Within a file it skips frontmatter, code, headings, existing wikilinks, URLs, markdown links, file paths, and self-links.

**Configuration** (constants at the top of the script):
- `SKIP_NAMES`: note names never linked. The defaults are generic filenames such as `README`, `index`, `AGENTS`, and `CONSTITUTION`. Add any note name that is also a common word in your prose.
- `MIN_NAME_LENGTH`: names shorter than this (default 4) are never linked.
- `SKIP_PATHS`, `SKIP_DIR_NAMES`, `SKIP_FILE_PREFIXES`: paths the linker never edits or targets.
- `FIRST_MENTION_ONLY`: link only the first mention of each note per file (default `True`).

**Expect false positives.** A note whose filename is a common word (a character named after an object, a concept named with an everyday verb) gets linked wherever that word appears. Reject those in review and add the name to `SKIP_NAMES`.

**When to run it:** after batch-adding documents, after a research import, or as periodic maintenance. Run `vault-link-check.py` afterward.

## Without Python

Search for `\[\[([^\]|#]+)` with your grep tool to list link targets, then confirm each target exists with a file search for `<target>.md`. If Obsidian is open, its CLI (`obsidian unresolved`) or the Unresolved links view does the same check.
