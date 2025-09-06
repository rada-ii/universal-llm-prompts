# Universal LLM Prompts

Production-ready prompts for ChatGPT, Claude, and other large language models. Designed for both technical and non-technical users across multiple industries.

## Quick Start

1. Browse `prompts/simple/` or `prompts/structured/` directories
2. Copy the complete prompt from any .md file
3. Replace bracketed placeholders with your information
4. Execute in your preferred AI platform

**Example:**

```
File: prompts/simple/business/business-plan-simple.md
Input: Replace [YOUR BUSINESS IDEA] with "meal planning app"
Output: Professional business plan section in 2 minutes
```

## Repository Structure

```
universal-llm-prompts/
├── prompts/
│   ├── simple/                    # Document generation (18 prompts)
│   │   ├── business/              # Plans, analysis, decisions
│   │   ├── healthcare/            # Patient communication
│   │   ├── legal/                 # Contract analysis
│   │   ├── finance/               # Investment evaluation
│   │   ├── education/             # Lesson plans, quizzes
│   │   ├── communication/         # Emails, presentations
│   │   ├── creative/              # Content, social media
│   │   └── [6 more categories]/
│   └── structured/                # Data extraction (13 prompts)
│       ├── classification/        # Sentiment, categorization
│       ├── templates/             # JSON/CSV outputs
│       ├── advanced/              # Complex reasoning
│       └── system-roles/          # AI behavior definitions
├── tests/
│   ├── inputs/                    # Realistic test scenarios
│   └── outputs/golden/            # Quality benchmarks
└── scripts/                       # Validation tools
```

## Prompt Categories

### Simple Prompts

Generate documents humans read - business plans, emails, lesson plans.

**Business & Professional:**

- Business Plan Creator - Executive summaries, market analysis
- Competitor Analysis - Strategic positioning
- Financial Analysis - Investment evaluation, budget planning
- Legal Document Analysis - Contract review in plain English

**Industry-Specific:**

- Healthcare Communication - Patient instructions, medical notes
- Real Estate Analysis - Property valuation, market research
- Educational Tools - Curriculum development, assessment creation

**Career Development:**

- Resume Builder - ATS-optimized professional resumes
- Interview Preparation - Company research, practice questions
- Task Organization - Priority management, productivity

### Structured Prompts

Generate machine-readable outputs for automation workflows.

**Data Processing:**

- Email Classification - Automated routing with confidence scoring
- Sentiment Analysis - Text emotion detection
- Job Data Extraction - Structured parsing of employment postings
- CSV Message Export - Clean data for reporting

**Advanced Features:**

- Chain-of-Thought Reasoning - Complex problem-solving with visible logic
- Error Handling Templates - Robust validation patterns
- Few-Shot Learning - Pattern recognition examples

## Platform Compatibility

**Tested and verified on:**

- ChatGPT 4 and ChatGPT 5
- Claude 3 and Claude 4
- Compatible with other large language models

**Features:**

- Standardized compatibility headers for consistent behavior
- Temperature recommendations for optimal results
- Error handling across different AI systems

## Usage Examples

### Document Generation

```
Prompt: Business Plan Creator
Input: "AI-powered meal planning app for busy professionals"
Output: 500-word executive summary with market analysis and financial projections
Time: 2-3 minutes
```

### Data Processing

```
Prompt: Job Data Extraction
Input: Raw job posting text
Output: Valid JSON with salary, location, skills, experience requirements
Accuracy: 95%+ for structured data
```

### Content Creation

```
Prompt: Blog Outline Creator
Input: "Remote work productivity tips"
Output: Complete article structure with SEO keywords and social media hooks
Result: Ready-to-write content plan
```

## Testing and Quality

**Validation Framework:**

- 31 prompts across 11 professional categories
- 28 realistic test scenarios with sample inputs
- Automated JSON/CSV validation
- Cross-platform compatibility verification

**Run Tests:**

```bash
# Complete test suite
bash scripts/run-all-tests.sh

# Category-specific testing
python3 tests/test-runner.py --category business

# JSON validation only
python3 scripts/validate_json_examples.py
```

## Target Users

**Non-Technical Professionals** - Business plans, patient communications, lesson plans without requiring technical knowledge.

**Technical Teams** - Structured data extraction, classification systems, automated workflows with proper error handling.

**Industry Specialists** - Healthcare professionals, educators, legal teams, real estate agents with domain-specific tools.

## Getting Started by Role

**Business Users:** Start with `prompts/simple/business/` for planning and analysis tools.

**Healthcare:** Review `prompts/simple/healthcare/` for patient communication templates.

**Developers:** Explore `prompts/structured/` for JSON/CSV automation workflows.

**Educators:** Access `prompts/simple/education/` for curriculum and assessment tools.

## Advanced Usage

**Workflow Examples:** Combine multiple prompts for complex projects. See `examples/workflow-examples.md` for business planning, content marketing, and job search strategies.

**Custom Integration:** Structured prompts include production-ready schemas for software integration and API workflows.

## Documentation

- **CONTRIBUTING.md** - Guidelines for adding prompts and quality standards
- **TROUBLESHOOTING.md** - Platform-specific issues and solutions
- **TESTING_EXPLAINED.md** - Quality assurance methodology
- **PROMPT-CREATION-GUIDE.md** - Best practices for writing effective prompts

## Contributing

Quality contributions welcome. All prompts must:

- Work on ChatGPT 4 and Claude 3
- Include realistic test scenarios
- Follow established templates
- Pass automated validation

See CONTRIBUTING.md for detailed guidelines.

## License

MIT License - Open source with active community contribution framework.
