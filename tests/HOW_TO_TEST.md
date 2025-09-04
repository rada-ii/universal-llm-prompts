# How to Test Universal LLM Prompts

## Testing Overview

Testing validates that prompts produce consistent, useful results across different AI platforms and user scenarios.

## Quick Testing Process

### 1. Choose Prompt and Test Input

```
Prompt: prompts/simple/business/business-plan-simple.md
Test Input: tests/inputs/business/business-idea-1.txt
Expected: Professional business plan section
```

### 2. Prepare the Prompt

- Copy entire prompt file content
- Replace `{{VARIABLES}}` with test input content
- Do not modify prompt structure

### 3. Test Across Platforms

**Required Platforms:**

- ChatGPT 4 (primary)
- Claude 3 (primary)

**Optional:**

- Gemini Pro
- GPT-3.5

**Settings:**

- Simple prompts: Temperature 0.3
- Structured prompts: Temperature 0.1
- Max tokens: 2000

### 4. Validate Results

**Simple Prompts:**

- [ ] Output is immediately usable
- [ ] Format matches expected type (email, plan, etc.)
- [ ] Content quality is professional
- [ ] No obvious errors or hallucinations

**Structured Prompts:**

- [ ] Valid JSON/CSV format
- [ ] All required fields present
- [ ] Data types match schema
- [ ] Error cases handled properly

### 5. Document Results

Save outputs to `tests/outputs/[category]/[test-case]-[platform].json`

## Comprehensive Testing Framework

### Test Categories

**Functionality Tests:**

- Core prompt behavior
- Edge case handling
- Cross-platform consistency

**Quality Tests:**

- Output usefulness
- Professional standards
- Accuracy verification

**Performance Tests:**

- Response time
- Token efficiency
- Reliability metrics

### Testing Matrix

| Prompt Type      | ChatGPT 4 | Claude 3 | Gemini Pro | Pass Criteria   |
| ---------------- | --------- | -------- | ---------- | --------------- |
| Simple Business  | Required  | Required | Optional   | Usable document |
| Simple Education | Required  | Required | Optional   | Teaching-ready  |
| Structured Data  | Required  | Required | Optional   | Valid schema    |
| Classification   | Required  | Required | Optional   | Accurate labels |

### Automated Testing Setup

**validation.js**

```javascript
// JSON schema validation
function validateJSON(output, schema) {
  try {
    const parsed = JSON.parse(output);
    return validateSchema(parsed, schema);
  } catch (e) {
    return { valid: false, error: e.message };
  }
}
```

**test-runner.py**

```python
# Automated prompt testing
def run_test_suite(prompt_file, test_inputs, platforms):
    results = {}
    for platform in platforms:
        for test_input in test_inputs:
            result = execute_prompt(prompt_file, test_input, platform)
            results[f"{platform}_{test_input}"] = validate_result(result)
    return results
```

## Error Testing

### Common Error Scenarios

**For Structured Prompts:**

- Empty input: `""`
- Invalid format: `"random text not matching expected format"`
- Incomplete data: `"Job title: Engineer"` (missing other fields)
- Malformed input: `"Salary: $ABC"` (non-numeric salary)

**For Simple Prompts:**

- Insufficient context: `"Write business plan"` (no details)
- Contradictory requirements: `"Simple but comprehensive plan"`
- Unrealistic constraints: `"$0 budget, unlimited features"`

### Expected Error Handling

**Structured Prompts Should Return:**

```json
{
  "error": "insufficient_data",
  "missing_fields": ["company", "salary"],
  "confidence": "low"
}
```

**Simple Prompts Should:**

- Request clarification
- Provide best effort with available info
- Include assumptions made

## Quality Benchmarks

### Minimum Standards

**Simple Prompts:**

- 90% of outputs usable without editing
- Cross-platform consistency score > 0.8
- User satisfaction rating > 4.0/5.0

**Structured Prompts:**

- 95% valid JSON/CSV format
- 100% schema compliance when successful
- Error rate < 5% on well-formed inputs

### Performance Targets

| Metric           | Target            | Measurement         |
| ---------------- | ----------------- | ------------------- |
| Response Time    | < 30 seconds      | Platform API timing |
| Token Efficiency | < 2000 tokens     | Token counting      |
| Success Rate     | > 95%             | Validation passing  |
| Cross-Platform   | > 90% consistency | Output comparison   |

## Test Case Development

### Creating New Test Cases

**Input Requirements:**

- Realistic scenarios
- Edge cases included
- Multiple difficulty levels
- Industry-specific examples

**Example Test Suite Structure:**

```
tests/inputs/business/
├── simple-business-idea.txt          # Basic case
├── complex-business-model.txt        # Advanced case
├── incomplete-information.txt        # Error case
├── unrealistic-constraints.txt       # Edge case
└── industry-specific-saas.txt        # Domain case
```

### Test Input Guidelines

**Good Test Input:**

```
Business idea: AI-powered meal planning app
Target market: Urban professionals aged 25-45
Revenue model: Subscription $9.99/month
Key features: Personalized meal plans, grocery integration
```

**Poor Test Input:**

```
Make business plan for app
```

## Regression Testing

### When to Run Full Test Suite

- Before major releases
- After prompt modifications
- Platform updates
- Weekly quality checks

### Automated Regression Setup

```bash
#!/bin/bash
# run-regression.sh
for prompt in prompts/**/*.md; do
  echo "Testing $prompt"
  python test-runner.py --prompt="$prompt" --platforms="chatgpt,claude"
  if [ $? -ne 0 ]; then
    echo "FAILED: $prompt"
    exit 1
  fi
done
echo "All tests passed"
```

## Reporting and Metrics

### Test Report Format

```json
{
  "test_run_id": "2024-01-15-v1.2",
  "timestamp": "2024-01-15T10:30:00Z",
  "summary": {
    "total_tests": 156,
    "passed": 149,
    "failed": 7,
    "success_rate": 95.5
  },
  "platform_breakdown": {
    "chatgpt_4": { "passed": 52, "failed": 1 },
    "claude_3": { "passed": 51, "failed": 2 },
    "gemini_pro": { "passed": 46, "failed": 4 }
  },
  "failed_tests": [
    {
      "prompt": "email-classifier.md",
      "platform": "gemini_pro",
      "error": "invalid_json_format",
      "input": "tests/inputs/emails/spam-example.txt"
    }
  ]
}
```

### Quality Tracking

**Key Metrics:**

- Success rate trends
- Platform reliability scores
- Response time averages
- User feedback scores
- Error pattern analysis

This testing framework ensures prompt reliability and maintains quality standards across all supported platforms and use cases.
