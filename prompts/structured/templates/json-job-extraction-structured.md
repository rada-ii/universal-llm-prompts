---
title: JSON Job Extraction - Structured Template
type: structured
category: classification|templates|advanced
last_updated: 2025-09-05
tested_platforms: ["ChatGPT 4", "Claude 3"]
target_users: ["developers", "analysts"]
output_format: json|csv
schema_version: "1.0"
---

[COMPAT HEADER — STRUCTURED OUTPUT (JSON)]

- Output must be JSON only; first character must be {.
- On failure, return only: {"error":"format_violation","note":"why"}.
  [/COMPAT]

# JSON Job Extraction - Structured Template

## Purpose

Convert job postings into structured JSON with confidence scoring and comprehensive error handling.

## Template

<system>JSON only, no code fence, no extra text.</system>
<schema>{"title":"string","company":"string","location":"string",
"salary_min":"number|null","salary_max":"number|null","salary_currency":"string|null",
"work_mode":"remote|hybrid|onsite|null","remote":"boolean|null",
"skills":"string[]","experience_years":"number|null","education_required":"string|null",
"application_deadline":"YYYY-MM-DD|null","job_type":"full_time|part_time|contract|null",
"benefits":"string[]","clarifying_question":"string|null","parsing_confidence":"high|medium|low"}</schema>
<rules>

- missing_data=null; boolean=true/false; dates=YYYY-MM-DD format only
- salary_parsing: remove currency symbols ($,£,€) and commas; k=×1000, m=×1000000;
  examples: "120k"→120000, "$1.5M"→1500000, "€45,000"→45000
- hourly_to_annual: multiply hourly rate by 2080 (40h/week × 52weeks)
- salary_ranges: "120k-180k" → salary_min:120000, salary_max:180000
- vague_salary: "competitive/negotiable/DOE/inquire" → salary_min:null, salary_max:null
- skills: lowercase, unique, max 10 items, most relevant first, remove duplicates
- work_mode_mapping: "remote/WFH/from home/fully remote" → remote; "hybrid/mixed/flexible/part remote" → hybrid; "office/onsite/in-person/on-site" → onsite
- remote_boolean: true if work_mode="remote", false if "onsite", null if "hybrid" or unclear
- experience_parsing: "5+ years" → 5, "3-5 years" → 3, "entry level/junior" → 0, "senior" → 5
- education_mapping: "bachelor's/degree/BA/BS" → "bachelors", "master's/MBA/MS" → "masters", "PhD/doctorate" → "phd"
- job_type_mapping: "full-time/permanent/FTE" → "full_time", "part-time/PT" → "part_time", "contractor/freelance/temp" → "contract"
- benefits: extract specific benefits mentioned, max 5 items
- confidence_criteria: high=all fields clear, medium=some assumptions made, low=multiple ambiguities
- ambiguous_input: output only {"clarifying_question":"specific question about unclear fields","parsing_confidence":"low"}
- currency_detection: detect from salary format ($=USD, £=GBP, €=EUR)
  </rules>
  <error_handling>
  If insufficient data: {"error":"insufficient_data","available_fields":["field1"],"minimum_required":["title","company"]}
  If completely unclear: {"clarifying_question":"What specific information can you provide about job title, company, and location?","parsing_confidence":"low"}
  If parsing errors: {"error":"parsing_error","issue":"specific problem description","raw_text":"problematic section"}
  </error_handling>
  <data>{{JOB_POSTING_TEXT}}</data>

## Test Cases

### Complete Job Posting

Input:

```
Senior React Developer at Meta, Menlo Park CA
Salary: $120k-180k annually, Full remote available
Requirements: React, TypeScript, GraphQL, 5+ years experience
Bachelor's degree preferred
Benefits: Health insurance, 401k, unlimited PTO
Apply by December 15, 2024
```

Expected:

```json
{
  "title": "Senior React Developer",
  "company": "Meta",
  "location": "Menlo Park CA",
  "salary_min": 120000,
  "salary_max": 180000,
  "salary_currency": "USD",
  "work_mode": "remote",
  "remote": true,
  "skills": ["react", "typescript", "graphql"],
  "experience_years": 5,
  "education_required": "bachelors",
  "application_deadline": "2024-12-15",
  "job_type": "full_time",
  "benefits": ["health insurance", "401k", "unlimited pto"],
  "clarifying_question": null,
  "parsing_confidence": "high"
}
```

### Minimal Information

Input:

```
Software Engineer at TechCorp
Location: London, hybrid working
Salary: £45k-60k + benefits
Skills: JavaScript, Python, AWS
```

Expected:

```json
{
  "title": "Software Engineer",
  "company": "TechCorp",
  "location": "London",
  "salary_min": 45000,
  "salary_max": 60000,
  "salary_currency": "GBP",
  "work_mode": "hybrid",
  "remote": null,
  "skills": ["javascript", "python", "aws"],
  "experience_years": null,
  "education_required": null,
  "application_deadline": null,
  "job_type": "full_time",
  "benefits": ["benefits"],
  "clarifying_question": null,
  "parsing_confidence": "medium"
}
```

### Vague/Ambiguous Posting

Input:

```
XYZ Corp seeks programmer
Location: flexible
Salary: depends on experience
Tech: modern stack
Apply soon
```

Expected:

```json
{
  "clarifying_question": "Could you provide more specific information about the job title, required technologies, salary range, and application deadline?",
  "parsing_confidence": "low"
}
```

### European Format

Input:

```
Frontend Developer - Part Time
Company: Berlin Startup GmbH
Location: Berlin, Germany (office-based)
Salary: €40.000 - €55.000 per year
Requirements: Vue.js, 3+ years experience, Master's degree
Contract: 20 hours/week
Benefits: Flexible hours, training budget
```

Expected:

```json
{
  "title": "Frontend Developer",
  "company": "Berlin Startup GmbH",
  "location": "Berlin, Germany",
  "salary_min": 40000,
  "salary_max": 55000,
  "salary_currency": "EUR",
  "work_mode": "onsite",
  "remote": false,
  "skills": ["vue.js"],
  "experience_years": 3,
  "education_required": "masters",
  "application_deadline": null,
  "job_type": "part_time",
  "benefits": ["flexible hours", "training budget"],
  "clarifying_question": null,
  "parsing_confidence": "high"
}
```

### Contract Position

Input:

```
Senior DevOps Engineer (Contract)
Remote worldwide, 6-month contract
Rate: $80-100/hour
Skills: Kubernetes, Docker, AWS, Terraform
10+ years experience required
Security clearance preferred
```

Expected:

```json
{
  "title": "Senior DevOps Engineer",
  "company": null,
  "location": "Remote worldwide",
  "salary_min": 166400,
  "salary_max": 208000,
  "salary_currency": "USD",
  "work_mode": "remote",
  "remote": true,
  "skills": ["kubernetes", "docker", "aws", "terraform"],
  "experience_years": 10,
  "education_required": null,
  "application_deadline": null,
  "job_type": "contract",
  "benefits": [],
  "clarifying_question": null,
  "parsing_confidence": "medium"
}
```

### Error Case - Insufficient Data

Input:

```
Job available
Good pay
```

Expected:

```json
{
  "error": "insufficient_data",
  "available_fields": [],
  "minimum_required": ["title", "company"]
}
```
