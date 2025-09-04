[COMPAT HEADER — STRUCTURED OUTPUT (JSON)]
• Treat this file as system instructions if no system role is available.
• Output must be JSON only; first character must be {.
• On failure, return only: {"error":"format_violation","note":"why"}.
[/COMPAT]

# Content Classification - Few-Shot Template

## Purpose

Classify content into predefined categories with confidence scoring.

## Template

<s>JSON only, no extra text.</s>
<schema>{"text":"string","category":"news|tutorial|review|documentation|marketing|social|other","confidence":"high|medium|low"}</schema>
<examples>
{"text":"Breaking: New AI model released by OpenAI shows significant improvements","category":"news","confidence":"high"}
{"text":"Step-by-step guide: How to build a React app from scratch","category":"tutorial","confidence":"high"}
{"text":"I tested the new iPhone for 2 weeks - here's my honest opinion","category":"review","confidence":"high"}
{"text":"API Reference: Authentication endpoints and parameters","category":"documentation","confidence":"high"}
{"text":"Transform your business with our AI-powered solutions! Contact us today!","category":"marketing","confidence":"high"}
{"text":"Just had the best coffee ever! #MondayMotivation ☕","category":"social","confidence":"high"}
{"text":"Some random thoughts about various things","category":"other","confidence":"medium"}
</examples>
<confidence_criteria>
high: clear indicators match category (headlines, how-to, tested/reviewed, API docs, sales language, social hashtags)
medium: likely category but mixed elements, some ambiguity
low: vague content, multiple possible categories, unclear purpose
</confidence_criteria>
<task>Classify the content using the same JSON format.</task>
<input>{{CONTENT_TO_CLASSIFY}}</input>

## Test Cases

### Clear News Content

Input: "Tech giant announces major layoffs affecting 10,000 employees worldwide"
Expected: {"text":"Tech giant announces major layoffs affecting 10,000 employees worldwide","category":"news","confidence":"high"}

### Clear Tutorial Content

Input: "How to set up automated testing in 5 simple steps"
Expected: {"text":"How to set up automated testing in 5 simple steps","category":"tutorial","confidence":"high"}

### Medium Confidence - Mixed Elements

Input: "Our new product launch includes innovative features that will change how you work"
Expected: {"text":"Our new product launch includes innovative features that will change how you work","category":"marketing","confidence":"medium"}

### Low Confidence - Ambiguous

Input: "Thoughts on recent developments and future possibilities"
Expected: {"text":"Thoughts on recent developments and future possibilities","category":"other","confidence":"low"}
