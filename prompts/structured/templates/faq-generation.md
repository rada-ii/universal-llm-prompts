[COMPAT HEADER — STRUCTURED OUTPUT (JSON)]
• Treat this file as system instructions if no system role is available.
• Output must be JSON only; first character must be {.
• On failure, return only: {"error":"format_violation","note":"why"}.
[/COMPAT]

# FAQ Generation Template

## Purpose

Extract 3–5 high-quality FAQ pairs from documentation or content.

## Template

<s>JSON only, no extra text.</s>
<goal>Extract FAQ pairs (question/answer) from the provided text.</goal>
<quality_rules>

- Generate 3–5 FAQ pairs (prefer 5 if content allows)
- Questions must start with: How, What, Why, When, Where, Can, Does, Is, Are
- Questions should cover most important/frequently asked topics
- Answers must be ≤30 words and specific (avoid "it depends" responses)
- Use information only from provided text, no external knowledge
- If insufficient content for 3 quality FAQs: {"error":"insufficient_content","available_faqs":X,"minimum_needed":3}
  </quality_rules>
  <output>JSON format: {"faq":[{"q":"question","a":"answer"}]} with no additional text</output>
  <data>{{CONTENT_TEXT}}</data>

## Test Cases

### Rich Content (5 FAQs possible)

Input:

```
Our REST API supports user management with JWT authentication. Tokens expire after 24 hours and must be refreshed. Rate limiting allows 1000 requests per hour per API key. We only support JSON responses. Code examples are available in Python, JavaScript, and cURL. Premium accounts receive 10x higher rate limits (10,000/hour) and priority support. API documentation includes endpoint descriptions, request/response schemas, and error codes. Free tier users can make up to 100 requests per day.
```

Expected Output:

```json
{
  "faq": [
    {
      "q": "What authentication method does the API use?",
      "a": "JWT tokens that expire after 24 hours and must be refreshed."
    },
    {
      "q": "What are the rate limits for API requests?",
      "a": "1000 requests/hour for standard, 10,000/hour for premium accounts."
    },
    {
      "q": "What response formats does the API support?",
      "a": "JSON responses only."
    },
    {
      "q": "What programming languages have code examples?",
      "a": "Python, JavaScript, and cURL examples are available."
    },
    {
      "q": "How many requests can free tier users make?",
      "a": "Up to 100 requests per day."
    }
  ]
}
```

### Limited Content (3 FAQs possible)

Input:

```
Our service offers email notifications. Users can enable or disable notifications in settings. Notifications are sent for account changes and security alerts.
```

Expected Output:

```json
{
  "faq": [
    {
      "q": "What types of notifications do you send?",
      "a": "Email notifications for account changes and security alerts."
    },
    {
      "q": "How can users control notifications?",
      "a": "Enable or disable notifications in account settings."
    },
    {
      "q": "Where are notification settings located?",
      "a": "In the account settings section."
    }
  ]
}
```

### Insufficient Content

Input:

```
We provide software solutions.
```

Expected Output:

```json
{ "error": "insufficient_content", "available_faqs": 0, "minimum_needed": 3 }
```
