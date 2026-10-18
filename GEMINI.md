# GEMINI.md

Read [[AGENTS]].md before doing anything. It is the single source of truth for this vault.

@AGENTS.md

## Gemini-Specific Notes

- Gemini CLI loads `AGENTS.md` through the `@AGENTS.md` import above. If it doesn't, run `read_file('AGENTS.md')`.
- Use `read_file`, `grep_search`, `glob`, and `run_shell_command` (with the `obsidian` CLI if installed) for vault queries.
- Link the vault skills with the `sync-skills` skill so Gemini can run `vault-start`.
