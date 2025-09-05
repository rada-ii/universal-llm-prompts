---
title: Support Ticket Routing - Few-Shot Template
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

# Support Ticket Routing - Few-Shot Template

## Purpose

Categorize customer support tickets with confidence scoring.

## Template

<s>JSON only, no extra text.</s>
<schema>{"text":"string","category":"billing|technical|shipping|sales|refund|account|other","confidence":"high|medium|low"}</schema>
<examples>
{"text":"My credit card was charged twice for the same order.","category":"billing","confidence":"high"}
{"text":"The website keeps crashing when I try to checkout.","category":"technical","confidence":"high"}
{"text":"Where is my package? Tracking shows no updates.","category":"shipping","confidence":"high"}
{"text":"Do you offer discounts for students or bulk orders?","category":"sales","confidence":"high"}
{"text":"I want to return this item and get my money back.","category":"refund","confidence":"high"}
{"text":"I can't login to my account, forgot my password.","category":"account","confidence":"high"}
{"text":"Something weird happened but I'm not sure what.","category":"other","confidence":"low"}
{"text":"Is there a way to maybe change something? Not sure.","category":"other","confidence":"low"}
</examples>
<confidence_criteria>
high: clear keywords match category, specific issue described
medium: category likely but some ambiguity, mixed signals
low: vague description, multiple possible categories, unclear intent
</confidence_criteria>
<task>Classify the support ticket using the same JSON format.</task>
<input>{{SUPPORT_TICKET_TEXT}}</input>

## Test Cases

### Clear Category - Billing

Input: "Why was I charged $50 when the price showed $30 at checkout?"
Expected: {"text":"Why was I charged $50 when the price showed $30 at checkout?","category":"billing","confidence":"high"}

### Clear Category - Technical

Input: "Error 500 appears every time I click the submit button."
Expected: {"text":"Error 500 appears every time I click the submit button.","category":"technical","confidence":"high"}

### Medium Confidence

Input: "I ordered something but haven't received my confirmation email."
Expected: {"text":"I ordered something but haven't received my confirmation email.","category":"technical","confidence":"medium"}

### Low Confidence/Ambiguous

Input: "I have some questions about stuff, can you help?"
Expected: {"text":"I have some questions about stuff, can you help?","category":"other","confidence":"low"}

### Mixed Category Signals

Input: "My order was cancelled but I was still charged, and now I can't login to check status."
Expected: {"text":"My order was cancelled but I was still charged, and now I can't login to check status.","category":"billing","confidence":"medium"}
