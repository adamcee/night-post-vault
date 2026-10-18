#!/usr/bin/env python3
"""
Vault Link Checker: Extracts all [[wikilinks]] from vault files and reports
any that don't resolve to an actual note.

Rules:
- Skip wikilinks inside YAML frontmatter
- Skip wikilinks inside code blocks (``` or ~~~ fenced)
- Skip wikilinks inside inline code (`backticks`)
- Handle aliased links: [[path|display text]] checks the path portion
- Handle escaped pipes in tables: [[path\\|display text]]
- Handle heading links: [[path#heading]] checks the path portion
- Handle block links: [[path#^block-id]] checks the path portion
- Resolve links vault-root-relative ([[decisions/product/PDR-P001-name]])
  or by bare filename ([[PDR-P001-name]]), case-insensitively, like Obsidian
- Non-markdown files (images, PDFs) resolve when the link names the extension
- Don't check files inside EXEMPT_DIRS (archive/, journal/) or untouched
  originals (_source-*.md); they still count as link targets
- Skip targets listed in .link-check-ignore (vault root)

Vault root: the nearest directory containing AGENTS.md, searched upward from
the current directory first, then from this script's folder.

Ignore file (.link-check-ignore):
  One pattern per line. # comments. Blank lines ignored.
  Exact match:   prototype/specs/future-spec
  Prefix match:  research/interviews/*
  Case-insensitive matching (matches Obsidian behavior).

Usage:
  python3 vault-link-check.py                    # Check all vault files
  python3 vault-link-check.py path/to/file.md    # Check specific file(s)
  python3 vault-link-check.py --json             # Output as JSON for scripting

Exit codes:
  0 = all links resolve
  1 = broken links found
  2 = no vault root found, or none of the given files exist
"""

import json
import os
import re
import sys
from pathlib import Path

# Folders whose files are never checked. Archives hold retired docs; journal/
# is human-only, so an agent can't fix links there. Both remain link targets.
EXEMPT_DIRS = {"archive", "journal"}
# Untouched originals kept beside a cleaned doc by the ingestion gate. They
# are never edited, so their links are never checked.
EXEMPT_FILE_PREFIXES = ("_source-",)


def find_vault_root():
    """Walk up from the current directory, then from this script, to the folder holding AGENTS.md."""
    starts = [Path.cwd()]
    if "__file__" in globals():
        starts.append(Path(__file__).resolve().parent)
    for start in starts:
        d = start.resolve()
        while True:
            if (d / "AGENTS.md").exists():
                return d
            if d == d.parent:
                break
            d = d.parent
    return None


VAULT_ROOT = find_vault_root()

# Regex to find [[wikilinks]], including aliased [[path|text]] forms
WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')

IGNORE_FILENAME = '.link-check-ignore'


def load_ignore_patterns(ignore_path):
    """Load ignore patterns from .link-check-ignore file.

    Returns (exact_set, prefix_list) where:
    - exact_set: set of lowercased exact target strings to ignore
    - prefix_list: list of lowercased prefix strings (from patterns ending in *)
    """
    exact = set()
    prefixes = []
    if not ignore_path.exists():
        return exact, prefixes
    with open(ignore_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line.endswith('*'):
                prefixes.append(line[:-1].lower())  # "foo/*" keeps the trailing /
            else:
                # Strip trailing slash so "architecture/" matches target "architecture"
                exact.add(line.rstrip('/').lower())
    return exact, prefixes


def is_ignored(target, ignore_exact, ignore_prefixes):
    """Check if a target matches any ignore pattern."""
    t = target.lower()
    if t in ignore_exact:
        return True
    for prefix in ignore_prefixes:
        if t.startswith(prefix):
            return True
    return False


def is_exempt(rel_path):
    """True if the file sits inside an exempt folder or is an untouched original."""
    parts = Path(rel_path).parts
    return (any(part in EXEMPT_DIRS for part in parts[:-1])
            or parts[-1].startswith(EXEMPT_FILE_PREFIXES))


def _walk(root):
    """Yield vault-relative paths (forward slashes) of all files, skipping hidden dirs."""
    for dirpath, dirs, filenames in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in filenames:
            if f.startswith('.'):
                continue
            rel = os.path.relpath(os.path.join(dirpath, f), root)
            yield rel.replace(os.sep, '/')


def get_all_md_files(root):
    """Get all .md files in the vault, excluding hidden dirs."""
    return {rel for rel in _walk(root) if rel.endswith('.md')}


def get_attachment_files(root):
    """Get all non-markdown files (images, PDFs, ...), excluding hidden dirs."""
    return {rel for rel in _walk(root) if not rel.endswith('.md')}


def build_resolution_index(md_files, other_files=()):
    """Build a set of paths that wikilinks can resolve to.

    A wikilink [[foo/bar]] resolves if foo/bar.md exists.
    A wikilink [[foo/bar.md]] also resolves (strip the .md, check).
    Obsidian resolves case-insensitively and by basename alone.
    We match both behaviors. Attachments resolve by path or basename
    with their extension ([[assets/map.png]], [[map.png]]).
    """
    index = set()
    for rel_path in md_files:
        # Store without .md extension (how wikilinks reference notes)
        without_ext = rel_path[:-3] if rel_path.endswith('.md') else rel_path
        index.add(without_ext.lower())
        # Also store the basename without extension for short-form links
        index.add(os.path.basename(without_ext).lower())
    for rel_path in other_files:
        index.add(rel_path.lower())
        index.add(os.path.basename(rel_path).lower())
    return index


def extract_links_from_content(content):
    """Extract all wikilinks from file content, skipping frontmatter and code blocks.

    Returns list of (line_number, raw_link, target_path) tuples.
    target_path is the resolved path portion (before | alias, before # heading).
    """
    links = []
    lines = content.split('\n')
    in_frontmatter = False
    fence = None  # the fence marker (``` or ~~~) that opened the current code block

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        # Frontmatter detection
        if i == 1 and stripped == '---':
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped in ('---', '...'):
                in_frontmatter = False
            continue

        # Code block detection
        marker = stripped[:3]
        if marker in ('```', '~~~'):
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            continue
        if fence:
            continue

        # Strip inline code before searching for wikilinks
        line_no_code = re.sub(r'`[^`]+`', '', line)

        for match in WIKILINK_RE.finditer(line_no_code):
            raw = match.group(1)
            # Extract target path: strip alias (|text or \|text), heading (#), block ref (#^)
            # Obsidian escapes | as \| inside table cells
            target = re.split(r'\\?\|', raw)[0].split('#')[0].strip()
            # Skip empty targets ([[#heading]] links point into the same note)
            if target:
                links.append((i, raw, target))

    return links


def check_file(filepath, resolution_index, ignore_exact=None, ignore_prefixes=None):
    """Check all wikilinks in a single file. Returns list of broken link dicts."""
    if ignore_exact is None:
        ignore_exact = set()
    if ignore_prefixes is None:
        ignore_prefixes = []

    broken = []
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    rel_path = os.path.relpath(filepath, VAULT_ROOT).replace(os.sep, '/')
    links = extract_links_from_content(content)

    for line_num, raw_link, target in links:
        # Strip trailing / for directory-style links
        clean_target = target.rstrip('/')
        # Also try with .md stripped if someone wrote [[foo.md]]
        if clean_target.endswith('.md'):
            clean_target = clean_target[:-3]

        if is_ignored(clean_target, ignore_exact, ignore_prefixes):
            continue

        if clean_target.lower() not in resolution_index:
            broken.append({
                'file': rel_path,
                'line': line_num,
                'link': raw_link,
                'target': target,
            })

    return broken


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = [a for a in sys.argv[1:] if a.startswith('--')]
    if '--help' in flags or '-h' in args:
        print(__doc__)
        sys.exit(0)
    json_output = '--json' in flags

    if VAULT_ROOT is None:
        print("ERROR: Could not find vault root (no AGENTS.md in this or any parent directory)",
              file=sys.stderr)
        sys.exit(2)

    all_md_files = get_all_md_files(VAULT_ROOT)
    resolution_index = build_resolution_index(all_md_files, get_attachment_files(VAULT_ROOT))
    ignore_exact, ignore_prefixes = load_ignore_patterns(VAULT_ROOT / IGNORE_FILENAME)

    # Determine which files to check
    if args:
        targets = []
        for a in args:
            p = Path(a)
            if not p.is_absolute() and not p.exists():
                p = VAULT_ROOT / p
            if p.is_file():
                targets.append(str(p.resolve()))
            else:
                print(f"WARNING: {a} not found, skipping", file=sys.stderr)
        if not targets:
            print("No valid files to check.", file=sys.stderr)
            sys.exit(2)
    else:
        targets = [str(VAULT_ROOT / f) for f in sorted(all_md_files) if not is_exempt(f)]

    all_broken = []
    for filepath in targets:
        broken = check_file(filepath, resolution_index, ignore_exact, ignore_prefixes)
        all_broken.extend(broken)

    if json_output:
        print(json.dumps(all_broken, indent=2))
    else:
        if not all_broken:
            print(f"All links resolve. Checked {len(targets)} files.")
        else:
            print(f"Found {len(all_broken)} broken link(s) in {len(targets)} files:\n")
            for b in all_broken:
                print(f"  {b['file']}:{b['line']}  [[{b['link']}]]  → target not found: {b['target']}")

    sys.exit(1 if all_broken else 0)


if __name__ == '__main__':
    main()
