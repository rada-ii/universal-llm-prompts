---
title: Context Management for Long Document
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

# Context Management for Long Documents

## Purpose

Process long documents efficiently while maintaining accuracy and avoiding "lost in the middle" problem.

## Template: Chunked Processing with Summary

<s>Process long document in chunks, then synthesize final results.</s>
<goal>Extract {{TARGET_COUNT}} requirements and {{RISK_COUNT}} risks from document.</goal>
<strategy>

1. Process document in ~500-word chunks
2. For each chunk: identify key themes and extract relevant items
3. Prioritize information from introduction and conclusion (2x weight)
4. Synthesize all chunk results into final output
5. If insufficient context, request specific clarification
   </strategy>
   <chunk_processing>
   For each chunk, create mini-summary with:

- Chunk theme: [main topic]
- Requirements found: [list]
- Risks identified: [list]
- Confidence level: [high/medium/low]
  </chunk_processing>
  <o>Final JSON: {"requirements":[{{TARGET_COUNT}} items],"risks":[{{RISK_COUNT}} items],"processing_notes":"summary of approach"}</o>
  <data>{{LONG_DOCUMENT_TEXT}}</data>
  <reminder>Remember: EXACTLY {{TARGET_COUNT}} requirements and {{RISK_COUNT}} risks in final output.</reminder>

## Template: Front-loaded Processing

<s>Prioritize key sections of long documents for critical information.</s>
<priority_order>

1. Executive summary / Introduction (highest priority)
2. Conclusions / Recommendations (highest priority)
3. Section headings and subheadings (medium priority)
4. First and last paragraph of each section (medium priority)
5. Body content (lower priority)
   </priority_order>
   <goal>Extract {{ITEM_COUNT}} key insights following priority order above.</goal>
   <rules>

- Process high-priority sections first and most thoroughly
- Use medium-priority sections to validate and supplement findings
- Reference body content only if high-priority sections insufficient
- Mark confidence level based on source priority
  </rules>
  <o>JSON: {"insights":[{{ITEM_COUNT}} items with source and confidence],"method":"front_loaded"}</o>
  <data>{{LONG_DOCUMENT_TEXT}}</data>

## Template: Iterative Refinement

<s>Multi-pass document processing for comprehensive analysis.</s>
<process>
Pass 1: Broad scan for main themes and structure
Pass 2: Detailed extraction of specific items requested  
Pass 3: Validation and gap filling
Pass 4: Final ranking and selection
</process>
<goal>Find {{TARGET_ITEMS}} most important items of type {{ITEM_TYPE}}.</goal>
<pass_instructions>
Pass 1: List all potential items found (no limit)
Pass 2: Group similar items and rank by importance  
Pass 3: Verify ranking logic and fill any obvious gaps
Pass 4: Select final {{TARGET_ITEMS}} with highest scores
</pass_instructions>
<o>JSON: {"items":[{{TARGET_ITEMS}} ranked items],"process_log":"brief summary of each pass"}</o>
<data>{{LONG_DOCUMENT_TEXT}}</data>

## Test Cases

### Long Technical Document (2000+ words)

Input: Full API documentation with multiple sections
Expected: Accurate extraction despite length, no missed critical info in middle sections

### Document with Contradictory Information

Input: Policy document with conflicting requirements in different sections
Expected: Flag contradictions, synthesize coherently or request clarification

### Very Long Document (5000+ words)

Input: Comprehensive business requirements document
Expected: Maintain accuracy across full document, proper prioritization
