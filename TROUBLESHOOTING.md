# Troubleshooting Guide

## Quick Fixes

### AI adds extra text to JSON output

**Problem**: Getting explanations instead of clean JSON/CSV

```
Here's the analysis:
{"title": "Developer", "company": "TechCorp"...}
Hope this helps!
```

**Solutions**:

1. Use structured prompts only for data extraction
2. Set temperature to 0.1
3. Copy entire prompt without modifications
4. Try Claude for better JSON consistency

### Output too generic

**Problem**: Getting textbook answers instead of practical advice

**Solutions**:

1. Add specific constraints:

   ```
   Instead of: "Write a business plan"
   Try: "Write a business plan for mobile app connecting dog owners
   with pet sitters, targeting urban professionals, $50K budget"
   ```

2. Include your situation:

   ```
   "We currently use spreadsheets, have 10 employees, $500/month budget"
   ```

3. Request specific examples:
   ```
   "Include 3 tools I can implement this week"
   ```

### Inconsistent results across platforms

**Platform strengths**:

- **ChatGPT 4**: Business documents, consistent formatting
- **Claude 3**: Long documents, structured data, analysis
- **Gemini Pro**: Creative content (sometimes verbose)

**Solutions**:

1. Use compatibility headers (included in structured prompts)
2. Adjust for platform:
   - ChatGPT: Direct instructions
   - Claude: Detailed prompts work well
   - Gemini: Shorter, focused prompts

### Not sure which prompt to use

**Decision tree**:

- **Want document humans read?** → Simple prompts
- **Want data for spreadsheets?** → Structured prompts
- **Need brainstorming?** → Simple prompts
- **Processing lots of data?** → Structured prompts

**Check examples**: Browse `tests/inputs/` for similar scenarios

### Prompts too slow or hit limits

**Solutions**:

1. Break large tasks into smaller parts
2. Focus requests:
   ```
   Instead of: "Analyze 50-page document"
   Try: "Analyze pages 1-10, focus on key findings"
   ```
3. Use structured prompts for data tasks (more efficient)

## Platform-Specific Issues

### ChatGPT Problems

- **Stops mid-response**: Ask "Continue" or break task smaller
- **Adds explanations to data**: End prompt with "Return only JSON"
- **Inconsistent format**: Use specific examples in prompt

### Claude Problems

- **Too verbose**: Add "Keep it concise" or use ChatGPT
- **Refuses requests**: Be more specific about business context

### Gemini Problems

- **Adds commentary to data**: Use Claude or ChatGPT for pure data
- **Ignores format**: Repeat format requirements at prompt end

## Technical Issues

### JSON validation errors

1. Use online JSON validator to find syntax errors
2. Check temperature settings (use 0.1 for structured)
3. Try different platform
4. Ensure using exact prompt text

### Missing test files

1. Check file path: `tests/inputs/[category]/[name].txt`
2. Verify file naming follows convention
3. Ensure file is readable UTF-8 text

### Structured prompts not working

**Checklist**:

- [ ] Using exact prompt text (don't modify structured prompts)
- [ ] Set temperature to 0.1
- [ ] Testing on ChatGPT 4 or Claude 3
- [ ] Input data in expected format

## Getting Better Results

### For Simple Prompts

1. **Be specific** - More detail = better results
2. **Use examples** - Show what good output looks like
3. **Provide context** - Explain your situation and constraints
4. **Set expectations** - Specify format and length

### For Structured Prompts

1. **Use exact templates** - Don't modify compatibility headers
2. **Validate inputs** - Ensure data is clean and complete
3. **Check outputs** - Use JSON/CSV validators
4. **Handle errors** - Review error messages for guidance

## Performance Expectations

### Normal Response Times

- Simple prompts: 10-25 seconds
- Structured prompts: 5-15 seconds
- Complex analysis: 20-45 seconds

### Success Rates

- Well-formed inputs: >95% success
- Edge cases: >85% success
- Error recovery: >90% helpful responses

## When to Get Help

### Before asking for help

1. Try prompt with provided test inputs first
2. Test on multiple AI platforms
3. Check if similar issues documented here
4. Read prompt instructions carefully

### How to report problems

Include:

1. Exact prompt filename used
2. AI platform (ChatGPT 4, Claude 3, etc.)
3. Your input (remove sensitive data)
4. Expected vs actual output
5. Temperature and other settings

### Community resources

- Check GitHub issues for similar problems
- Browse discussions for solutions
- Share successful modifications

Most issues stem from input formatting or platform differences. When in doubt, try exact test cases first.
