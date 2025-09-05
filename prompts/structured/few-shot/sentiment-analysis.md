---
title: Sentiment Analysis - Structured Template
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

# Sentiment Analysis - Structured Template

## Purpose

Classify text sentiment with confidence scoring and error handling for automated workflows.

## Template

<s>JSON only, no extra text.</s>
<schema>{"text":"string","sentiment":"positive|neutral|negative","confidence":"high|medium|low","word_count":"number","language_detected":"string|null"}</schema>
<examples>
{"text":"Amazing experience! Highly recommended!","sentiment":"positive","confidence":"high","word_count":5,"language_detected":"english"}
{"text":"It's okay, nothing special but not bad either.","sentiment":"neutral","confidence":"high","word_count":9,"language_detected":"english"}
{"text":"Terrible service, very disappointed.","sentiment":"negative","confidence":"high","word_count":5,"language_detected":"english"}
{"text":"","sentiment":"neutral","confidence":"low","word_count":0,"language_detected":null}
{"text":"Hmm, maybe... we'll see I guess...","sentiment":"neutral","confidence":"low","word_count":6,"language_detected":"english"}
{"text":"ABSOLUTELY FANTASTIC!","sentiment":"positive","confidence":"high","word_count":2,"language_detected":"english"}
{"text":"This is THE WORST thing ever!","sentiment":"negative","confidence":"high","word_count":6,"language_detected":"english"}
{"text":"Good product but terrible customer service","sentiment":"neutral","confidence":"medium","word_count":7,"language_detected":"english"}
</examples>
<confidence_criteria>
high: clear positive/negative words, strong emotion, definitive language, sufficient context
medium: mixed signals, moderate language, some ambiguity but leaning direction clear
low: empty text, very short text, ambiguous language, uncertainty markers, contradictory signals
</confidence_criteria>
<error_handling>
If text is empty: {"text":"","sentiment":"neutral","confidence":"low","word_count":0,"language_detected":null}
If text too short (1-2 words): confidence = low
If mixed sentiment detected: sentiment = neutral, confidence = medium
If non-English detected: attempt analysis, note language in language_detected field
</error_handling>
<validation_rules>
word_count: actual word count of input text
language_detected: "english" | "other" | null (for empty)
confidence must align with clarity of sentiment indicators
sentiment must be one of three values exactly
</validation_rules>
<task>Classify the following text using the EXACT same JSON format as examples.</task>
<input>{{TEXT_TO_ANALYZE}}</input>

## Test Cases

### Clear Positive Sentiment

Input: "Absolutely love this product! Best purchase I've made this year."
Expected: {"text":"Absolutely love this product! Best purchase I've made this year.","sentiment":"positive","confidence":"high","word_count":11,"language_detected":"english"}

### Clear Negative Sentiment

Input: "Worst customer service ever. Complete waste of money."
Expected: {"text":"Worst customer service ever. Complete waste of money.","sentiment":"negative","confidence":"high","word_count":9,"language_detected":"english"}

### Mixed Sentiment

Input: "Great product quality but overpriced and slow shipping."
Expected: {"text":"Great product quality but overpriced and slow shipping.","sentiment":"neutral","confidence":"medium","word_count":8,"language_detected":"english"}

### Ambiguous/Uncertain

Input: "It's fine I suppose... could be better, could be worse."
Expected: {"text":"It's fine I suppose... could be better, could be worse.","sentiment":"neutral","confidence":"low","word_count":11,"language_detected":"english"}

### Very Short Text

Input: "Okay."
Expected: {"text":"Okay.","sentiment":"neutral","confidence":"low","word_count":1,"language_detected":"english"}

### Empty Input

Input: ""
Expected: {"text":"","sentiment":"neutral","confidence":"low","word_count":0,"language_detected":null}

### Strong Positive with Caps

Input: "OMG BEST THING EVER! LOVE IT!"
Expected: {"text":"OMG BEST THING EVER! LOVE IT!","sentiment":"positive","confidence":"high","word_count":6,"language_detected":"english"}

### Sarcastic/Complex

Input: "Oh great, another delay. Just what I needed today."
Expected: {"text":"Oh great, another delay. Just what I needed today.","sentiment":"negative","confidence":"medium","word_count":9,"language_detected":"english"}
