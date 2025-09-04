# How to Test Universal LLM Prompts

## What is testing?

Testing means taking a prompt template and giving it real content to see if it produces useful results.

## Step-by-step testing process:

### 1. Choose a prompt to test

Example: `prompts/templates/json-job-extraction.md`

### 2. Find matching test input

Example: `tests/inputs/jobs/sample-job-1.txt`

### 3. Prepare the prompt

- Copy the entire prompt file
- Replace `{{JOB_POSTING_TEXT}}` with content from the test file

### 4. Test with an AI

- Open ChatGPT, Claude, or another LLM
- Paste the prepared prompt
- Set temperature to 0-0.2 for consistent results

### 5. Save the result

- Copy the AI's response
- Save to `tests/outputs/jobs/sample-job-1-result.json`

### 6. Validate the result

Check if the output:

- Is in the expected format (JSON/readable text)
- Contains useful information
- Can be used for its intended purpose

## Example test run:

**Prompt:** json-job-extraction.md
**Input:** "Senior React Developer at Meta, $120k-180k, Remote"
**Expected output:** Valid JSON with job details
**Actual result:** Save to outputs folder and check format

## Success criteria:

- Output is correctly formatted
- Information is accurately extracted
- Result is useful for intended audience
- No errors or hallucinated data

## What to do with failed tests:

1. Check if prompt instructions are clear
2. Verify input data quality
3. Test with different AI models
4. Adjust prompt if needed
5. Document any issues found
