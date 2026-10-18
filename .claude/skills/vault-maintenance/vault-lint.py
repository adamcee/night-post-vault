#!/usr/bin/env python3
"""Session-close checks for the vault. Run from anywhere inside it.

Checks the files every agent touches at session close, where sessions break
things: AGENTS.md size, very long lines, session-history.md headings and entry
format, agreement between session-history.md and the weekly log, and
append-only logs (lines removed since the last commit fail unless
--allow-edits is passed; past weekly logs fail on any change).

Usage:
    python3 .claude/skills/vault-maintenance/vault-lint.py
    python3 .claude/skills/vault-maintenance/vault-lint.py --allow-edits   # after an intentional correction

Vault root: the nearest directory containing AGENTS.md, searched upward from
the current directory first, then from this script's folder.

Exit code 0 when clean, 1 when any check fails, 2 when no vault root is found.
"""
import datetime
import re
import subprocess
import sys
from pathlib import Path

ALLOW_EDITS = "--allow-edits" in sys.argv[1:]
if "--help" in sys.argv[1:] or "-h" in sys.argv[1:]:
    print(__doc__)
    sys.exit(0)

# AGENTS.md is read in full at the start of every session. Some agent tools
# read files in fixed-size chunks (one CLI shows 46,080 bytes per call) and
# silently drop the rest, so rules near the end of a long AGENTS.md go unread.
# The cap leaves a margin under that limit and keeps detail in the pages
# AGENTS.md points to.
AGENTS_MAX_BYTES = 40_000

# Edit tools match exact text, and very long lines make those edits fail or
# mangle the line. Pointer files are checked only if they exist.
LINE_LIMITS = {
    "AGENTS.md": 1_000,
    "CLAUDE.md": 1_000,
    "GEMINI.md": 1_000,
    "session-history.md": 2_000,
}
REQUIRED = {"AGENTS.md", "session-history.md"}
LOG_DIR = "prototype/implementation-logs"

DATE = r"\d{4}-\d{2}-\d{2}"
# One line per session: "- (agent, session type) what changed"
ENTRY = re.compile(r"- \([^(),]+, [^()]+\) \S")


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
    print("vault-lint: no AGENTS.md in this or any parent directory.")
    sys.exit(2)

failures = []
notes = []


def fail(msg):
    failures.append(msg)


def read(name):
    p = ROOT / name
    if not p.exists():
        if name in REQUIRED:
            fail(f"{name}: missing")
        return None
    return p.read_text(encoding="utf-8")


# --- AGENTS.md ---------------------------------------------------------------

agents = read("AGENTS.md") or ""
size = len(agents.encode("utf-8"))
if size > AGENTS_MAX_BYTES:
    fail(f"AGENTS.md: {size} bytes, limit {AGENTS_MAX_BYTES}. Move detail to the docs it points to.")
if re.search(rf"^## {DATE}", agents, re.M) or any(ENTRY.match(l) for l in agents.split("\n")):
    fail("AGENTS.md: contains a session entry. Session entries go in session-history.md and the weekly log.")

for name, limit in LINE_LIMITS.items():
    text = read(name)
    if text is None:
        continue
    for n, line in enumerate(text.split("\n"), 1):
        if len(line) > limit:
            fail(f"{name}:{n}: line is {len(line)} characters, limit {limit}. Split it.")

# --- session-history.md ------------------------------------------------------

history = read("session-history.md") or ""
for n, line in enumerate(history.split("\n"), 1):
    if line.startswith("## ") and not re.fullmatch(rf"## {DATE}\s*", line):
        if "YYYY-MM-DD" in line:
            fail(f"session-history.md:{n}: placeholder heading '{line.strip()}'. Replace it with the vault's creation date.")
        else:
            fail(f"session-history.md:{n}: heading must be '## YYYY-MM-DD' alone: {line[:80]}")
heads = re.findall(rf"^## ({DATE})\s*$", history, re.M)
last_date = heads[-1] if heads else None
dupes = sorted({h for h in heads if heads.count(h) > 1})
if dupes:
    fail(f"session-history.md: date heading repeated: {', '.join(dupes)}. Two sessions added it at once; merge the sections.")
if heads != sorted(heads):
    fail("session-history.md: date headings are out of order. Entries go under today's heading at the end of the file.")
if last_date:
    try:
        if datetime.date.fromisoformat(last_date) > datetime.date.today():
            fail(f"session-history.md: last heading {last_date} is in the future.")
    except ValueError:
        fail(f"session-history.md: {last_date} is not a real date.")
    # Only the last section is checked: older entries may predate the format,
    # and append-only means they stay as written.
    last = history[history.rindex(f"## {last_date}"):]
    for line in last.split("\n")[1:]:
        if line.strip() and not ENTRY.match(line):
            fail(f"session-history.md: entry not in '- (agent, session type) what changed' form: {line[:80]}")

# --- Weekly logs ---------------------------------------------------------------

logs = sorted((ROOT / LOG_DIR).glob("20??-W??.md"))
if logs:
    for log in logs:
        rel = log.relative_to(ROOT)
        year, week = int(log.stem[:4]), int(log.stem[6:])
        for n, line in enumerate(log.read_text(encoding="utf-8").split("\n"), 1):
            if not line.startswith("## "):
                continue
            m = re.match(rf"## ({DATE})", line)
            if not m:
                if log == logs[-1]:
                    fail(f"{rel}:{n}: section heading must start with a date: {line[:80]}")
                continue
            try:
                iso = datetime.date.fromisoformat(m.group(1)).isocalendar()
            except ValueError:
                fail(f"{rel}:{n}: {m.group(1)} is not a real date.")
                continue
            if (iso[0], iso[1]) != (year, week):
                fail(f"{rel}:{n}: {m.group(1)} falls in {iso[0]}-W{iso[1]:02d}, not {log.stem}.")
    if last_date:
        try:
            iso = datetime.date.fromisoformat(last_date).isocalendar()
            expected = ROOT / LOG_DIR / f"{iso[0]}-W{iso[1]:02d}.md"
            if not expected.exists():
                fail(f"{expected.relative_to(ROOT)}: missing. session-history.md has an entry for {last_date}; "
                     f"add the week's log with a '## {last_date}' section.")
            elif not re.search(rf"^## {last_date}", expected.read_text(encoding="utf-8"), re.M):
                fail(f"{expected.relative_to(ROOT)}: no section for {last_date}. Add '## {last_date} ...' to match session-history.md.")
        except ValueError:
            pass
else:
    notes.append(f"no weekly logs in {LOG_DIR}/; skipped log checks")

# --- Append-only logs ----------------------------------------------------------

# Lines removed since the last commit mean a session rewrote the file. Past
# weekly logs are closed, so any change to one fails.
try:
    head_ok = subprocess.run(["git", "rev-parse", "--verify", "-q", "HEAD"], cwd=ROOT,
                             capture_output=True, text=True).returncode == 0
except FileNotFoundError:  # git not installed
    head_ok = False
if not head_ok:
    notes.append("not a git repository with commits; skipped append-only checks")
else:
    current = [str(logs[-1].relative_to(ROOT))] if logs else []
    past = [str(l.relative_to(ROOT)) for l in logs[:-1]]
    for name in ["session-history.md"] + current + past:
        diff = subprocess.run(["git", "diff", "--unified=0", "HEAD", "--", name], cwd=ROOT,
                              capture_output=True, text=True)
        changed = [l for l in diff.stdout.split("\n")
                   if l[:1] in "+-" and l and not l.startswith(("---", "+++"))]
        removed = [l for l in changed if l.startswith("-")]
        if name in past and changed and not ALLOW_EDITS:
            fail(f"{name}: changed since the last commit. Past weekly logs are closed; "
                 f"log today's work in this week's file, or rerun with --allow-edits if the fix was intentional.")
        elif removed and not ALLOW_EDITS:
            fail(f"{name}: {len(removed)} line(s) removed since the last commit. Logs are append-only; "
                 f"restore them, or rerun with --allow-edits if you corrected an entry on purpose.")

for note in notes:
    print(f"note: {note}")
if failures:
    print("\n".join(failures))
    print(f"\n{len(failures)} failure(s).")
    sys.exit(1)
print("vault-lint: all checks pass.")
