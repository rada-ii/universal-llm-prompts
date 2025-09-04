[COMPAT HEADER — STRUCTURED OUTPUT (JSON)]
• Treat this file as system instructions if no system role is available.
• Output must be JSON only; first character must be {.
• On failure, return only: {"error":"format_violation","note":"why"}.
[/COMPAT]

# Sentiment Analysis - Few-Shot Template

## Purpose

Classify text sentiment with confidence scoring using few-shot examples.

## Template

<s>JSON only, no extra text.</s>
<schema>{"text":"string","sentiment":"positive|neutral|negative","confidence":"high|low"}</schema>
<examples>
{"text":"Amazing experience! Highly recommended!","sentiment":"positive","confidence":"high"}
{"text":"It's okay, nothing special but not bad either.","sentiment":"neutral","confidence":"high"}
{"text":"Terrible service, very disappointed.","sentiment":"negative","confidence":"high"}
{"text":"","sentiment":"neutral","confidence":"low"}
{"text":"Hmm, maybe... we'll see I guess...","sentiment":"neutral","confidence":"low"}
{"text":"ABSOLUTELY FANTASTIC!!!","sentiment":"positive","confidence":"high"}
{"text":"This is THE WORST thing ever!!!","sentiment":"negative","confidence":"high"}
</examples>
<confidence_criteria>
high: clear positive/negative words, strong emotion, definitive language
low: empty text, ambiguous language, mixed signals, uncertainty markers
</confidence_criteria>
<task>Classify the following text using the EXACT same JSON format as examples.</task>
<input>{{TEXT_TO_ANALYZE}}</input>

## Test Cases

### Clear Positive Sentiment

Input: "Absolutely love this product! Best purchase I've made this year."
Expected: {"text":"Absolutely love this product! Best purchase I've made this year.","sentiment":"positive","confidence":"high"}

### Clear Negative Sentiment

Input: "Worst customer service ever. Complete waste of money."
Expected: {"text":"Worst customer service ever. Complete waste of money.","sentiment":"negative","confidence":"high"}

### Ambiguous/Uncertain

Input: "It's fine I suppose... could be better, could be worse."
Expected: {"text":"It's fine I suppose... could be better, could be worse.","sentiment":"neutral","confidence":"low"}

### With Emojis and Caps

Input: "OMG BEST THING EVER!!!LOVE IT!!!"
Expected: {"text":"OMG BEST THING EVER!!!LOVE IT!!!","sentiment":"positive","confidence":"high"}

### Empty Input

Input: ""
Expected: {"text":"","sentiment":"neutral","confidence":"low"}
