---
name: sync-skills
description: "Makes the vault's skills in .claude/skills/ available to other agent CLIs, such as Antigravity CLI and Gemini CLI. Use when the user asks to manage, link, or check skills, or when vault-start finds them missing."
---

# Sync Skills

The vault keeps one copy of its skills in `.claude/skills/`. Other agent CLIs look elsewhere, so link them to that folder instead of copying.

## Antigravity CLI (`agy`)

Antigravity reads workspace skills from `.agents/skills/`. From the vault root:

```bash
mkdir -p .agents
ln -s ../.claude/skills .agents/skills
```

Check with `ls .agents/skills/`: it should list `vault-start`, `vault-links`, `vault-maintenance`, `prompt-architect`, and `sync-skills`. On Windows, where symlinks may be unavailable, copy the folder instead and rerun this skill after skills change.

## Gemini CLI (paid API keys)

Gemini CLI links skills one at a time:

```bash
gemini skills list
gemini skills link .claude/skills/<skill-name>
```

Link every folder in `.claude/skills/` that `gemini skills list` doesn't show.
