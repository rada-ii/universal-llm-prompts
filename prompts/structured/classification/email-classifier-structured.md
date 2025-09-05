---
title: Email Classification - Structured Template
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

# Email Classification - Structured Template

## Purpose

Classify emails into actionable categories with priority and confidence scoring for automated workflow routing.

## Template

<s>JSON only, no extra text.</s>
<schema>{"subject":"string","category":"urgent|action_required|meeting|information|spam|promotion|personal|follow_up|other","priority":"critical|high|medium|low","confidence":"high|medium|low","suggested_action":"string","estimated_time":"string","business_hours":"boolean"}</schema>
<examples>
{"subject":"URGENT: Server down - all services affected","category":"urgent","priority":"critical","confidence":"high","suggested_action":"Immediate response required","estimated_time":"< 5 minutes","business_hours":false}
{"subject":"Please review and approve Q4 budget proposal","category":"action_required","priority":"high","confidence":"high","suggested_action":"Review document and respond","estimated_time":"15-30 minutes","business_hours":true}
{"subject":"Weekly team meeting - Tuesday 2pm","category":"meeting","priority":"medium","confidence":"high","suggested_action":"Add to calendar","estimated_time":"< 2 minutes","business_hours":true}
{"subject":"Industry newsletter - March 2024 edition","category":"information","priority":"low","confidence":"high","suggested_action":"Read when time permits","estimated_time":"10-15 minutes","business_hours":true}
{"subject":"You've won $1M! Click here now!","category":"spam","priority":"low","confidence":"high","suggested_action":"Delete","estimated_time":"< 1 minute","business_hours":false}
{"subject":"50% off all products this weekend only","category":"promotion","priority":"low","confidence":"high","suggested_action":"Review if interested","estimated_time":"2-5 minutes","business_hours":true}
{"subject":"Happy birthday! Hope you have a great day","category":"personal","priority":"low","confidence":"high","suggested_action":"Respond when convenient","estimated_time":"2-5 minutes","business_hours":false}
{"subject":"Following up on our conversation yesterday","category":"follow_up","priority":"medium","confidence":"high","suggested_action":"Review and respond to follow-up","estimated_time":"5-10 minutes","business_hours":true}
{"subject":"Fwd: Fwd: RE: Some random thoughts","category":"other","priority":"low","confidence":"medium","suggested_action":"Review to determine relevance","estimated_time":"5-10 minutes","business_hours":true}
</examples>
<classification_rules>
urgent: security issues, system failures, compliance deadlines, crisis situations
action_required: approvals needed, decisions required, tasks assigned, responses requested with deadlines
meeting: calendar invites, meeting confirmations, agenda items, scheduling requests
information: newsletters, updates, reports, FYI items, industry news, announcements
spam: obvious scams, phishing attempts, suspicious links, irrelevant promotional content
promotion: legitimate marketing emails, sales offers, product announcements, webinar invites
personal: messages from friends/family, non-work social content, personal celebrations
follow_up: responses to previous conversations, check-ins, status updates on ongoing topics
other: unclear purpose, mixed content, requires further review to categorize
</classification_rules>
<priority_criteria>
critical: system outages, security breaches, legal emergencies, immediate safety issues
high: urgent category items, CEO/executive requests, deadline today, compliance issues
medium: action required with reasonable timeline, scheduled meetings, important updates, follow-ups
low: informational content, promotions, personal messages, non-time-sensitive items
</priority_criteria>
<confidence_criteria>
high: clear indicators match category perfectly, obvious classification, standard patterns
medium: likely category but some ambiguity, mixed signals present, context dependent
low: unclear purpose, insufficient information, multiple possible categories, unusual format
</confidence_criteria>
<business_hours_logic>
true: requires business context, work-related action, professional response needed
false: personal matters, after-hours emergencies, spam, non-work communications
</business_hours_logic>
<error_handling>
If subject empty: {"error":"empty_subject","note":"Subject line is required for classification"}
If subject too vague: confidence = low, category = other
If multiple categories apply: choose primary category, note in suggested_action
If suspicious content detected: category = spam, priority = low
</error_handling>
<task>Classify the email subject line using the exact JSON format shown in examples.</task>
<input>{{EMAIL_SUBJECT}}</input>

## Test Cases

### Critical Urgent Email

Input: "CRITICAL: Data breach detected - immediate action required"
Expected: {"subject":"CRITICAL: Data breach detected - immediate action required","category":"urgent","priority":"critical","confidence":"high","suggested_action":"Immediate security response","estimated_time":"< 5 minutes","business_hours":false}

### High Priority Action

Input: "CEO needs Q4 numbers for board meeting tomorrow"
Expected: {"subject":"CEO needs Q4 numbers for board meeting tomorrow","category":"action_required","priority":"high","confidence":"high","suggested_action":"Prepare and send Q4 financial data","estimated_time":"30-60 minutes","business_hours":true}

### Meeting Invitation

Input: "Invitation: Project kickoff meeting - March 15 at 10am"
Expected: {"subject":"Invitation: Project kickoff meeting - March 15 at 10am","category":"meeting","priority":"medium","confidence":"high","suggested_action":"Accept and add to calendar","estimated_time":"< 2 minutes","business_hours":true}

### Newsletter/Information

Input: "Weekly DevOps digest - Latest tools and best practices"
Expected: {"subject":"Weekly DevOps digest - Latest tools and best practices","category":"information","priority":"low","confidence":"high","suggested_action":"Read when time permits","estimated_time":"10-15 minutes","business_hours":true}

### Obvious Spam

Input: "Congratulations! You've inherited $5 million from Nigerian prince"
Expected: {"subject":"Congratulations! You've inherited $5 million from Nigerian prince","category":"spam","priority":"low","confidence":"high","suggested_action":"Delete immediately","estimated_time":"< 1 minute","business_hours":false}

### Legitimate Promotion

Input: "New features in our project management tool - 30% discount"
Expected: {"subject":"New features in our project management tool - 30% discount","category":"promotion","priority":"low","confidence":"high","suggested_action":"Review if tool is relevant","estimated_time":"5-10 minutes","business_hours":true}

### Personal Email

Input: "Thanks for dinner last night! Had a great time"
Expected: {"subject":"Thanks for dinner last night! Had a great time","category":"personal","priority":"low","confidence":"high","suggested_action":"Respond when convenient","estimated_time":"2-5 minutes","business_hours":false}

### Follow-up Email

Input: "Following up on proposal we discussed last week"
Expected: {"subject":"Following up on proposal we discussed last week","category":"follow_up","priority":"medium","confidence":"high","suggested_action":"Review proposal status and respond","estimated_time":"10-15 minutes","business_hours":true}

### Ambiguous/Low Confidence

Input: "RE: That thing we discussed"
Expected: {"subject":"RE: That thing we discussed","category":"other","priority":"low","confidence":"low","suggested_action":"Review full email content","estimated_time":"5-10 minutes","business_hours":true}

### Empty Subject Error

Input: ""
Expected: {"error":"empty_subject","note":"Subject line is required for classification"}

### Complex Business Context

Input: "URGENT: Board meeting moved to Friday - please confirm your Q4 numbers are ready for presentation to investors"
Expected: {"subject":"URGENT: Board meeting moved to Friday - please confirm your Q4 numbers are ready for presentation to investors","category":"action_required","priority":"high","confidence":"high","suggested_action":"Prepare Q4 financial data for Friday board meeting","estimated_time":"2-4 hours","business_hours":true}

### Mixed Category Signals

Input: "Reminder: Team building event next week - please RSVP and submit your expense reports"
Expected: {"subject":"Reminder: Team building event next week - please RSVP and submit your expense reports","category":"action_required","priority":"medium","confidence":"medium","suggested_action":"RSVP for event and submit expense reports","estimated_time":"15-30 minutes","business_hours":true}
