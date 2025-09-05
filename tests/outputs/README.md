# Universal LLM Prompts

Professional prompt library for ChatGPT, Claude, and other large language models. Designed for both technical and non-technical users.

## Quick Start

1. Browse `prompts/simple/` or `prompts/structured/` directories
2. Copy the complete prompt from any .md file
3. Replace bracketed placeholders with your specific information
4. Execute in your preferred AI platform

## Repository Structure

### Simple Prompts

Document-generation prompts that produce human-readable content ready for immediate use. No technical knowledge required.

**Categories Available:**

- **Business:** Plans, competitor analysis, decision frameworks
- **Healthcare:** Patient communication, medical documentation
- **Legal:** Contract analysis, document review
- **Finance:** Investment analysis, financial planning
- **Real Estate:** Property valuation, market analysis
- **Education:** Lesson plans, assessment creation
- **Communication:** Professional emails, presentations, meeting summaries
- **Creative:** Content planning, social media strategies
- **Productivity:** Task organization, data analysis
- **Career:** Resume building, interview preparation

### Structured Prompts

Data-extraction prompts that return JSON or CSV outputs for automation workflows. Designed for developers and technical users.

**Categories Available:**

- **Classification:** Sentiment analysis, content categorization, email routing
- **Templates:** Job data extraction, FAQ generation, message processing
- **Advanced:** Chain-of-thought reasoning, context management
- **System Roles:** AI behavior definitions for specialized tasks

## Platform Compatibility

All prompts tested and validated on:

- ChatGPT 4
- Claude 3 and Claude 4
- Google Gemini Pro

Cross-platform compatibility headers ensure consistent behavior across different AI systems.

## Example Usage

**Business Plan Creation:**

```
File: prompts/simple/business/business-plan-simple.md
Input: Replace [YOUR BUSINESS IDEA] with "SaaS project management tool"
Output: Professional business plan section in under one minute
```

**Structured Data Extraction:**

```
File: prompts/structured/templates/json-job-extraction-structured.md
Input: Raw job posting text
Output: Valid JSON with salary, location, skills, and other structured fields
```

## Quality Assurance

- **31 total prompts** across 11 industry categories
- **28 test scenarios** with realistic input data
- **Automated validation** for JSON outputs and file integrity
- **Cross-platform testing** ensures reliability across AI platforms

### Testing Framework

```bash
# Complete validation suite
bash scripts/run-all-tests.sh

# Category-specific testing
python3 tests/test-runner.py --category business

# JSON output validation
python3 scripts/validate_json_examples.py
```

## Target Users

### Non-Technical Users

Simple prompts provide immediate value for business professionals, educators, healthcare workers, and other domain experts without requiring programming knowledge.

### Technical Users and Developers

Structured prompts offer production-ready solutions for data processing, classification tasks, and automated workflows with proper error handling and validation.

## Project Statistics

- **18 simple prompts** for document generation
- **13 structured prompts** for data processing
- **11 industry categories** including specialized domains
- **Comprehensive documentation** with troubleshooting guides
- **Open-source contribution framework** for community expansion

## Getting Started

### For Business Users

Start with `prompts/simple/business/` for planning, analysis, and decision-making tools.

### For Healthcare Professionals

Review `prompts/simple/healthcare/` for patient communication and medical documentation.

### For Developers

Explore `prompts/structured/` for JSON/CSV outputs and automation workflows.

### For Educators

Access `prompts/simple/education/` for curriculum development and assessment tools.

## Documentation

- **CONTRIBUTING.md:** Guidelines for adding new prompts and maintaining quality standards
- **TROUBLESHOOTING.md:** Solutions for common issues and platform-specific problems
- **TESTING_EXPLAINED.md:** Detailed explanation of testing methodology and quality assurance
- **examples/workflow-examples.md:** Advanced usage patterns combining multiple prompts

## Technical Implementation

### Simple Prompts

- Clear instruction format with placeholder replacement
- Professional output templates
- Industry-specific terminology and best practices
- Immediate usability without post-processing

### Structured Prompts

- Standardized JSON/CSV schemas
- Comprehensive error handling
- Input validation and sanitization
- Production-ready compatibility headers

All prompts include metadata for version control, platform compatibility, and target user identification.

---

**License:** Open source  
**Maintenance:** Actively maintained with regular updates  
**Community:** Contributions welcome via established guidelines
