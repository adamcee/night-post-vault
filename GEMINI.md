# GEMINI.md

Read [[AGENTS]].md before doing anything. It is the single source of truth for this vault.

@AGENTS.md

## Antigravity and Gemini Notes

- Antigravity CLI (`agy`), which replaced Gemini CLI for individual accounts, reads `AGENTS.md` and this file from the workspace. Gemini CLI, still available with paid API keys, loads `AGENTS.md` through the `@AGENTS.md` import above.
- Antigravity looks for workspace skills in `.agents/skills/`. Run the `sync-skills` skill once to link that folder to `.claude/skills/`, so `vault-start` and the other vault skills work here too.
- Use the filesystem tools for vault queries, and the `obsidian` CLI if it is installed.
