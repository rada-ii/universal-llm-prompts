[COMPAT HEADER — COT-SAFE]
• If the model/policy prevents showing rationale, omit it and return either:
• Direct answer only, or
• {"warning":"rationale_withheld"} alongside the final plan.
[/COMPAT]

# Chain-of-Thought Reasoning Templates

## Purpose

Compare different reasoning approaches: direct answer, explicit rationale, debug mode.

## v1: Direct Answer (No CoT)

<s>Task completion without showing reasoning process.</s>
<task>Create a 4-point workshop plan for prompt engineering.</task>
<rules>Reply with exactly 4 bullet points; no introduction or conclusion; ≤15 words per point.</rules>
<format>

- 1. [point]
- 2. [point]
- 3. [point]
- 4. [point]
     </format>

## v2: Explicit Rationale (Visible CoT)

<s>Show reasoning process then provide final answer.</s>
<task>Create a 4-point workshop plan for prompt engineering.</task>
<rationale>Consider key factors: target audience skill level, available time, learning objectives, practical application.</rationale>
<rules>Show reasoning first, then final plan; ≤15 words per final point.</rules>
<format>
**Rationale:**

- Audience analysis: [reasoning]
- Time allocation: [reasoning]
- Learning progression: [reasoning]
- Success metrics: [reasoning]

**Workshop Plan:**

- 1. [point]
- 2. [point]
- 3. [point]
- 4. [point]
     </format>

Fallback for rationale-restricted models: If rationale cannot be displayed, output only the Workshop Plan and add {"warning":"rationale_withheld"}.

## v3: Debug Mode (Self-Correction)

<s>Create initial plan, critique it, then provide improved version.</s>
<task>Create a workshop plan with explicit revision process.</task>
<debug_process>

1. Generate initial 4-point plan
2. Identify weaknesses or gaps
3. Apply improvements based on critique
4. Present final optimized plan
   </debug_process>
   <format>
   **Initial Draft:**

- [4 points]

**Critique & Issues:**

- [weakness 1]
- [weakness 2]
- [improvement needed]

**Improved Final Plan:**

- [optimized 4 points]
  </format>

## Comparison Results

| Approach       | Speed   | Quality | Transparency    | Use Case           | Best For              |
| -------------- | ------- | ------- | --------------- | ------------------ | --------------------- |
| Direct (v1)    | ⚡ Fast | Good    | None            | Quick tasks        | Simple, routine work  |
| Rationale (v2) | Slower  | Better  | Full visibility | Complex planning   | Stakeholder review    |
| Debug (v3)     | Slowest | Best    | Full process    | Critical decisions | High-stakes scenarios |
