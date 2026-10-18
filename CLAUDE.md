**Before any work, run the `vault-start` skill** (`.claude/skills/vault-start/SKILL.md`). If you realize mid-session that you skipped it, run it now.

# CLAUDE.md

Read [[AGENTS]].md before doing anything. It is the single source of truth for this vault.

@AGENTS.md

## Claude-Specific Notes

- Claude Code loads `AGENTS.md` through the `@AGENTS.md` import above. Other Claude surfaces should read it directly.
- Vault skills live in `.claude/skills/`: `vault-start`, `vault-links`, `vault-maintenance`, `prompt-architect`, and `sync-skills`. Read a skill's `SKILL.md` before running its scripts.
- **Moving notes:** use the Obsidian CLI `move` command, which rewrites links. If you must use `mv`, fix the links and run `vault-link-check.py` before closing the task.
- **Claude Desktop with Obsidian MCP:** append to logs with the MCP append tool, never by overwriting the file. For files over about 20KB, write a stub and append in chunks. Read files created this session by path, since search lags.
