#!/usr/bin/env python3
"""
Vault Auto-Linker: Finds plain-text mentions of vault note names
and replaces them with [[wikilinks]].

Rules:
- Skip self-links
- Skip YAML frontmatter
- Skip code blocks (``` or ~~~ fenced)
- Skip headings
- Skip inline code (`backticks`)
- Skip text already inside [[wikilinks]], URLs, and markdown links
- Skip names in SKIP_NAMES, date-pattern names (YYYY-MM-DD), and names
  shorter than MIN_NAME_LENGTH
- Never edit files under SKIP_PATHS (human-only, append-only, archived) or
  untouched originals (_source-*.md), and never link to them
- Don't link inside file paths (preceded by / or . or followed by .md)
- Use the full vault-root-relative path: [[decisions/product/PDR-P001-name]]
- Match whole names only: a hyphen or word character on either side blocks
  the match, so "plan" never links inside "plan-b"
- With FIRST_MENTION_ONLY, link only the first mention of each note per file

Vault root: the nearest directory containing AGENTS.md, searched upward from
the current directory first, then from this script's folder.

Usage:
  python3 vault-autolink.py preview   # Show diffs without writing (default)
  python3 vault-autolink.py apply     # Write changes to files

Always preview first, then review `git diff` after applying.

Exit codes:
  0 = success (preview shown, or changes applied, or nothing to change)
  1 = unknown mode, missing pyyaml, or no vault root found

Requires: pip install pyyaml
"""

import os, re, difflib, sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: vault-autolink.py needs pyyaml. Install it with: pip3 install pyyaml")
    sys.exit(1)

# --- Configuration -----------------------------------------------------------

# Note names never auto-linked: generic filenames and pointer files. Matching
# is exact and case-sensitive. Add any note name that is also a common word in
# your vault's prose.
SKIP_NAMES = {
    "README", "readme", "index", "Index",
    "AGENTS", "CLAUDE", "GEMINI",
    "CONSTITUTION", "template", "notes", "todo",
}

# Names shorter than this are never auto-linked.
MIN_NAME_LENGTH = 4

# Vault-relative folders and files the linker never edits and never links to.
# journal/ is human-only, the logs and human task list are append-only or
# human-owned, and archive/ folders (at any depth) hold retired docs.
SKIP_PATHS = {
    "journal/",
    "session-history.md",
    "prototype/implementation-logs/",
    "prototype/human-task-list.md",
}
SKIP_DIR_NAMES = {"archive"}

# Untouched originals kept beside a cleaned doc by the ingestion gate.
SKIP_FILE_PREFIXES = ("_source-",)

# Link only the first plain-text mention of each note in a file (the usual
# wiki convention). Set to False to link every mention.
FIRST_MENTION_ONLY = True

# -----------------------------------------------------------------------------

# Skip date-pattern filenames (YYYY-MM-DD)
DATE_PATTERN = re.compile(r'^\d{4}-\d{2}-\d{2}$')

# YAML frontmatter at the top of a file
FRONTMATTER_RE = re.compile(r'\A---[ \t]*\n(.*?)\n(?:---|\.\.\.)[ \t]*(?:\n|\Z)', re.S)


def find_vault_root():
    """Walk up from the current directory, then from this script, to the folder holding AGENTS.md."""
    for start in (Path.cwd(), Path(__file__).resolve().parent):
        d = start.resolve()
        while True:
            if (d / "AGENTS.md").exists():
                return d
            if d == d.parent:
                break
            d = d.parent
    return None


VAULT_ROOT = find_vault_root()
if VAULT_ROOT is None:
    print("ERROR: Could not find vault root (no AGENTS.md in this or any parent directory)")
    sys.exit(1)


def is_skipped(rel):
    """True if the vault-relative path is one the linker must not edit or target."""
    if any(rel == p or (p.endswith('/') and rel.startswith(p)) for p in SKIP_PATHS):
        return True
    parts = rel.split('/')
    if any(part in SKIP_DIR_NAMES for part in parts[:-1]):
        return True
    return parts[-1].startswith(SKIP_FILE_PREFIXES)


def get_all_md_files():
    """Get all .md files in the vault, excluding hidden dirs and skipped paths."""
    files = []
    for root, dirs, filenames in os.walk(VAULT_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in filenames:
            if f.endswith('.md'):
                path = Path(root) / f
                if not is_skipped(path.relative_to(VAULT_ROOT).as_posix()):
                    files.append(path)
    return sorted(files)


def usable_name(name):
    """True if a note name or alias is specific enough to auto-link."""
    return (isinstance(name, str)
            and len(name) >= MIN_NAME_LENGTH
            and name not in SKIP_NAMES
            and not DATE_PATTERN.match(name))


def build_index(files):
    """Build index: note_name -> relative_path (without .md).

    Skips: generic names, date patterns, empty files.
    For duplicate names, prefers the shorter path.
    Also extracts YAML frontmatter aliases.
    """
    index = {}
    aliases = {}
    for f in files:
        note_name = f.stem
        rel_no_ext = f.relative_to(VAULT_ROOT).as_posix()[:-3]
        if f.stat().st_size <= 1:
            continue
        if usable_name(note_name):
            if note_name not in index or len(rel_no_ext) < len(index[note_name]):
                index[note_name] = rel_no_ext
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                content = fh.read()
            m = FRONTMATTER_RE.match(content)
            if m:
                fm = yaml.safe_load(m.group(1))
                if isinstance(fm, dict) and fm.get('aliases'):
                    found = fm['aliases']
                    if isinstance(found, str):
                        found = [found]
                    for alias in found:
                        if usable_name(alias):
                            aliases[alias] = rel_no_ext
        except (OSError, UnicodeDecodeError, yaml.YAMLError):
            pass
    return index, aliases


def process_file(filepath, index, aliases):
    """Process a single file, adding wikilinks where appropriate.

    Returns (new_content, original) if changes were made, else (None, None).
    """
    rel = filepath.relative_to(VAULT_ROOT).as_posix()
    self_path = rel[:-3]
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.split('\n')
    result_lines = []
    in_frontmatter = False
    fence = None
    # Notes already linked in this file count as mentioned
    linked = {m.group(1).split('|')[0].split('#')[0].strip().lower()
              for m in re.finditer(r'\[\[([^\]]+)\]\]', content)}
    for i, line in enumerate(lines):
        stripped = line.strip()
        if i == 0 and stripped == '---':
            in_frontmatter = True
            result_lines.append(line)
            continue
        if in_frontmatter:
            if stripped in ('---', '...'):
                in_frontmatter = False
            result_lines.append(line)
            continue
        marker = stripped[:3]
        if marker in ('```', '~~~'):
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            result_lines.append(line)
            continue
        if fence or stripped.startswith('#'):
            result_lines.append(line)
            continue
        line = apply_links_to_line(line, index, aliases, self_path, linked)
        result_lines.append(line)
    new_content = '\n'.join(result_lines)
    if new_content != original:
        return new_content, original
    return None, None


def apply_links_to_line(line, index, aliases, self_path, linked=None):
    """Replace plain-text mentions with wikilinks in a single line.

    Protects: existing [[wikilinks]], inline `code`, URLs, markdown links.
    Skips: matches inside file paths (preceded by / or . or followed by .md).
    Processes longest names first to avoid partial matches.
    `linked` is the set of lowercased paths already linked in this file; with
    FIRST_MENTION_ONLY, a path in it is not linked again.
    """
    if linked is None:
        linked = set()
    protected = []
    for m in re.finditer(r'\[\[.*?\]\]', line):
        protected.append((m.start(), m.end()))
    for m in re.finditer(r'`[^`]+`', line):
        protected.append((m.start(), m.end()))
    for m in re.finditer(r'https?://[^\s\)>]+', line):
        protected.append((m.start(), m.end()))
    for m in re.finditer(r'\[[^\]]*\]\([^)]*\)', line):
        protected.append((m.start(), m.end()))

    all_names = {}
    all_names.update(aliases)
    all_names.update(index)
    sorted_names = sorted(all_names.items(), key=lambda x: len(x[0]), reverse=True)

    for name, path in sorted_names:
        if path == self_path:
            continue
        if FIRST_MENTION_ONLY and (path.lower() in linked or
                                   path.split('/')[-1].lower() in linked):
            continue
        pattern = r'(?<![\w-])(' + re.escape(name) + r')(?![\w-])'
        matches = list(re.finditer(pattern, line))
        if FIRST_MENTION_ONLY:
            # Process left to right so the first eligible mention wins
            order = matches
        else:
            # Right to left keeps earlier match offsets valid
            order = list(reversed(matches))
        for m in order:
            start, end = m.start(), m.end()
            if any(ps <= start < pe or ps < end <= pe for ps, pe in protected):
                continue
            if start > 0 and line[start - 1] in '/.':
                continue
            if end < len(line) and line[end:end + 3] == '.md':
                continue
            matched_text = m.group(1)
            path_basename = path.split('/')[-1]
            if matched_text == path_basename:
                replacement = f'[[{path}]]'
            else:
                replacement = f'[[{path}|{matched_text}]]'
            line = line[:start] + replacement + line[end:]
            shift = len(replacement) - (end - start)
            protected = [
                (ps + shift if ps > start else ps, pe + shift if pe > start else pe)
                for ps, pe in protected
            ]
            protected.append((start, start + len(replacement)))
            if FIRST_MENTION_ONLY:
                linked.add(path.lower())
                break
    return line


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
    if mode in ("-h", "--help"):
        print(__doc__)
        return
    if mode not in ("preview", "apply"):
        print(f"Unknown mode: {mode}. Use 'preview' or 'apply'.")
        sys.exit(1)

    files = get_all_md_files()
    index, aliases = build_index(files)
    print(f"Vault: {VAULT_ROOT}")
    print(f"Index: {len(index)} note names, {len(aliases)} aliases")

    changes = {}
    for f in files:
        new_content, original = process_file(f, index, aliases)
        if new_content is not None:
            rel = f.relative_to(VAULT_ROOT).as_posix()
            changes[rel] = (new_content, original)
    print(f"Files to change: {len(changes)}")

    if not changes:
        print("\nNo changes needed — vault is fully linked.")
        return

    if mode == "preview":
        for path in sorted(changes.keys()):
            new_content, original = changes[path]
            orig_lines = original.splitlines(keepends=True)
            new_lines = new_content.splitlines(keepends=True)
            diff = list(difflib.unified_diff(
                orig_lines, new_lines, fromfile=path, tofile=path, n=0))
            if diff:
                print(f"\n{'=' * 60}")
                print(f"FILE: {path}")
                for line in diff[2:]:
                    if line.startswith('@@') or line.startswith('-') or line.startswith('+'):
                        print(line if line.endswith('\n') else line + '\n', end='')
        print("\nPreview only. Run with 'apply' to write these changes.")
    else:
        for path in sorted(changes.keys()):
            new_content, _ = changes[path]
            full_path = VAULT_ROOT / path
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Updated: {path}")
        print(f"\nDone. {len(changes)} files updated. Review with `git diff`.")


if __name__ == '__main__':
    main()
