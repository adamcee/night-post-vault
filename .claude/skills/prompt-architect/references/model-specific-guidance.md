# Model-Specific Prompt Engineering Guidance

Patterns for the major model families. Behavior shifts between model versions, so treat these as defaults and confirm version-specific details in each provider's current prompting guide.

## Claude (Anthropic)

**Structural preferences:**
- XML tags are the primary structural mechanism: `<instructions>`, `<context>`, `<constraints>`, `<examples>`, `<output_format>`.
- `<thinking>` tags enable explicit chain-of-thought reasoning before the response.
- `<example>` blocks with `<input>` and `<output>` sub-tags work well for few-shot demonstrations.
- The system prompt sets baseline behavior; user messages trigger task execution within that frame.

**Behavioral tendencies to manage:**
- Claude over-explains by default, so always include explicit length and scope constraints.
- It responds well to negative constraints ("never do X") and better to positive and negative pairs ("do Y; never do X").
- It follows XML-delimited instructions more precisely than prose instructions.
- It respects persona framing without elaborate backstories; role plus constraints is enough.

**High-leverage patterns:**
- "Think step by step in `<thinking>` tags before responding" improves quality on reasoning tasks.
- Prefilling the assistant turn forces an output format, where the API version supports it.
- Explicit `<rules>` blocks for behavioral constraints get treated as high priority.
- "If you're uncertain, say so rather than guessing" is respected more reliably than in most models.

**Context window notes:**
- Performance degrades with context overload even inside a large window, so optimize for signal density.
- Put the most important instructions at the beginning and end of the prompt (primacy and recency effects).
- For long documents, provide a summary plus the key sections rather than the full text.

**Sources:** Anthropic prompt engineering docs (docs.claude.com) and Anthropic's context engineering guide (anthropic.com/engineering).

---

## Gemini (Google)

**Structural preferences:**
- Hierarchical markdown with headers, subheaders, and numbered steps.
- Explicit step decomposition helps more than with other models.
- Structured output templates (JSON schemas, markdown tables) are followed well.
- System instructions set persistent behavior across multi-turn conversations.

**Behavioral tendencies to manage:**
- Gemini drifts in scope on research tasks and explores tangents without firm boundaries.
- It tends toward long outputs, so explicit word or sentence limits are essential.
- It follows structural templates closely when given one.
- It can produce confident but invented citations, so always require "flag if unsourced".

**High-leverage patterns:**
- Numbered step-by-step instructions execute more reliably than prose.
- "Limit your response to the following scope: [explicit boundary]".
- For deep research, give the exact list of sources to read, not just topics to explore.
- Markdown tables in the prompt template produce well-structured tabular output.

**Context window notes:**
- A very large context enables whole-document analysis, but signal-to-noise still matters.
- Explicit "focus on" directives help when processing large inputs.
- Structure research briefs as context preamble, then specific questions, then output format, then constraints.

---

## GPT (OpenAI)

**Structural preferences:**
- System message and user message separation is well respected.
- JSON mode and structured output schemas produce reliable machine-readable output.
- Numeric constraints ("under 50 words", "exactly 3 items") are followed precisely.
- It tolerates XML tags, and markdown structure works equally well.

**Behavioral tendencies to manage:**
- It can be overly agreeable and push back too little on flawed premises.
- JSON output mode can produce valid JSON that doesn't match the intent.
- Function calling is well supported, but tool descriptions must be precise.

**High-leverage patterns:**
- `response_format: { type: "json_schema", ... }` guarantees structured output.
- "You must respond with exactly N items"; numeric precision is a strength.
- Persistent behavioral constraints go in the system message, task-specific instructions in the user message.
- Temperature 0 gives more deterministic output when consistency matters, on models that expose it.

---

## Model-Agnostic Design

When one prompt is rendered by a provider-abstraction layer and sent to whichever model the configuration names, design for the intersection:
- **Use XML tags.** Claude and Gemini support them, and GPT tolerates them.
- **Include explicit constraints.** Every model respects them.
- **Avoid provider-only features.** Skip Claude `<thinking>` tags, GPT JSON mode, and Gemini-specific markdown conventions.
- **Test with the weakest target model.** If it works on the least capable provider, it works everywhere.
- **Keep few-shot examples brief.** One or two examples conserve tokens across providers with different context costs.
- **Use explicit step decomposition.** "Step 1: Assess... Step 2: Generate... Step 3: Verify..." works for every model.

**Variable slots in templates:**
- Use consistent delimiters, such as `{{user_name}}`, `{{current_task}}`, `{{prior_attempts}}`, and `{{session_history_summary}}`.
- Document each variable's type, source, and fallback value.
- Keep dynamic state in a separate XML block from static instructions.
