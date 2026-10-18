# Obsidian Configuration

Open this folder in Obsidian with **Open folder as vault**. Then connect a desktop AI app that supports MCP (Model Context Protocol), such as Claude Desktop or the Codex app, so every chat can read and write the vault while you edit it here. Back the vault up to a private GitHub repository with the Git plugin.

## Plugins That Help the AI

- **Local REST API with MCP** (community): runs an MCP server so desktop AI apps can read, search, and write notes.
- **Omnisearch** (community): fast full-text search with an HTTP API agents can query.
- **Bases** (core): queryable tables over decision frontmatter, using `decisions/_BASES_SCHEMA.md`.
- **Properties** (core): view and edit frontmatter such as decision status.
- **Backlinks**, **Outgoing links**, and **Graph view** (core): see how notes connect; reweaves rely on backlinks.
- **Git** (community): scheduled commit and push to GitHub, so every AI edit is backed up and reversible.
- **Find orphaned files and broken links** (community): link hygiene for maintenance sessions.
- **Linter** (community): consistent frontmatter and formatting.
- **Templater** (community): templates for decision records, research docs, and ideas.

Optional: **Smart Connections** (semantic search), **Dataview** (custom frontmatter queries), and **Agent Client** or **Copilot** (run Claude Code or Codex inside Obsidian).

Full guide: https://adamcee.github.io/agentic-vault/installation/obsidian-setup/
