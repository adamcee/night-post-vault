---
name: vault-maintenance
description: "Audits the health and integrity of the vault: session-close lint, broken wikilinks, orphaned notes, dead ends, writing-discipline and reweave gaps, and tag consistency. Trigger at every session close (vault-lint.py), or when tasked with 'vault maintenance', 'vault review', 'checking links', 'cleaning up the vault', or 'aligning tags'."
---

# Vault Maintenance

This skill runs vault audits with three Python 3 scripts plus the Obsidian CLI, and falls back to plain file search when neither is available. The scripts need only the Python standard library and find the vault root by walking up from the current directory to the folder holding `AGENTS.md`.

| Script | Job | Writes files? |
|---|---|---|
| `vault-lint.py` | Session-close checks on `AGENTS.md` and the logs. | No |
| `vault-review-scan.py` | Writing-discipline and reweave gap scan. | No |
| `tag-aligner.py` | Bulk frontmatter and footer tag fixes. | Yes, unless `--dry-run` |

Broken-link checks and auto-linking live in the `vault-links` skill (`vault-link-check.py`, `vault-autolink.py`).

## Vault Lint (`vault-lint.py`)

Run this at every session close, as the Post-Task Completion Gate in `AGENTS.md` requires. It catches the mistakes sessions make most often when they log their work.

```bash
python3 .claude/skills/vault-maintenance/vault-lint.py
python3 .claude/skills/vault-maintenance/vault-lint.py --allow-edits   # after an intentional log correction
```

It fails when any of these hold:
- `AGENTS.md` exceeds 40,000 bytes. Some agent tools read files in fixed-size chunks and silently drop the rest, so rules at the end of a long `AGENTS.md` go unread.
- `AGENTS.md` holds a session entry or a `## YYYY-MM-DD` heading. Session entries belong in the logs.
- A line in `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md` exceeds 1,000 characters, or a line in `session-history.md` exceeds 2,000. Edit tools mangle very long lines.
- `session-history.md` has a heading other than `## YYYY-MM-DD` (including the template's `## [YYYY-MM-DD]` placeholder), repeats a date, has dates out of order, or ends on a future date.
- A line under the last date heading isn't in the form `- (agent, session type) what changed`. Older sections aren't checked, since append-only logs keep entries as written.
- A weekly log in `prototype/implementation-logs/YYYY-Www.md` has a dated heading outside its ISO week, or the current log has a `## ` heading that doesn't start with a date.
- The week of the last `session-history.md` date has no log, or that log has no `## YYYY-MM-DD` section for the date.
- Lines were removed from `session-history.md` or the current weekly log since the last commit (`git diff HEAD`), or a past week's log changed at all. Pass `--allow-edits` when a correction is intentional.

Exit code 0 means clean, 1 lists each failure, and 2 means no `AGENTS.md` was found. Log checks are skipped with a note when there are no weekly logs, and append-only checks are skipped when the vault isn't a git repository with commits.

**Manual fallback.** Check the file size (`wc -c AGENTS.md`), list the headings (`grep -n '^## ' session-history.md`) and confirm they are unique and ascending, and compare the last date with the current weekly log's headings. Before closing, run `git diff session-history.md` and confirm every changed line starts with `+`.

## Vault Review Scan (`vault-review-scan.py`)

This read-only scan scores each markdown file on tightening-checklist heuristics and prints the worst offenders, totals, and lists of files with no frontmatter, missing fields, or orphan checkboxes. Use it during a vault review; its findings go to `prototype/implementation-plan.md`, never to a standalone report.

```bash
python3 .claude/skills/vault-maintenance/vault-review-scan.py              # default folders + root files
python3 .claude/skills/vault-maintenance/vault-review-scan.py decisions    # named folders only
python3 .claude/skills/vault-maintenance/vault-review-scan.py --top 40     # show 40 rows (default 25)
python3 .claude/skills/vault-maintenance/vault-review-scan.py --reweave    # research reweave gaps; add folders to narrow
```

**Columns:** `h3` (`###` headers), `slop` (banned words), `meta` (meta-commentary such as "this section"), `lp` (paragraphs over two sentences), `em` (paragraphs with more than one em-dash), `html`, `nofm` (no frontmatter), `fmmiss` (missing required fields), and `cb` (orphan checkboxes). Paragraph and checkbox counts are reliable. Slop and meta counts are leads, since wikilink filenames and rule text that quotes banned words trip them.

**`--reweave`** lists research docs missing `## Reweave Triggers` or an `evidence-maturity` frontmatter field. It also lists weakened or invalidated triggers whose target never mentions the source doc, because the Reweave Protocol puts a dated note in the target and backlinks don't carry the verdict.

**Configuration** (constants at the top of the script):
- `DEFAULT_DIRS`: `architecture`, `concepts`, `decisions`, `ideas`, `prototype`, `research`, `strategy`, `vault-guide`. `ROOT_FILES` adds `AGENTS.md`, the pointer files, and `session-history.md`.
- `EXCLUDE_DIRS`: `journal`, `archive`, and `drafts` at any depth. Untouched `_source-*.md` originals are skipped too.
- `CB_ALLOWED`: files where checkboxes belong, by default `prototype/implementation-plan.md`, `prototype/human-task-list.md`, and `AGENTS.md` (protocol checklists). `CB_ALLOWED_PREFIXES` adds `vault-guide/` for protocol pages.
- `REQUIRED_FIELDS`: frontmatter fields every doc needs (default `date`, `tags`). Root files and READMEs need no frontmatter.
- `REWEAVE_DIRS`, `REWEAVE_HEADING`, `MATURITY_FIELD`: settings for `--reweave`.

Exit code 0 after the report (findings are leads, not failures), 2 when no vault root is found or `--top` lacks a number.

**Manual fallback.** Grep for `^### ` headings, the banned phrases in the style guide, and `^\s*- \[ \]` outside the two task files. For reweave gaps, run `grep -L "## Reweave Triggers" -r research/` and `grep -L "evidence-maturity:" -r research/`.

## Tag Aligner (`tag-aligner.py`)

This script standardizes tags across one folder. It rewrites the frontmatter `tags` field to the bracketed form (`tags: [a, b]`, converting comma lists and block lists), adds missing `--target-tags`, and appends missing `--footer-tags` as `#tag` lines at the end of the body.

```bash
python3 .claude/skills/vault-maintenance/tag-aligner.py research --target-tags research --dry-run   # preview
python3 .claude/skills/vault-maintenance/tag-aligner.py research --target-tags research             # write
python3 .claude/skills/vault-maintenance/tag-aligner.py concepts --footer-tags concept
```

| Flag | Effect |
|---|---|
| `<directory>` | Folder to process, recursively. Required. |
| `--target-tags a b` | Tags to add to the frontmatter array if missing. |
| `--footer-tags a b` | Tags to append as `#a` and `#b` if missing. |
| `--dry-run` | Print the files that would change and write nothing. |

It only edits frontmatter for target tags, so a body line starting with `tags:` is safe. It never edits `journal/`, `archive/`, or `implementation-logs/` folders, `session-history.md`, or `human-task-list.md`. Always run `--dry-run` first and review `git diff` after a real run. Add new tags to the shared tag list in `decisions/_BASES_SCHEMA.md` before using them.

**Manual fallback.** Find files with unbracketed tags with `grep -rn '^tags: [^[]' <folder>` and fix each one with your edit tool.

## Graph Checks

Use the Obsidian CLI for graph queries when the project uses Obsidian and the CLI is installed (for example `/Applications/Obsidian.app/Contents/MacOS/obsidian` on macOS). It understands the vault's internal link graph, aliases, and moved files.

```bash
obsidian unresolved        # broken links
obsidian orphans           # notes with no incoming links
obsidian deadends          # notes with no outgoing links
obsidian tags sort=count   # tag distribution, to spot near-duplicates
```

Without the CLI, use `vault-link-check.py` for broken links. Otherwise degrade to native file search (`grep`, `glob`):
- **Broken links:** grep for `\[\[([^\]|#]+)` to list link targets, then confirm each exists with a file search.
- **Orphans:** list every `.md` file, then grep for each filename inside `[[ ]]` across the vault. This is slow, so run it only on small vaults or when the user asks.
- **Tags:** grep for `^tags:` and compare spellings.

## Maintenance Operations

1. **Broken links.** Fix the typo, point the link at the nearest relevant note (often a folder `README.md`), or add an intended forward link to `.link-check-ignore`. Ask the user if the missing note should be created.
2. **Orphaned notes.** If a note is obsolete, move it to the nearest `archive/` folder with a tool that rewrites links. If it is valid, link it from a logical parent such as the folder `README.md`.
3. **Dead ends.** Read the note and add `[[wikilinks]]` to the concepts, decisions, or research it depends on.
4. **Tag consolidation.** Merge near-duplicate tags into the canonical list in `decisions/_BASES_SCHEMA.md`, by hand or with `tag-aligner.py`.
5. **Writing discipline.** Run `vault-review-scan.py`, fix the top offenders or route them to the ledger, and run `vault-lint.py` before closing the session.
