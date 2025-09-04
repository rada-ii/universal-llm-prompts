[COMPAT HEADER — STRUCTURED OUTPUT (JSON)]
• Output must be JSON only; first character must be {.
• On failure, return only: {"error":"format_violation","note":"why"}.
[/COMPAT]

# Email Classification - Structured Template

## Purpose

Classify emails into actionable categories with priority and confidence scoring for automated workflow routing.

## Template

<s>JSON only, no extra text.</s>
<schema>{"subject":"string","category":"urgent|action_required|meeting|information|spam|promotion|personal|other","priority":"high|medium|low","confidence":"high|medium|low","suggested_action":"string","estimated_time":"string"}</schema>
<examples>
{"subject":"URGENT: Server down - all services affected","category":"urgent","priority":"high","confidence":"high","suggested_action":"Immediate response required","estimated_time":"< 5 minutes"}
{"subject":"Please review and approve Q4 budget proposal","category":"action_required","priority":"medium","confidence":"high","suggested_action":"Review document and respond","estimated_time":"15-30 minutes"}
{"subject":"Weekly team meeting - Tuesday 2pm","category":"meeting","priority":"medium","confidence":"high","suggested_action":"Add to calendar","estimated_time":"< 2 minutes"}
{"subject":"Industry newsletter - March 2024 edition","category":"information","priority":"low","confidence":"high","suggested_action":"Read when time permits","estimated_time":"10-15 minutes"}
{"subject":"You've won $1M! Click here now!","category":"spam","priority":"low","confidence":"high","suggested_action":"Delete","estimated_time":"< 1 minute"}
{"subject":"50% off all products this weekend only","category":"promotion","priority":"low","confidence":"high","suggested_action":"Review if interested","estimated_time":"2-5 minutes"}
{"subject":"Happy birthday! Hope you have a great day","category":"personal","priority":"low","confidence":"high","suggested_action":"Respond when convenient","estimated_time":"2-5 minutes"}
{"subject":"Fwd: Fwd: RE: Some random thoughts","category":"other","priority":"low","confidence":"medium","suggested_action":"Review to determine relevance","estimated_time":"5-10 minutes"}
</examples>
<classification_rules>
urgent: security issues, system failures, compliance deadlines, crisis situations
action_required: approvals needed, decisions required, tasks assigned, responses requested
meeting: calendar invites, meeting confirmations, agenda items, scheduling
information: newsletters, updates, reports, FYI items, industry news
spam: obvious scams, phishing attempts, irrelevant promotional content
promotion: legitimate marketing emails, sales offers, product announcements
personal: messages from friends/family, non-work social content
other: unclear purpose, mixed content, requires further review
</classification_rules>
<priority_criteria>
high: urgent category, deadline today, security/legal issues, C-level requests
medium: action required with reasonable timeline, scheduled meetings, important updates
low: informational content, promotions, personal messages, non-time-sensitive items
</priority_criteria>
<confidence_criteria>
high: clear indicators match category perfectly, obvious classification
medium: likely category but some ambiguity, mixed signals present
low: unclear purpose, insufficient information, multiple possible categories
</confidence_criteria>
<task>Classify the email subject line using the exact JSON format shown in examples.</task>
<input>{{EMAIL_SUBJECT}}</input>

## Test Cases

### Clear Urgent Email

Input: "CRITICAL: Data breach detected - immediate action required"
Expected: {"subject":"CRITICAL: Data breach detected - immediate action required","category":"urgent","priority":"high","confidence":"high","suggested_action":"Immediate security response","estimated_time":"< 5 minutes"}

### Action Required Email

Input: "Please sign contract and return by Friday"
Expected: {"subject":"Please sign contract and return by Friday","category":"action_required","priority":"medium","confidence":"high","suggested_action":"Review, sign, and return document","estimated_time":"10-20 minutes"}

### Meeting Invitation

Input: "Invitation: Project kickoff meeting - March 15 at 10am"
Expected: {"subject":"Invitation: Project kickoff meeting - March 15 at 10am","category":"meeting","priority":"medium","confidence":"high","suggested_action":"Accept and add to calendar","estimated_time":"< 2 minutes"}

### Newsletter/Information

Input: "Weekly DevOps digest - Latest tools and best practices"
Expected: {"subject":"Weekly DevOps digest - Latest tools and best practices","category":"information","priority":"low","confidence":"high","suggested_action":"Read when time permits","estimated_time":"10-15 minutes"}

### Obvious Spam

Input: "Congratulations! You've inherited $5 million from Nigerian prince"
Expected: {"subject":"Congratulations! You've inherited $5 million from Nigerian prince","category":"spam","priority":"low","confidence":"high","suggested_action":"Delete immediately","estimated_time":"< 1 minute"}

### Legitimate Promotion

Input: "New features in our project management tool - 30% discount"
Expected: {"subject":"New features in our project management tool - 30% discount","category":"promotion","priority":"low","confidence":"high","suggested_action":"Review if tool is relevant","estimated_time":"5-10 minutes"}

### Personal Email

Input: "Thanks for dinner last night! Had a great time"
Expected: {"subject":"Thanks for dinner last night! Had a great time","category":"personal","priority":"low","confidence":"high","suggested_action":"Respond when convenient","estimated_time":"2-5 minutes"}

### Ambiguous/Low Confidence

Input: "RE: That thing we discussed"
Expected: {"subject":"RE: That thing we discussed","category":"other","priority":"low","confidence":"low","suggested_action":"Review full email content","estimated_time":"5-10 minutes"}

### High Priority Action

Input: "CEO needs Q4 numbers for board meeting tomorrow"
Expected: {"subject":"CEO needs Q4 numbers for board meeting tomorrow","category":"action_required","priority":"high","confidence":"high","suggested_action":"Prepare and send Q4 financial data","estimated_time":"30-60 minutes"}

### Security/Compliance

Input: "Security audit findings require immediate remediation"
Expected: {"subject":"Security audit findings require immediate remediation","category":"urgent","priority":"high","confidence":"high","suggested_action":"Review findings and start remediation","estimated_time":"< 10 minutes"}
