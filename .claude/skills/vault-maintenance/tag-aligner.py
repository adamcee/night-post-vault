#!/usr/bin/env python3
"""Tag Aligner: bulk tag standardization for the markdown files in one folder.

For every .md file under the given directory:
1. Rewrites the frontmatter `tags` field to the bracketed array format
   (`tags: a, b` and block lists both become `tags: [a, b]`).
2. Adds any --target-tags missing from that array.
3. Appends any --footer-tags missing from the end of the body as `#tag`.

Only the YAML frontmatter is touched for steps 1 and 2; files without
frontmatter get footer tags only. Files in SKIP_DIRS folders (human-only,
archived, append-only logs) and SKIP_FILES are never edited.

Usage:
    python3 .claude/skills/vault-maintenance/tag-aligner.py <directory> \\
        --target-tags tag1 tag2 --footer-tags tag1 tag2 [--dry-run]

Always run with --dry-run first, then check `git diff` after the real run.
Exit code 0 on success, 2 if the directory doesn't exist.
"""
import os
import re
import sys
import argparse

# Folder names never edited, at any depth.
SKIP_DIRS = {"journal", "archive", "implementation-logs"}
# File names never edited: append-only or human-owned.
SKIP_FILES = {"session-history.md", "human-task-list.md"}

FRONTMATTER_RE = re.compile(r'\A---[ \t]*\n(.*?\n)?---[ \t]*(\n|\Z)', re.S)


def parse_tag_list(text):
    """Split 'a, b' or '[a, b]' into a clean list of tags."""
    text = text.strip()
    if text.startswith('[') and text.endswith(']'):
        text = text[1:-1]
    return [t.strip().strip('\'"') for t in text.split(',') if t.strip()]


def align_frontmatter(fm, target_tags):
    """Return frontmatter text with tags in [a, b] form and target tags added."""
    lines = fm.split('\n')
    for i, line in enumerate(lines):
        m = re.match(r'^tags:[ \t]*(.*)$', line)
        if not m:
            continue
        value = m.group(1).strip()
        end = i + 1
        if value:
            tags = parse_tag_list(value)
        else:
            # Block list: "tags:" followed by "  - tag" lines
            tags = []
            while end < len(lines) and re.match(r'^\s*-\s+', lines[end]):
                tags.append(re.sub(r'^\s*-\s+', '', lines[end]).strip().strip('\'"'))
                end += 1
        for tt in target_tags:
            if tt not in tags:
                tags.append(tt)
        lines[i:end] = ['tags: [' + ', '.join(tags) + ']']
        return '\n'.join(lines)
    return fm


def align_tags(directory, target_tags, footer_tags, dry_run=False):
    """
    Standardizes YAML frontmatter tags to [bracket, array] format,
    ensures specific target tags are in the frontmatter,
    and appends Obsidian footer tags.
    """
    print(f"Aligning tags in {directory}...")
    changed = 0

    for root, dirs, files in os.walk(directory):
        dirs[:] = sorted(d for d in dirs if not d.startswith('.') and d not in SKIP_DIRS)
        for filename in sorted(files):
            if not filename.endswith('.md') or filename in SKIP_FILES:
                continue

            path = os.path.join(root, filename)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            # 1-2. Bracketed tag array with target tags, inside frontmatter only
            m = FRONTMATTER_RE.match(content)
            if m and m.group(1):
                fm = m.group(1)
                new_fm = align_frontmatter(fm, target_tags)
                content = content[:m.start(1)] + new_fm + content[m.end(1):]

            # 3. Add footer tags to bottom if missing
            for ft in footer_tags:
                if not re.search(r'(?<![\w#])#' + re.escape(ft) + r'(?![\w/-])', content):
                    content = content.rstrip() + f"\n\n#{ft}\n"

            if content != original_content:
                changed += 1
                if dry_run:
                    print(f"[DRY RUN] Would update {path}")
                else:
                    print(f"Updated {path}")
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)

    verb = "would change" if dry_run else "changed"
    print(f"Done. {changed} file(s) {verb}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Align vault tags in frontmatter and footers.")
    parser.add_argument("directory", help="Directory to process")
    parser.add_argument("--target-tags", nargs="*", default=[], help="Tags to ensure in frontmatter")
    parser.add_argument("--footer-tags", nargs="*", default=[], help="Obsidian tags to append to footer")
    parser.add_argument("--dry-run", action="store_true", help="Don't write changes")

    args = parser.parse_args()
    if not os.path.isdir(args.directory):
        print(f"Not a directory: {args.directory}")
        sys.exit(2)
    align_tags(args.directory, args.target_tags, args.footer_tags, args.dry_run)
