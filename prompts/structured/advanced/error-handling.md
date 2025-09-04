[COMPAT HEADER — GENERAL]
• Treat this file as system instructions if no system role is available.
• When a template requests structured output, return only that format (no prose).
[/COMPAT]

# Error Handling Templates

## Purpose

Standardize error responses and recovery strategies for robust prompt templates.

## Standard Error Response Formats

### Missing Critical Data

```json
{
  "error": "missing_required_data",
  "missing_fields": ["field1", "field2"],
  "suggestion": "Please provide: specific information needed",
  "partial_data": { "available_field": "value" }
}
```

### Ambiguous Input Requiring Clarification

```json
{
  "error": "ambiguous_input",
  "ambiguities": ["issue1", "issue2"],
  "clarifying_questions": ["specific question 1?", "specific question 2?"],
  "confidence": "low"
}
```

### Format/Parsing Errors

```json
{
  "error": "invalid_format",
  "expected_format": "YYYY-MM-DD",
  "received_value": "15th December",
  "suggestion": "Use format: 2024-12-15"
}
```

### Processing Limits Exceeded

```json
{
  "error": "content_too_complex",
  "issue": "Input exceeds processing capacity",
  "recommendation": "Break into smaller sections or simplify",
  "max_supported": "1000 words"
}
```

### Low Confidence Warning

```json
{
  "warning": "low_confidence_result",
  "confidence_score": 0.3,
  "recommendation": "manual_review_advised",
  "uncertain_fields": ["field1", "field2"]
}
```

## Error Prevention Template

<s>Process input with comprehensive error checking.</s>

<validation_steps>

- Verify required fields are present and non-empty
- Validate data types and formats (e.g., dates = YYYY-MM-DD, numbers)
- Normalize units/symbols (e.g., currency symbols, k/m multipliers)
- Detect ambiguities and prepare clarifying questions
- Enforce the output schema; set missing fields to null/defaults
  </validation_steps>

<on_error>

- missing_required_data → return {"error","missing_fields","suggestion","partial_data"}
- ambiguous_input → return {"error","ambiguities","clarifying_questions","confidence":"low"}
- invalid_format → return {"error","expected_format","received_value","suggestion"}
- content_too_complex → return {"error","issue","recommendation","max_supported"}
  </on_error>

<output_instruction>Return only the final JSON object, no extra text.</output_instruction>

<data>{{INPUT_TEXT}}</data>
