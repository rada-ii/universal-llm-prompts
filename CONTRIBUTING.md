# Contributing to Universal LLM Prompts

## Quick Contribution Checklist

Before submitting a prompt:

- [ ] Tested on ChatGPT 4 and Claude 3
- [ ] Follows standard format (see templates)
- [ ] Includes realistic test input and expected output
- [ ] Uses clear, non-technical language
- [ ] Solves real-world problem

## Types of Contributions

### Simple Prompts

**For**: Documents humans read (business plans, emails, lesson plans)

**Requirements**:

- Clear "What this does" section
- Step-by-step instructions
- Complete prompt with examples
- Expected output sample
- Success tips

### Structured Prompts

**For**: Data extraction and automation (JSON/CSV outputs)

**Requirements**:

- Valid JSON/CSV schema
- Error handling for bad inputs
- Compatibility headers
- Confidence scoring
- Edge case handling

## Standard Templates

### Simple Prompt Format

```markdown
# [Tool Name] Creator

## What this does:

[1-2 sentences explaining purpose and target user]

## How to use:

1. Copy this entire prompt
2. Replace [bracketed sections] with your details
3. Paste into any AI assistant

## The Prompt:

[Complete prompt with clear placeholders]

## Example Result:

[Realistic example output]

## Tips for Success:

1. **Be specific** - Include details about your situation
2. **Provide context** - Explain who will use the output
3. **Set constraints** - Mention budget, timeline, limitations
```

### Structured Prompt Format

```markdown
[COMPAT HEADER — STRUCTURED OUTPUT (JSON)]
• Output must be JSON only; first character must be {.
• On failure, return only: {"error":"format_violation","note":"why"}.
[/COMPAT]

# [Tool Name] - Structured Template

## Purpose

[Brief explanation of data extraction/processing]

## Template

<s>JSON only, no extra text.</s>
<schema>[Complete JSON schema]</schema>
<examples>[3-5 realistic examples]</examples>
<task>[Processing instructions]</task>
<input>{{INPUT_VARIABLE}}</input>
```

## Testing Requirements

### Before Submitting

1. **Test on multiple platforms**

   - ChatGPT 4 (required)
   - Claude 3 (required)
   - Note platform differences

2. **Create test files**

   - Add realistic input to `tests/inputs/[category]/`
   - Save expected output to `tests/outputs/[category]/`

3. **Validate quality**
   - Non-technical users can follow instructions
   - Output is immediately usable
   - Handles edge cases gracefully

## File Organization

### Naming Convention

- Simple prompts: `[tool-name]-simple.md`
- Structured prompts: `[tool-name]-structured.md`
- Test inputs: `[descriptive-name].txt`
- Use lowercase with hyphens

### Folder Structure

```
prompts/
├── simple/[category]/[tool-name]-simple.md
└── structured/[category]/[tool-name]-structured.md

tests/
├── inputs/[category]/[test-case].txt
└── outputs/[category]/[expected-result].[json|csv|md]
```

## Quality Standards

### Writing Style

- **Clear and conversational** - No jargon
- **Specific examples** - Real scenarios, not generic placeholders
- **Action-oriented** - Focus on results users achieve
- **Inclusive language** - No assumptions about background

### Technical Standards

- **Cross-platform compatibility** - Works on ChatGPT, Claude, Gemini
- **Error resilience** - Handles malformed inputs
- **Consistent formatting** - Follows established patterns
- **Validation** - Outputs are parseable and usable

## Submission Process

1. **Fork repository**
2. **Create branch**: `add-[prompt-name]`
3. **Add prompt and test files**
4. **Submit pull request** with:
   - Clear description of prompt purpose
   - Testing results from different platforms
   - Example use cases

## What Makes Good Contributions

### Excellent Prompts

- Solve real problems people face regularly
- Work consistently across AI platforms
- Produce immediately usable results
- Include helpful examples and context

### Avoid

- Prompts requiring technical knowledge
- Outputs needing significant editing
- Overly complex instructions
- Platform-specific solutions

## Recognition

Quality contributors receive:

- Credit in prompt file headers
- Invitation to review future contributions
- Priority for feature requests

## Getting Help

- Check existing issues for similar questions
- Create new issue for bugs or features
- Email maintainer for private questions

Focus on creating prompts that solve real problems with minimal user effort.
