# Contributing to Universal LLM Prompts

Thank you for your interest in contributing! This guide will help you create high-quality prompts that benefit the entire community.

## Quick Contribution Checklist

Before submitting a prompt:

- [ ] Tested on at least 2 different AI platforms (ChatGPT, Claude, etc.)
- [ ] Follows our standard format (see templates below)
- [ ] Includes realistic test input and expected output
- [ ] Uses clear, jargon-free language
- [ ] Solves a real-world problem

## Types of Contributions

### 1. New Simple Prompts

**Best for:** Creating documents, plans, content that humans will read

**Requirements:**

- Clear "What this does" section
- Step-by-step "How to use" instructions
- Complete prompt with placeholder examples
- Real example of expected output
- Tips for success

### 2. New Structured Prompts

**Best for:** Extracting data, JSON/CSV outputs for automation

**Requirements:**

- Valid JSON/CSV schema definition
- Error handling for malformed inputs
- Compatibility headers for different platforms
- Confidence scoring where applicable
- Test cases covering edge cases

### 3. Improvements to Existing Prompts

- Better examples or instructions
- Fixed bugs or compatibility issues
- Additional use cases or variations
- Performance optimizations

## Standard Format Templates

### Simple Prompt Template

```markdown
# [Tool Name] Creator

## What this does:

[1-2 sentences explaining what this prompt creates and who should use it]

## How to use:

1. Copy this entire prompt
2. [Specific step about filling in details]
3. Paste into any AI assistant and get your [output type]

## The Prompt:

[Complete prompt with clear placeholders in brackets]

## Example Result:

[Realistic example of what the AI will produce]

## Tips for Success:

1. **[Tip category]** - [Specific advice]
2. **[Tip category]** - [Specific advice]
3. **[Tip category]** - [Specific advice]

## Common Use Cases:

- **[Use case]** - [When to use this variation]
- **[Use case]** - [When to use this variation]
```

### Structured Prompt Template

```markdown
[COMPAT HEADER — STRUCTURED OUTPUT (JSON/CSV)]
• Output must be [format] only; first character must be [requirement].
• On failure, return only: [error format].
[/COMPAT]

# [Tool Name] - Structured Template

## Purpose

[Brief explanation of what data this extracts or processes]

## Template

<s>[Format] only, no extra text.</s>
<schema>[Complete schema definition]</schema>
<rules>
[Processing rules and validation criteria]
</rules>
<task>[What to do with the input]</task>
<input>{{INPUT_VARIABLE}}</input>

## Test Cases

### [Test Case Name]

Input: [Example input]
Expected: [Expected JSON/CSV output]
```

## Testing Requirements

### Before Submitting

1. **Test on Multiple Platforms**

   - ChatGPT 4 (required)
   - Claude 3 (required)
   - Gemini Pro (recommended)
   - Note any platform-specific issues

2. **Create Test Files**

   - Add realistic input to `tests/inputs/[category]/`
   - Save expected output to `tests/outputs/[category]/`
   - Include edge cases and error scenarios

3. **Validate Output Quality**
   - Can a non-technical person use this successfully?
   - Does it solve a real problem?
   - Is the output immediately usable?

### Testing Checklist

- [ ] Prompt works without modification on ChatGPT 4
- [ ] Prompt works without modification on Claude 3
- [ ] Output format is consistent across platforms
- [ ] Instructions are clear to non-technical users
- [ ] Example output matches what users actually get
- [ ] Error cases are handled gracefully (for structured prompts)

## File Organization

### Naming Conventions

- Simple prompts: `[tool-name]-simple.md`
- Structured prompts: `[tool-name]-structured.md`
- Test inputs: `[descriptive-name].txt`
- Use lowercase with hyphens, no spaces

### Folder Structure

```
prompts/
├── simple/
│   └── [category]/
│       └── [tool-name]-simple.md
└── structured/
    └── [category]/
        └── [tool-name]-structured.md

tests/
├── inputs/
│   └── [category]/
│       └── [test-case].txt
└── outputs/
    └── [category]/
        └── [expected-result].[json|csv|md]
```

## Quality Standards

### Writing Style

- **Clear and conversational** - Write like you're helping a friend
- **Specific examples** - Use realistic scenarios, not generic placeholders
- **Action-oriented** - Focus on what users will accomplish
- **Inclusive language** - Avoid assumptions about gender, culture, or background

### Technical Standards

- **Cross-platform compatibility** - Test on multiple AI services
- **Error resilience** - Handle malformed inputs gracefully
- **Consistent formatting** - Follow established patterns
- **Validation** - Ensure outputs can be parsed/used as intended

## Contribution Process

### Step 1: Plan Your Contribution

1. Check existing prompts to avoid duplication
2. Identify the specific problem your prompt solves
3. Choose simple vs. structured based on output needs
4. Research similar tools to ensure yours adds unique value

### Step 2: Create Your Prompt

1. Follow the appropriate template exactly
2. Write clear, tested instructions
3. Create realistic examples
4. Test thoroughly on multiple platforms

### Step 3: Submit for Review

1. Fork the repository
2. Create a new branch: `add-[prompt-name]`
3. Add your prompt and test files
4. Submit a pull request with:
   - Clear description of what the prompt does
   - Testing results from different platforms
   - Example use cases

### Step 4: Respond to Feedback

- Address reviewer comments promptly
- Make requested changes
- Update tests if needed
- Collaborate to ensure quality

## What Makes a Great Contribution

### Excellent Prompts:

- Solve real problems that people face regularly
- Work consistently across different AI platforms
- Produce immediately usable results
- Include helpful examples and tips
- Are well-tested with realistic inputs

### Avoid:

- Prompts that require technical knowledge to use
- Outputs that need significant editing to be useful
- Overly complex instructions
- Generic examples that don't represent real use
- Prompts that work on only one AI platform

## Recognition

Contributors who submit high-quality prompts will be:

- Listed in the CONTRIBUTORS.md file
- Credited in the prompt file comments
- Invited to help review future contributions
- Given priority for feature requests

## Questions?

- Check existing issues for similar questions
- Create a new issue for bugs or feature requests
- Start a discussion for general questions
- Email [maintainer] for private questions

Thank you for helping make AI more accessible and useful for everyone!
