# Testing Explained for Beginners

## What is Testing and Why Do We Need It?

**Simple explanation:** Testing means checking that our prompts work correctly and give good results to users.

Imagine you wrote a recipe. Testing would be like:

1. Having different people try the recipe
2. Checking if they all get tasty food
3. Making sure the instructions are clear
4. Fixing anything that doesn't work

## Why Test LLM Prompts?

### Problem: AI Models Can Be Unpredictable

- Same prompt might work great on ChatGPT but poorly on Claude
- Small changes in wording can dramatically change results
- What works for you might confuse other users

### Solution: Systematic Testing

- Test prompts on multiple AI platforms
- Use realistic scenarios (not just simple examples)
- Check that non-technical users can follow instructions
- Verify outputs are actually useful

## Our Testing Strategy (Simple Version)

### 1. Input Testing

**What:** Check that test input files are realistic and complete
**Why:** Garbage in = garbage out
**How:** We have test files like `business-idea-1.txt` with realistic scenarios

### 2. Output Validation

**What:** Check that AI responses are in the right format
**Why:** JSON should be valid JSON, emails should look like emails
**How:** Automated scripts check file formats

### 3. Quality Checking

**What:** Verify that outputs are actually useful
**Why:** Technically correct but useless results help nobody
**How:** Manual review by real users

### 4. Cross-Platform Testing

**What:** Same prompt tested on ChatGPT, Claude, and Gemini
**Why:** Users use different AI platforms
**How:** Run same test on multiple platforms, compare results

## File Structure Explained

```
tests/
├── inputs/                 # Test data we feed to prompts
│   ├── business/          # Business scenario test cases
│   ├── education/         # Education scenario test cases
│   └── ...               # One folder per prompt category
├── outputs/               # What we expect to get back
│   ├── golden/           # "Perfect" examples of good output
│   └── runs/             # Actual test results (temporary)
└── test-runner.py        # Script that runs tests automatically
```

### Test Inputs (`tests/inputs/`)

**Purpose:** Realistic scenarios to test prompts with
**Example:** `business-idea-1.txt` contains a detailed business concept
**Why needed:** Better than testing with "write business plan for my company"

### Golden Outputs (`tests/outputs/golden/`)

**Purpose:** Examples of what good results should look like
**Example:** Perfect business plan output for `business-idea-1.txt`
**Why needed:** So we know when something gets worse

### Test Runner (`tests/test-runner.py`)

**Purpose:** Automatically checks files and runs basic validations
**What it does:**

- Checks that input files are readable
- Validates JSON files are properly formatted
- Counts how many tests we have
- Reports any obvious problems

## How to Run Tests

### Quick Test (2 minutes)

```bash
# From project root directory
bash scripts/run-all-tests.sh
```

This checks file formats and structure automatically.

### Manual Quality Test (15 minutes)

1. Pick a prompt (e.g., `business-plan-simple.md`)
2. Use test input (e.g., `business-idea-1.txt`)
3. Run prompt on ChatGPT 4
4. Run same prompt on Claude 3
5. Compare results - are they both useful?

### Full Test Suite (1 hour)

Test all prompts with all test inputs on multiple platforms.

## What Our Scripts Actually Do

### `scripts/validate_json_examples.py`

**Purpose:** Check that all JSON files are valid
**What it checks:**

- Can the file be opened?
- Is the JSON syntax correct?
- Are there any obvious formatting errors?

**When to run:** After adding new golden output files

### `tests/test-runner.py`

**Purpose:** Validate test files and structure
**What it checks:**

- Are test input files readable?
- Do we have test cases for each prompt category?
- Are golden output files properly formatted?
- Is the file structure complete?

**When to run:** Before submitting changes

### `scripts/run-all-tests.sh`

**Purpose:** Complete automated test suite
**What it does:**

- Runs all other validation scripts
- Checks file structure
- Counts prompts and test cases
- Reports overall project health

**When to run:** Weekly, or before releases

## Understanding Test Results

###  Green (Good)

- Files are properly formatted
- Structure looks correct
- Basic validations pass

### ⚠️ Yellow (Warning)

- Something might be missing but not critical
- Manual review recommended
- Often happens with new prompts that don't have golden outputs yet

###  Red (Problem)

- Something is broken and needs fixing
- Could be invalid JSON, missing files, or structural issues
- Must be fixed before release

## Creating Test Cases (Step by Step)

### Step 1: Create Test Input

1. Go to `tests/inputs/[category]/`
2. Create new file: `descriptive-name.txt`
3. Fill with realistic, detailed scenario
4. **Good example:**
   ```
   Business concept: AI-powered meal planning app
   Target market: Busy professionals aged 25-45
   Budget: $50,000 initial funding
   Timeline: 6 months to MVP
   Competition: MyFitnessPal, Lose It
   ```

### Step 2: Test Manually

1. Use your test input with the prompt
2. Run on ChatGPT 4 and Claude 3
3. Save the best result

### Step 3: Create Golden Output (for structured prompts)

1. Go to `tests/outputs/golden/[prompt-name]/`
2. Create file: `case-001.json`
3. Format with metadata:
   ```json
   {
     "_meta": {
       "prompt": "business-plan-simple",
       "version": "1.0.0",
       "test_input": "business-idea-1.txt",
       "last_updated": "2025-09-05"
     },
     "output": {
       "actual_ai_response": "goes here"
     }
   }
   ```

### Step 4: Validate

```bash
python3 scripts/validate_json_examples.py
```

## Common Testing Problems

### Problem: "JSON validation failed"

**Cause:** Syntax error in JSON file
**Fix:** Use online JSON validator to find the error
**Prevention:** Copy-paste actual AI output, don't type manually

### Problem: "No test files found"

**Cause:** Files in wrong directory or wrong naming
**Fix:** Check file is in `tests/inputs/[category]/` and ends with `.txt`
**Prevention:** Follow exact naming convention

### Problem: "Test input file unreadable"

**Cause:** File encoding or permission issues
**Fix:** Save file as UTF-8 plain text
**Prevention:** Use simple text editor, not Word

## What We Don't Test (And Why)

### We DON'T Test:

- **AI model responses automatically** - Would require API keys and costs money
- **Subjective quality** - "Is this email friendly enough?" needs human judgment
- **Real-time AI behavior** - Models change over time
- **User preferences** - Different users want different styles

### We DO Test:

- **File formats** - JSON must be valid JSON
- **Structure completeness** - All required files present
- **Basic functionality** - Can files be read and processed
- **Cross-platform compatibility** - Same prompt works on different AIs

## Best Practices for Testing

### 1. Test Early and Often

- Test new prompts immediately after creation
- Don't wait until you have 10 prompts to test

### 2. Use Realistic Scenarios

- Test inputs should represent real user problems
- Include edge cases (missing info, unusual requests)

### 3. Document Everything

- If a test fails, note why and how you fixed it
- Keep examples of good and bad outputs

### 4. Test on Multiple Platforms

- Minimum: ChatGPT 4 and Claude 3
- Bonus: Test on Gemini Pro for completeness

### 5. Get Outside Perspective

- Have someone else try your prompts
- Fresh eyes catch problems you miss

## Continuous Improvement

### Weekly Health Check

```bash
bash scripts/run-all-tests.sh
```

### Monthly Deep Dive

- Test sample prompts manually on all platforms
- Review user feedback and common issues
- Update golden outputs if needed

### Before Each Release

- Full test suite must pass
- All new prompts must have test cases
- Documentation must be current

## Getting Help with Testing

### If Tests Keep Failing:

1. Read the error message carefully
2. Check `TROUBLESHOOTING.md` for common solutions
3. Verify you're following file naming conventions
4. Try testing just one prompt at a time

### If You're Confused:

1. Start with the simplest test: `python3 tests/test-runner.py --category business`
2. Look at existing test files for examples
3. Ask for help in GitHub discussions

Remember: Testing isn't about perfection - it's about catching obvious problems before users encounter them!
