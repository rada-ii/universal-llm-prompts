[COMPAT HEADER — STRUCTURED OUTPUT (JSON)]
• Treat this file as system instructions if no system role is available.
• Output must be JSON only; first character must be {.
• Unknown/unused fields → null (do not omit required keys).
• On failure, return only: {"error":"format_violation","note":"why"}.
[/COMPAT]

# JSON Job Extraction Template

## Purpose

Convert job postings into structured JSON with confidence scoring and error handling.

## Template

<system>JSON only, no code fence, no extra text.</system>
<schema>{"title":"string","company":"string","location":"string",
"salary_min":"number|null","salary_max":"number|null",
"work_mode":"remote|hybrid|onsite|null","remote":"boolean|null",
"skills":"string[]","application_deadline":"YYYY-MM-DD|null",
"clarifying_question":"string|null","parsing_confidence":"high|medium|low"}</schema>
<rules>

- missing_data=null; boolean=true/false; dates=YYYY-MM-DD format only
- salary_parsing: remove $,£,€ symbols and commas; k=×1000, m=×1000000 (120k→120000, 1.5m→1500000)
- salary_ranges: "120k-180k" → salary_min:120000, salary_max:180000
- vague_salary: "competitive/negotiable/DOE/inquire" → salary_min:null, salary_max:null
- skills: lowercase, unique, max 10 items, most relevant first
- work_mode_mapping: "remote/WFH/from home" → remote; "hybrid/mixed/flexible" → hybrid; "office/onsite/in-person" → onsite
- remote_boolean: true if work_mode="remote", false if "onsite", null if "hybrid" or unclear
- confidence_criteria: high=all fields clear, medium=some assumptions made, low=multiple ambiguities
- ambiguous_input: output only {"clarifying_question":"specific question about unclear fields","parsing_confidence":"low"}
  </rules>
  <data>{{JOB_POSTING_TEXT}}</data>

## Test Cases

Happy Path

Input:

Senior React Developer at Meta, Menlo Park CA
Salary: $120k-180k annually, Full remote available
Requirements: React, TypeScript, GraphQL, 5+ years experience
Apply by December 15, 2024

Expected Output:

{
"title": "Senior React Developer",
"company": "Meta",
"location": "Menlo Park CA",
"salary_min": 120000,
"salary_max": 180000,
"work_mode": "remote",
"remote": true,
"skills": ["react", "typescript", "graphql"],
"application_deadline": "2024-12-15",
"clarifying_question": null,
"parsing_confidence": "high"
}
