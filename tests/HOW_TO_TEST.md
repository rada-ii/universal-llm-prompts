# How to Test Universal LLM Prompts

This guide explains how to test prompts systematically across different AI platforms to ensure reliability and consistency.

## Quick Testing (5 minutes)

```bash
# From project root
bash scripts/run-all-tests.sh
```

This automatically validates:

- File structure integrity
- JSON syntax in golden outputs
- Test input readability
- Cross-platform compatibility headers

## Testing Overview

### Why We Test

- **Quality assurance** - Ensure prompts produce useful results
- **Cross-platform compatibility** - Work on ChatGPT, Claude, and Gemini
- **User experience** - Non-technical users can follow instructions
- **Consistency** - Same input produces similar quality across platforms

### What We Test

1. **File validation** - Proper format and structure
2. **Input quality** - Test cases represent real scenarios
3. **Output consistency** - Similar results across AI platforms
4. **User experience** - Instructions are clear and complete

## Testing Tools

### Automated Tools

**`tests/test-runner.py`** - Main validation script

```bash
# Test all categories
python3 tests/test-runner.py

# Test specific category
python3 tests/test-runner.py --category business

# Validate golden outputs only
python3 tests/test-runner.py --validate-golden
```

**`scripts/validate_json_examples.py`** - JSON validation

```bash
python3 scripts/validate_json_examples.py
```

**`scripts/run-all-tests.sh`** - Complete test suite

```bash
bash scripts/run-all-tests.sh
```

### Manual Testing Process

#### Step 1: Choose Test Case

- Navigate to `tests/inputs/[category]/`
- Select appropriate test file (e.g., `business-idea-1.txt`)
- Review test scenario for completeness

#### Step 2: Prepare Prompt

- Open corresponding prompt file
- Copy entire prompt content
- Replace all `[PLACEHOLDER]` sections with data from test file
- Do NOT modify prompt structure

#### Step 3: Test on Platforms

**Required platforms:**

- ChatGPT 4 (primary)
- Claude 3 (primary)

**Settings:**

- Simple prompts: Temperature 0.3
- Structured prompts: Temperature 0.1
- Max tokens: 2000

#### Step 4: Validate Results

**For Simple Prompts:**

- [ ] Output is immediately usable without editing
- [ ] Format matches prompt examples
- [ ] Content quality is professional
- [ ] All requested elements are present

**For Structured Prompts:**

- [ ] Valid JSON/CSV format
- [ ] All required fields present
- [ ] Data types match schema
- [ ] Error cases handled gracefully

## Test Input Guidelines

### Quality Standards for Test Inputs

**Good test input characteristics:**

- **Realistic** - Represents actual user scenarios
- **Complete** - Contains all information prompt expects
- **Specific** - Detailed enough for quality output
- **Varied** - Covers different complexity levels

**Example of good test input:**

```
Business concept: AI-powered meal planning app for busy professionals
Target market: Urban professionals aged 25-45 who work 50+ hours per week
Revenue model: Subscription at $9.99/month with premium tier at $19.99/month
Key features: Personalized meal plans, grocery list generation, nutrition tracking
Competition: MyFitnessPal, Lose It, traditional meal kit services
Budget: $50,000 personal savings, considering seed round
Timeline: 6 months to MVP
```

**Example of poor test input:**

```
Business idea: Make an app
```

### Creating New Test Inputs

1. **Identify gap** - What scenarios aren't covered?
2. **Research realistic details** - Use actual business/educational scenarios
3. **Follow naming convention** - `[descriptive-name].txt`
4. **Place in correct category** - `tests/inputs/[category]/`
5. **Test with multiple prompts** - Ensure broadly useful

## Golden Output Management

### What Are Golden Outputs?

Benchmark examples of high-quality prompt results used for:

- **Quality comparison** - Is new output as good as this?
- **Regression testing** - Did changes break anything?
- **Platform comparison** - How do different AIs compare?

### Creating Golden Outputs

#### Step 1: Generate High-Quality Output

1. Use test input with prompt
2. Test on ChatGPT 4 and Claude 3
3. Select best result (or merge best elements)
4. Verify output meets all quality standards

#### Step 2: Format as Golden File

Create: `tests/outputs/golden/[prompt-name]/case-001.json`

**For Simple Prompts:**

```json
{
  "_meta": {
    "prompt": "business-plan-simple",
    "version": "1.0.0",
    "test_input": "business-idea-1.txt",
    "last_updated": "2025-09-05",
    "platform_tested": "ChatGPT 4",
    "quality_score": "high"
  },
  "output": {
    "content": "actual AI output text here",
    "word_count": 187,
    "includes_metrics": true,
    "professional_tone": true,
    "actionable_content": true
  }
}
```

**For Structured Prompts:**

```json
{
  "_meta": {
    "prompt": "sentiment-analysis",
    "version": "1.0.0",
    "test_input": "positive-review.txt",
    "last_updated": "2025-09-05",
    "platform_tested": "Claude 3",
    "quality_score": "high"
  },
  "output": {
    "text": "input text that was analyzed",
    "sentiment": "positive",
    "confidence": "high",
    "word_count": 16,
    "language_detected": "english"
  }
}
```

#### Step 3: Validate

```bash
python3 scripts/validate_json_examples.py
```

## Cross-Platform Testing

### Platform Differences to Watch

**ChatGPT 4:**

- Strengths: Consistent formatting, business writing
- Weaknesses: Sometimes verbose
- Best for: Simple prompts, business content

**Claude 3:**

- Strengths: Structured data, analytical thinking
- Weaknesses: Can be overly detailed
- Best for: Structured prompts, data analysis

**Gemini Pro:**

- Strengths: Creative content, varied approaches
- Weaknesses: Less consistent formatting
- Best for: Creative prompts, brainstorming

### Consistency Checks

**Acceptable differences:**

- Minor wording variations
- Different examples (as long as quality is similar)
- Slightly different detail levels

**Unacceptable differences:**

- Different JSON schema or field names
- Significantly different quality levels
- Missing key information on one platform
- Instructions that only work on one platform

## Test Categories

### File Structure Tests

```bash
python3 tests/test-runner.py
```

- Verifies all required directories exist
- Checks file naming conventions
- Validates folder organization

### Format Validation Tests

```bash
python3 scripts/validate_json_examples.py
```

- JSON syntax validation
- Required field presence
- Data type consistency

### Quality Assurance Tests

_Manual process_

- Output usefulness
- Instruction clarity
- Cross-platform consistency

## Troubleshooting Tests

### Common Test Failures

**"JSON validation failed"**

- Cause: Syntax error in golden output file
- Fix: Use online JSON validator to find error
- Prevention: Copy-paste actual AI output

**"Test file not found"**

- Cause: File in wrong location or wrong name
- Fix: Check path matches `tests/inputs/[category]/[name].txt`
- Prevention: Follow exact naming convention

**"No golden outputs found"**

- Cause: Normal for new prompts
- Fix: Create golden outputs using process above
- Note: This is a warning, not an error

### Debug Mode

```bash
# Verbose output for debugging
python3 tests/test-runner.py --category business -v

# Test single file
python3 tests/test-runner.py --test-file tests/inputs/business/business-idea-1.txt
```

## Quality Standards

### Minimum Requirements (Must Pass)

- [ ] All JSON files validate
- [ ] Test inputs are readable
- [ ] File structure is complete
- [ ] No broken links in documentation

### Quality Goals (Should Achieve)

- [ ] 90%+ outputs usable without editing
- [ ] Cross-platform consistency >85%
- [ ] User satisfaction >4.0/5.0
- [ ] Response time <30 seconds

### Excellence Indicators (Nice to Have)

- [ ] Outputs exceed user expectations
- [ ] Zero user confusion on instructions
- [ ] Consistent quality across all test cases
- [ ] Community adoption and positive feedback

## Testing Workflow for Contributors

### Before Submitting New Prompt

1. **Create test inputs** - At least 2 realistic scenarios
2. **Test manually** - ChatGPT 4 and Claude 3 minimum
3. **Create golden outputs** - Document expected results
4. **Run validation** - `python3 tests/test-runner.py`
5. **Fix any issues** - Ensure all tests pass

### Before Modifying Existing Prompt

1. **Run current tests** - Establish baseline
2. **Make changes** - Modify prompt carefully
3. **Re-test** - Same test inputs, compare results
4. **Update golden outputs** - If intentional improvement
5. **Document changes** - Why change was made

### Regular Maintenance

- **Weekly:** `bash scripts/run-all-tests.sh`
- **Monthly:** Manual spot-check of sample prompts
- **Before releases:** Full manual testing of critical prompts

## Getting Help

**Test failures you can't resolve:**

1. Check [TROUBLESHOOTING.md](../TROUBLESHOOTING.md)
2. Search existing GitHub issues
3. Create new issue with:
   - Exact command that failed
   - Full error message
   - Operating system and Python version

**Questions about testing process:**

- [GitHub Discussions](../../discussions)
- [Contributing Guide](../CONTRIBUTING.md)

Remember: Testing helps us maintain quality, but it's not about perfection. The goal is catching obvious problems before users encounter them!
