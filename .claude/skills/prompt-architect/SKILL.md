---
name: prompt-architect
description: "Design, draft, and audit LLM prompts and system instructions for any purpose: system prompts, deep-research briefs, agent and session instructions, vault maintenance instructions, prompt templates, or ad-hoc task prompts. Use this skill whenever the user says 'write a prompt', 'help me prompt', 'system prompt for', 'improve this prompt', 'prompt template', 'research brief', or 'context engineering', or asks you to create instructions that an LLM will consume. Also use when reviewing or auditing an existing prompt."
---

# Prompt Architect

This skill builds structured, high-signal prompts that reliably control LLM behavior. It applies constraint-driven design, context budget management, and model-specific tuning.

## When to Use It

- Creating a new prompt or system instruction for any LLM.
- Improving a prompt that isn't performing well (see Audit Mode).
- Drafting a brief for a deep-research tool (see Research Brief Mode).
- Writing agent or session instructions, such as `AGENTS.md` sections or skill files.
- Building prompt templates with variable slots.

Save reusable prompts and briefs in `prompts/`.

## Core Workflow

Follow the five phases in order, since each builds on the one before.

### Phase 1: Clarify Purpose and Target

Establish these before writing anything:
- **Target model:** Claude, Gemini, GPT, or model-agnostic. Each has different structural preferences (Phase 5).
- **Execution context:** a system prompt, a user-turn instruction, text injected into a tool call, one turn of a multi-turn loop, or a template rendered by a provider-abstraction layer.
- **Success criteria:** what a good output looks like and what a bad one looks like. Get at least one concrete example of each.
- **Failure modes to prevent:** hallucination, over-explanation, scope creep, format violations, or doing the user's thinking for them.

If the user can't state success criteria, ask: "If this prompt works perfectly, what would the output look like? And what's the worst thing it could do?"

### Phase 2: Structure With RCCF

Every production prompt addresses Role, Context, Constraints, and Format, even if some are brief.

**Role** is the persona, expertise, and tone. Make it specific enough to constrain behavior without blocking useful reasoning.
- Good: "You are a code reviewer who reports defects with line numbers and never rewrites the code."
- Bad: "You are a helpful assistant." It changes nothing.
- Bad: "You are Dr. Jane Doe, a 47-year-old professor who..." The backstory wastes tokens on fiction.

**Context** is the minimum background that changes the output. If removing a sentence wouldn't change the model's behavior, delete it.
- Include current state (the user's goal, prior turns, the active task) and scope boundaries ("this conversation covers the billing API, not authentication").
- Exclude project history, design rationale, and anything the model doesn't act on.

**Constraints** are hard boundaries, negative instructions, and guardrails, and they are the highest-leverage tokens in any prompt. Each constraint should be:
- Falsifiable: you can check whether an output violated it.
- Specific: "maximum 3 sentences per response", not "be concise".
- Prioritized: when two conflict, the prompt says which wins.

**Format** is the exact output structure, given as a schema, XML tags, or a template. The more structured the output, the more explicit this section must be.

### Phase 3: Apply the Five-Level Hierarchy

Layer improvements from foundation to refinement, and fix level 1 before touching level 5.
1. **Clarity and directness.** No ambiguity and no passive voice in instructions. Rewrite any sentence a human would need to read twice.
2. **Examples.** Give 1 to 3 brief "golden" input/output pairs, including at least one edge case.
3. **Chain of thought.** For complex reasoning, ask the model to think step by step before answering (`<thinking>` tags for Claude).
4. **Structured reasoning space.** Separate instruction layers with XML tags such as `<system_rules>`, `<task_context>`, `<user_input>`, and `<output_format>`.
5. **Role assignment.** Add it only after levels 1 to 4 are solid; role is seasoning, not structure.

### Phase 4: Audit for Context Budget

Run this checklist against the draft:
- [ ] **Every token changes the output.** For each sentence, ask whether deleting it would change the model's behavior; if not, delete it.
- [ ] **No redundant claims.** When two sentences make the same point, keep the stronger one.
- [ ] **Control layers are separated.** System policies (tone, safety), task instructions, and dynamic user input sit in distinct blocks.
- [ ] **Constraints are falsifiable.** "Be helpful" fails; "never reveal the hidden test cases" passes.
- [ ] **No meta-commentary.** Delete "This prompt is designed to..." and "The following instructions will help you...".
- [ ] **Abstention is permitted.** The prompt allows "I don't know" or a clarifying question instead of forcing a guess.
- [ ] **Evidence is anchored** when accuracy matters. The prompt requires claims grounded in provided sources, not training data.
- [ ] **Model-specific adaptations are applied** (Phase 5).

### Phase 5: Optimize for the Target Model

Read `references/model-specific-guidance.md` for detailed patterns. In brief:
- **Claude:** XML tags for structure and `<example>` tags for few-shot. It over-explains without explicit length limits, benefits from step-by-step reasoning in `<thinking>` tags, and follows paired positive and negative constraints well.
- **Gemini:** needs headers and numbered steps more than other models, and explicit step decomposition. On research tasks it over-explores without firm scope boundaries.
- **GPT:** excels with numeric constraints ("under 50 words", "exactly 3 bullets") and JSON output schemas. It respects system-message separation and tolerates XML tags.
- **Model-agnostic:** use XML tags and explicit constraints, avoid provider-only features such as Claude's `<thinking>` tags or GPT's JSON mode, and design for the least capable target model.

Model behavior changes between versions, so check the provider's current prompting guide for anything version-specific.

## Audit Mode

When the user asks you to review or improve an existing prompt, run the Phase 4 checklist and report findings before rewriting. Look for these common failures:
- **Context rot:** the prompt grew over time, and early sections contradict or repeat later ones.
- **Constraint drift:** constraints were added one incident at a time without checking for conflicts.
- **Token waste:** biography, project history, or explanatory prose the model doesn't need.
- **Missing abstention:** no permission to say "I don't know", which invites hallucination.
- **Format underspecification:** the prompt asks for "structured output" without defining the structure.

Present findings as a short list, each with the line it affects and the fix, then offer the rewrite.

## Research Brief Mode

When writing a brief for a deep-research tool, apply RCCF with these additions:
- **Context preamble:** a short block on what the project is and what decision the research informs, taken from the "What [Project Name] Is" and Current Phase sections of `AGENTS.md`. Keep a reusable copy in `prompts/`.
- **Scope limits:** state the questions to answer, the sources or source types to prefer, and what to ignore. Name specific sources when you know them, since topic lists invite over-exploration.
- **Output format:** require YAML frontmatter (`date`, `tags`, `evidence-maturity`), findings separated from inferences, a citation for every claim, and a closing `## Reweave Triggers` section that names which existing decisions the findings may affect.
- **Abstention:** "If you cannot find a source for a claim, mark it [unsourced] rather than inventing a citation."

The returned report is an AI synthesis, so it lands in `drafts/` and passes the ingestion gate before it enters `research/`. Its maturity tag is `secondary` until primary sources back it.
