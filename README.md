# Universal LLM Prompts

A complete prompt library designed for everyone - from teachers and entrepreneurs to developers and data scientists. Get reliable, useful outputs from any major AI platform including ChatGPT, Claude, Gemini, and others.

## Two Ways to Use This Library

### For Non-Technical Users (Simple Prompts)

**Perfect for:** Teachers, business owners, marketers, researchers, students, content creators

- **Ready-to-use prompts** that produce formatted documents you can use immediately
- **No programming knowledge required** - just copy, fill in your details, and go
- **Human-readable outputs** like lesson plans, business strategies, meeting summaries
- **Step-by-step instructions** with examples included

### For Technical Users (Structured Prompts)

**Perfect for:** Developers, data scientists, automation engineers, AI researchers

- **JSON/CSV outputs** for integration and automation
- **Consistent schemas** across different AI providers
- **Production-ready** with comprehensive error handling
- **Cross-platform compatibility** headers for reliable results

## Quick Start Guide

### Option 1: Simple Use (No Technical Knowledge Needed)

1. **Browse `prompts/simple/`** to find what you need
2. **Open any .md file** and copy the entire prompt
3. **Fill in the bracketed sections** with your specific information
4. **Paste into ChatGPT, Claude, or any AI** and get your result
5. **Use the output directly** - it's formatted and ready to go

**Example:** Need a lesson plan? Use `prompts/simple/education/lesson-plan-simple.md`, fill in your topic and grade level, get a complete teaching plan.

### Option 2: Technical Use (For Automation/Integration)

1. **Browse `prompts/structured/`** for JSON/CSV templates
2. **Replace `{{PLACEHOLDER}}` variables** with your data
3. **Set AI temperature to 0-0.2** for consistent results
4. **Parse the structured output** in your applications

**Example:** Extract job data? Use `prompts/structured/templates/json-job-extraction.md`, get standardized JSON for your database.

## What's Available

### Business Applications

- **Business Plan Generator** - Professional business plan sections
- **Competitor Analysis** - Strategic market analysis
- **Marketing Content** - Blog outlines, social media plans

### Education Tools

- **Lesson Plan Creator** - Complete teaching plans with activities
- **Quiz Generator** - Tests and assessments from any content
- **Study Materials** - Learning guides and educational content

### Productivity Helpers

- **Meeting Summarizer** - Clean summaries with action items
- **Task Organizer** - Priority planning and time management
- **Decision Framework** - Systematic decision analysis

### Creative Content

- **Blog Outlines** - SEO-optimized content structure
- **Social Media Planning** - Content calendars and campaigns
- **Presentation Builder** - Professional presentation outlines

### Research & Analysis

- **Data Analyzer** - Extract insights from surveys and studies
- **Literature Review** - Academic research analysis
- **Report Generator** - Professional research documentation

### Technical Tools

- **Data Extraction** - Convert unstructured text to JSON/CSV
- **Content Classification** - Automated categorization
- **Error Handling** - Robust production patterns

## Real-World Examples

**Teacher uses lesson plan prompt:**
Input: "Fractions for 4th grade, 60 minutes"
Output: Complete lesson with objectives, activities, materials, and timing

**Entrepreneur uses business plan prompt:**
Input: "AI meal planning app for busy professionals"
Output: Professional executive summary ready for investors

**Developer uses job extraction prompt:**
Input: "Senior React Developer at Google, $120k-180k, Remote"
Output: `{"title":"Senior React Developer","company":"Google","salary_min":120000,...}`

**Manager uses meeting summary prompt:**
Input: Raw meeting notes with scattered information
Output: Clean summary with decisions, action items, and deadlines

## Testing Your Prompts

1. **Look in `tests/inputs/`** for example content that works well
2. **Follow the guide** in `tests/HOW_TO_TEST.md` for step-by-step testing
3. **Save your results** in `tests/outputs/` to track what works
4. **Use the examples** to understand what good outputs look like

## Repository Structure

```
prompts/
├── simple/              # Human-readable outputs for everyone
│   ├── business/        # Business planning and strategy
│   ├── education/       # Teaching and learning tools
│   ├── creative/        # Content creation and marketing
│   ├── productivity/    # Personal and professional efficiency
│   ├── research/        # Data analysis and insights
│   └── communication/   # Presentations and decision-making
└── structured/          # JSON/CSV outputs for developers
    ├── templates/       # Data extraction templates
    ├── few-shot/        # Classification with examples
    └── advanced/        # Complex reasoning patterns

tests/
├── inputs/              # Example content for testing
├── outputs/             # Where to save your test results
├── harness/             # Testing configuration
└── HOW_TO_TEST.md      # Step-by-step testing guide
```

## Best Practices

### For Simple Prompts:

- **Be specific** with your input - more detail leads to better results
- **Use fresh AI conversations** for each different task
- **Review and customize** the output to match your exact needs
- **Save successful prompts** for reuse with similar projects

### For Structured Prompts:

- **Set temperature to 0-0.2** for consistent JSON/CSV formatting
- **Validate outputs** using JSON parsers or CSV readers
- **Handle errors gracefully** using the provided error patterns
- **Test across different AI providers** to ensure compatibility

### General Tips:

- **Start with examples** from the tests/inputs/ folder to understand expected input format
- **Modify prompts** to better fit your specific use case or industry
- **Combine prompts** for complex workflows (but use separate AI conversations)
- **Keep successful variations** of prompts that work well for your needs

## Success Stories

**Teachers:** "Created a full week of science lesson plans in 45 minutes"
**Startups:** "Generated investor-ready business plan sections for pitch deck"
**Marketing Agencies:** "Planned 90 days of social media content for 5 clients"
**Consultants:** "Automated competitor analysis reports for client proposals"
**Developers:** "Extracted structured data from 10,000 job postings in hours"

## Troubleshooting

**Problem:** AI adds extra text before JSON output
**Solution:** Ensure you're using prompts from `prompts/structured/` and set temperature to 0-0.2

**Problem:** Output doesn't match your needs exactly
**Solution:** Use prompts from `prompts/simple/` and customize the instructions to your requirements

**Problem:** Inconsistent results across different AI platforms
**Solution:** All prompts include compatibility headers - copy the entire prompt file, not just parts

**Problem:** Not sure which prompt to use
**Solution:** Check `tests/inputs/` for examples that match your use case

## Contributing

Found a prompt that could work better? Have an idea for a new one?

1. **Fork this repository**
2. **Test your improvement** using the testing framework
3. **Add examples** to the appropriate `tests/inputs/` folder
4. **Submit a pull request** with your enhancement

## License

MIT License - use these prompts freely in personal and commercial projects.

## Support

- **Read the examples** in `tests/inputs/` for guidance on input format
- **Check the testing guide** at `tests/HOW_TO_TEST.md` for troubleshooting
- **Open an issue** if you discover bugs or have suggestions
- **Share your success stories** to help others understand the value

---

Whether you're a teacher planning lessons, an entrepreneur writing business strategies, a marketer creating content campaigns, or a developer building AI-powered applications - these prompts are designed to make AI more useful and reliable for your specific needs.
