---
name: sync-skills
description: "Synchronizes vault-based skills (.claude/skills/) with the CLI environment. Use this whenever the user asks to manage, link, or check for new skills."
---

# Sync Skills

Ensures that CLI environments (like Gemini CLI) maintain feature parity by linking new skills.

## 🛠️ Tooling & Operations

### 1. Check Discovered Skills
List the skills currently recognized by the environment (e.g., `gemini skills list`).

### 2. Scan Vault Skills
List the skill directories in the vault:
```bash
ls -1 .claude/skills/
```

### 3. Link Missing Skills
If there is a directory in `.claude/skills/` that does not appear in the installed skills list, link it immediately. 
Example for Gemini CLI:
```bash
gemini skills link .claude/skills/example-skill
```
*(Auto-accept prompts if necessary, e.g., `yes | gemini skills link...`)*