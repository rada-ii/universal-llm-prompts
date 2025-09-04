# Troubleshooting Guide

Having issues with prompts? This guide covers the most common problems and their solutions.

## Quick Fixes for Common Problems

### 🤖 AI adds extra text before/after my JSON output

**Problem:** Getting explanations or formatting instead of clean JSON/CSV

```
Here's the analysis you requested:
{"title": "Developer", "company": "TechCorp"...}
Hope this helps!
```

**Solutions:**

1. **Use structured prompts only** - Don't use simple prompts for data extraction
2. **Set temperature to 0.1** - Higher temperatures cause creative additions
3. **Copy the entire prompt** - Don't modify or shorten structured prompts
4. **Try different AI platform** - Claude is often better for pure JSON output

**Platform-specific fixes:**

- **ChatGPT:** Add "Output only the JSON, no additional text" to end of prompt
- **Gemini:** Often adds explanations; try Claude or ChatGPT instead
- **Claude:** Usually good with structured output by default

---

### 📝 Output doesn't match my needs exactly

**Problem:** Getting generic or irrelevant results

**Solutions:**

1. **Add specific examples** in your prompt:

   ```
   Instead of: "Write a business plan"
   Try: "Write a business plan for a mobile app that connects dog owners
   with pet sitters, targeting urban professionals who travel for work"
   ```

2. **Include context about your audience:**

   ```
   "Create this for busy executives who need quick, actionable insights"
   ```

3. **Specify the format you want:**

   ```
   "Format as an email I can send directly to my team"
   ```

4. **Give examples of what good looks like:**
   ```
   "Similar to how Airbnb connects hosts with travelers, but for pet care"
   ```

---

### 🔄 Inconsistent results across different AI platforms

**Problem:** Same prompt gives different quality results on different platforms

**Platform Strengths:**

- **ChatGPT 4:** Best for business documents, consistent formatting
- **Claude 3:** Excellent for long documents, analysis, and structured data
- **Gemini Pro:** Good for creative content, sometimes verbose
- **GPT-3.5:** Budget option, may need prompt adjustments

**Solutions:**

1. **Use compatibility headers** - Our structured prompts include these
2. **Test platform-specific versions:**

   - For ChatGPT: More direct instructions work better
   - For Claude: Longer, detailed prompts are fine
   - For Gemini: Shorter, focused prompts reduce verbosity

3. **Adjust for platform quirks:**
   - ChatGPT: Sometimes needs explicit format reminders
   - Claude: Excellent at following complex instructions
   - Gemini: May need "be concise" instruction

---

### ❓ Not sure which prompt to use for my situation

**Decision Tree:**

**Want a document humans will read?** → Use Simple Prompts

- Business plans, lesson plans, emails, presentations

**Want data for spreadsheets/automation?** → Use Structured Prompts

- Extract job info, classify content, analyze sentiment

**Need inspiration or brainstorming?** → Use Simple Prompts with creative focus

- Blog outlines, social media content, marketing ideas

**Processing lots of data?** → Use Structured Prompts

- Survey analysis, content classification, data extraction

**Check our examples:**

- Browse `tests/inputs/` for scenarios similar to yours
- Look at `EXAMPLES.md` for real outputs
- Try the closest match and adjust from there

---

### ⏱️ Prompts are too slow or hit token limits

**Problem:** AI stops mid-response or takes too long

**Solutions:**

1. **Break large tasks into smaller parts:**

   ```
   Instead of: "Analyze this 50-page document"
   Try: "Analyze pages 1-10 of this document, focusing on key findings"
   ```

2. **Use more focused prompts:**

   ```
   Instead of: "Create a complete marketing strategy"
   Try: "Create a social media plan for the next 30 days"
   ```

3. **Prioritize your requests:**

   ```
   "Focus on the 3 most important recommendations"
   ```

4. **Use structured prompts for data tasks** - They're more efficient

---

### 🎯 Results are too generic or obvious

**Problem:** Getting textbook answers instead of practical advice

**Solutions:**

1. **Add your specific constraints:**

   ```
   "Budget limited to $500/month, team of 2 people, B2B SaaS company"
   ```

2. **Request specific examples:**

   ```
   "Include 3 specific tools or tactics I can implement this week"
   ```

3. **Ask for personalization:**

   ```
   "Tailor this for a freelance graphic designer working with small businesses"
   ```

4. **Include your current situation:**
   ```
   "We're currently using spreadsheets and email, have 10 employees"
   ```

---

### 🔧 Technical prompts aren't working

**Problem:** Structured prompts returning errors or malformed data

**Checklist:**

- [ ] Using the exact prompt text (don't modify structured prompts)
- [ ] Set AI temperature to 0.1 or 0.2
- [ ] Copied entire prompt including compatibility headers
- [ ] Input data is in expected format
- [ ] Testing on ChatGPT 4 or Claude 3 (more reliable than others)

**Common fixes:**

1. **JSON validation errors:** Use an online JSON validator to check output
2. **CSV formatting issues:** Check for commas in data fields
3. **Missing fields:** Some platforms skip fields - specify "include all fields"
4. **Wrong data types:** Add type validation to your prompt

---

## Platform-Specific Troubleshooting

### ChatGPT Issues

**Problem:** Stops mid-response  
**Fix:** Ask "Continue" or break task into smaller parts

**Problem:** Adds explanations to structured output  
**Fix:** End prompt with "Return only the [format], no additional text"

**Problem:** Inconsistent formatting  
**Fix:** Use specific examples in your prompt

### Claude Issues

**Problem:** Too verbose for simple tasks  
**Fix:** Add "Keep it concise" or use ChatGPT for shorter outputs

**Problem:** Occasionally refuses reasonable requests  
**Fix:** Rephrase to be more specific about business context

### Gemini Issues

**Problem:** Adds commentary to data outputs  
**Fix:** Use Claude or ChatGPT for pure data extraction

**Problem:** Sometimes ignores format requirements  
**Fix:** Repeat format requirements at end of prompt

## Advanced Troubleshooting

### When Multiple Platforms Fail

1. **Check your input data:**

   - Is it clear and well-formatted?
   - Does it contain the information the prompt expects?
   - Try with our test inputs first

2. **Simplify your request:**

   - Remove optional elements
   - Focus on core functionality
   - Test with minimal example

3. **Check prompt compatibility:**
   - Are you mixing simple and structured prompt elements?
   - Did you modify a working prompt?
   - Try the original version first

### Performance Optimization

**For faster results:**

- Use shorter, more focused prompts
- Provide clear examples of desired output
- Avoid asking for multiple formats in one request

**For better quality:**

- Include specific context about your situation
- Give examples of good vs. bad outputs
- Use iterative refinement (start basic, then add details)

## Getting Help

### Before asking for help:

1. Try the prompt with our test inputs first
2. Test on multiple AI platforms
3. Check if similar issues are documented here
4. Read the prompt instructions carefully

### When to open an issue:

- Prompt consistently fails across platforms
- Documentation is unclear or incorrect
- Found a bug in the prompt logic
- Need a new prompt for common use case

### How to report problems:

1. **What prompt you used** (exact filename)
2. **What platform** (ChatGPT 4, Claude 3, etc.)
3. **Your input** (sanitized if needed)
4. **Expected vs. actual output**
5. **Any error messages**

### Community resources:

- Check existing GitHub issues
- Browse discussions for similar problems
- Share successful modifications with others

## Success Tips

### Make prompts work better:

1. **Be specific** - More detail usually = better results
2. **Use examples** - Show what good output looks like
3. **Provide context** - Explain your situation and constraints
4. **Test iteratively** - Start simple, add complexity gradually

### Platform selection:

- **For business documents:** ChatGPT 4
- **For data analysis:** Claude 3
- **For creative content:** Any platform works well
- **For automation:** Claude 3 or ChatGPT 4

Remember: These prompts are tested and working - most issues come from platform differences or input formatting. When in doubt, try the exact test cases first!
