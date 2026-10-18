#!/usr/bin/env python3
"""Writing-discipline scan for a vault review.

Scores each markdown file on tightening-checklist heuristics and prints the
worst offenders plus totals. Read-only. Run from anywhere inside the vault:

    python3 .claude/skills/vault-maintenance/vault-review-scan.py            # default dirs + root files
    python3 .claude/skills/vault-maintenance/vault-review-scan.py decisions  # any dirs
    python3 .claude/skills/vault-maintenance/vault-review-scan.py --top 40
    python3 .claude/skills/vault-maintenance/vault-review-scan.py --reweave  # research docs missing Reweave Triggers / evidence-maturity; unnoted weakened triggers

Columns: h3 (### headers), slop (banned words), meta (meta-commentary),
lp (paragraphs > 2 sentences), em (paragraphs with > 1 em-dash), html,
nofm (no frontmatter), fmmiss (missing REQUIRED_FIELDS), cb (orphan
checkboxes). Slop and meta run high on false positives (wikilink filenames,
rule text quoting banned words); paragraph and checkbox counts are mostly real.

Vault root: the nearest directory containing AGENTS.md, searched upward from
the current directory first, then from this script's folder.

Exit code 0 after printing the report (findings are leads, not failures),
2 when no vault root is found or --top has no number.
"""
import re, sys
from pathlib import Path

# --- Configuration -----------------------------------------------------------

# Folders scanned when no folder is named on the command line.
DEFAULT_DIRS = ["architecture", "concepts", "decisions", "ideas", "prototype",
                "research", "strategy", "vault-guide"]
# Root files scanned along with DEFAULT_DIRS.
ROOT_FILES = ["AGENTS.md", "CLAUDE.md", "GEMINI.md", "session-history.md"]
# Folder names never scanned, at any depth: human-only notes, retired docs,
# and unreviewed AI drafts.
EXCLUDE_DIRS = {"journal", "archive", "drafts"}
# Files where task checkboxes belong: the AI ledger, the owner's task list,
# and AGENTS.md (its protocol checklists).
CB_ALLOWED = {"prototype/implementation-plan.md", "prototype/human-task-list.md", "AGENTS.md"}
# Folders whose pages hold protocol checklists.
CB_ALLOWED_PREFIXES = ("vault-guide/",)
# Frontmatter fields every scanned doc should have.
REQUIRED_FIELDS = ("date", "tags")
# Files that need no frontmatter: the root files and folder READMEs.
NO_FRONTMATTER_OK = set(ROOT_FILES) | {"README.md"}

# --reweave settings
REWEAVE_DIRS = ["research"]
REWEAVE_HEADING = "## Reweave Triggers"
MATURITY_FIELD = "evidence-maturity"
# Untouched originals kept beside a cleaned doc; never edited, never scanned.
SOURCE_PREFIX = "_source-"

SLOP = re.compile(r"\b(delve\w*|testament|tapestry|synerg\w*|robust\w*|landscape\w*|leverag\w*|utiliz\w*|articulat\w*|paradigm shift\w*|seamless\w*|holistic\w*)\b", re.I)
META = re.compile(r"(this section|as previously discussed|it is worth noting|the following table|this document|in this document)", re.I)
HTML = re.compile(r"<(?!\!--)(/?[a-zA-Z][a-zA-Z0-9]*)(\s[^>]*)?>")

# -----------------------------------------------------------------------------


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


ROOT = find_vault_root()
if ROOT is None:
    print("no vault root found (AGENTS.md not in this or any parent directory)")
    sys.exit(2)

argv = sys.argv[1:]
if "--help" in argv or "-h" in argv:
    print(__doc__)
    sys.exit(0)


def excluded(f):
    """True if a file sits in an excluded folder (judged on the vault-relative path)."""
    return any(p in EXCLUDE_DIRS for p in f.relative_to(ROOT).parts[:-1])


def collect(dirs):
    files = []
    for d in dirs:
        if not (ROOT / d).is_dir():
            print(f"warning: {d}/ not found, skipping", file=sys.stderr)
            continue
        files += sorted((ROOT / d).rglob("*.md"))
    return files


if "--reweave" in argv:
    # Reweave gap finder: research docs without a Reweave Triggers section or maturity field.
    dirs = [a for a in argv if not a.startswith("--")] or REWEAVE_DIRS
    docs = [f for f in collect(dirs) if f.name != "README.md" and not f.name.startswith(SOURCE_PREFIX)
            and not excluded(f) and "prompts" not in f.relative_to(ROOT).parts]
    no_rw, no_em = [], []
    for f in docs:
        t = f.read_text(errors="replace")
        rel = f.relative_to(ROOT).as_posix()
        if REWEAVE_HEADING not in t:
            no_rw.append(rel)
        m = re.match(r"---\n(.*?)\n---", t, re.S)
        if not m or not re.search(rf"^{re.escape(MATURITY_FIELD)}\s*:", m.group(1), re.M):
            no_em.append(rel)
    print(f"research docs scanned: {len(docs)} (README and {SOURCE_PREFIX}* excluded)")
    print(f"\nmissing '{REWEAVE_HEADING}': {len(no_rw)}")
    for r in no_rw: print("  " + r)
    print(f"\nmissing '{MATURITY_FIELD}' frontmatter: {len(no_em)}")
    for r in no_em: print("  " + r)
    # Weakened or invalidated triggers whose target never mentions the source doc
    # (Reweave Protocol: the note goes in the target, since backlinks don't carry the verdict).
    by_stem = {}
    for f in ROOT.rglob("*.md"):
        parts = f.relative_to(ROOT).parts
        if not any(p.startswith(".") or p in EXCLUDE_DIRS for p in parts[:-1]):
            by_stem.setdefault(f.stem, f)
    unnoted = []
    for f in docs:
        t = f.read_text(errors="replace")
        if REWEAVE_HEADING not in t:
            continue
        for line in t.split(REWEAVE_HEADING, 1)[1].split("\n## ", 1)[0].splitlines():
            m = re.match(r"\s*-\s*\[\[([^\]|#\\]+)", line)
            if not m or not re.search(r"\b(weaken(ed|s)?|invalidated?)\b", line, re.I):
                continue
            target = by_stem.get(Path(m.group(1).strip()).stem)
            if target and f.stem not in target.read_text(errors="replace"):
                unnoted.append(f"{f.relative_to(ROOT).as_posix()} -> {target.relative_to(ROOT).as_posix()}")
    print(f"\nweakened/invalidated triggers with no note in the target: {len(unnoted)}")
    for r in unnoted: print("  " + r)
    sys.exit(0)

top = 25
if "--top" in argv:
    i = argv.index("--top")
    try:
        top = int(argv[i + 1])
    except (IndexError, ValueError):
        print("--top needs a number, e.g. --top 40")
        sys.exit(2)
    del argv[i:i + 2]
args = [a for a in argv if not a.startswith("--")]
dirs = args or DEFAULT_DIRS
files = [ROOT / f for f in ROOT_FILES if (ROOT / f).exists()] if not args else []
files += collect(dirs)
files = [f for f in files if not excluded(f) and not f.name.startswith(SOURCE_PREFIX)]


def sentences(t):
    t = re.sub(r"\[\[[^\]]*\]\]", "LINK", t)
    t = re.sub(r"`[^`]*`", "CODE", t)
    t = re.sub(r"\b(e\.g|i\.e|vs|etc|Dr|Mr|Ms|St|No|Fig|approx|cf)\.", "X", t)
    t = re.sub(r"\d\.\d", "N", t)
    return len(re.findall(r"[.!?](\s|$)", t))


rows = []
for f in files:
    rel = f.relative_to(ROOT).as_posix()
    txt = f.read_text(errors="replace")
    r = dict(file=rel, h3=0, slop=0, meta=0, lp=0, em=0, html=0, nofm=0, fmmiss="", cb=0, words=[])
    body, fm = txt, None
    if txt.startswith("---"):
        m = re.match(r"---\n(.*?)\n---\n?", txt, re.S)
        if m:
            fm, body = m.group(1), txt[m.end():]
    if fm is None:
        r["nofm"] = 0 if (rel in NO_FRONTMATTER_OK or f.name == "README.md") else 1
    else:
        r["fmmiss"] = ",".join(k for k in REQUIRED_FIELDS if not re.search(rf"^{k}\s*:", fm, re.M))
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    r["h3"] = len(re.findall(r"^#{3,}\s", body, re.M))
    # Quoted or code-formatted text is an example of the phrase, not a use of it.
    prose = re.sub(r"\*\*[^*\n]+\*\*", "", body)
    prose = re.sub(r"`[^`\n]*`|\"[^\"\n]*\"|“[^”\n]*”|\*[^*\n]+\*", "", prose)
    r["slop"] = len(SLOP.findall(prose)); r["words"] = sorted({w.lower() for w in SLOP.findall(prose)})
    r["meta"] = len(META.findall(prose))
    r["html"] = len(HTML.findall(re.sub(r"`[^`\n]*`", "", body)))
    if rel not in CB_ALLOWED and not rel.startswith(CB_ALLOWED_PREFIXES):
        r["cb"] = len(re.findall(r"^\s*- \[[ x~]\]", body, re.M))
    for para in re.split(r"\n\s*\n", body):
        p = para.strip()
        if not p or p.startswith(("#", "|", "-", "*", "+", ">", "<")) or re.match(r"^\d+\.", p):
            continue
        if re.search(r"^\s*[-*]\s", p, re.M):
            continue
        if sentences(p) >= 3:
            r["lp"] += 1
        if p.count("—") > 1:
            r["em"] += 1
    r["score"] = r["h3"] + 2*r["slop"] + 2*r["meta"] + 2*r["lp"] + r["em"] + r["html"] + 5*r["nofm"] + (2 if r["fmmiss"] else 0) + 3*r["cb"]
    rows.append(r)

rows.sort(key=lambda x: -x["score"])
print(f"{'file':60} {'sc':>3} h3 slop meta lp em html nofm fmmiss     cb")
for r in rows[:top]:
    print(f"{r['file'][:60]:60} {r['score']:3} {r['h3']:2} {r['slop']:4} {r['meta']:4} {r['lp']:2} {r['em']:2} {r['html']:4} {r['nofm']:4} {r['fmmiss'][:10]:10} {r['cb']:2}  {','.join(r['words'])[:40]}")
print("\nTotals:", {k: sum(r[k] for r in rows) for k in ("h3", "slop", "meta", "lp", "em", "html", "nofm", "cb")}, "files:", len(rows))
print("no frontmatter:", [r["file"] for r in rows if r["nofm"]])
print("frontmatter missing fields:", [(r["file"], r["fmmiss"]) for r in rows if r["fmmiss"]])
print("orphan checkboxes:", [(r["file"], r["cb"]) for r in rows if r["cb"]])
