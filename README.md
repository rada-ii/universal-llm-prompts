# Universal LLM Prompts

A comprehensive prompt library for large language models, designed to serve both technical and non-technical users across multiple industries and use cases.

## Overview

This repository provides production-ready prompts that generate professional documents and structured data outputs. All prompts have been tested for cross-platform compatibility and include comprehensive documentation, testing frameworks, and quality assurance measures.

## Repository Structure

```
universal-llm-prompts/
├── prompts/
│   ├── simple/                    # Document generation prompts
│   │   ├── business/              # Business planning and analysis
│   │   ├── healthcare/            # Medical communication
│   │   ├── legal/                 # Contract and document analysis
│   │   ├── finance/               # Financial analysis and planning
│   │   ├── real-estate/           # Property and market analysis
│   │   ├── education/             # Curriculum and assessment tools
│   │   ├── communication/         # Professional correspondence
│   │   ├── creative/              # Content and marketing materials
│   │   ├── productivity/          # Task management and decision support
│   │   ├── interview/             # Job preparation and career tools
│   │   └── resume/                # Professional resume development
│   └── structured/                # Data extraction and processing
│       ├── classification/        # Categorization and sentiment analysis
│       ├── templates/             # Data extraction frameworks
│       ├── advanced/              # Complex reasoning and analysis
│       ├── system-roles/          # AI behavior definitions
│       └── few-shot/              # Learning pattern examples
├── tests/
│   ├── inputs/                    # Test scenarios and sample data
│   │   ├── business/              # Business use case examples
│   │   ├── healthcare/            # Medical scenario examples
│   │   ├── legal/                 # Legal document samples
│   │   ├── finance/               # Financial analysis cases
│   │   ├── real-estate/           # Property evaluation examples
│   │   └── [other categories]/    # Additional test scenarios
│   ├── outputs/
│   │   └── golden/                # Expected output benchmarks
│   └── config.json                # Testing configuration
├── examples/
│   └── workflow-examples.md       # Multi-prompt usage patterns
├── scripts/
│   ├── validate_json_examples.py  # JSON output validation
│   ├── run-all-tests.sh          # Complete test suite
│   └── clean_release.sh          # Release preparation
├── CONTRIBUTING.md                # Development guidelines
├── TROUBLESHOOTING.md            # Common issues and solutions
├── TESTING_EXPLAINED.md          # Testing methodology
└── README.md                     # This file
```

## Platform Compatibility

**Tested and Verified:**

- ChatGPT 4 and ChatGPT 5
- Claude 3 and Claude 4
- Compatible with other large language models

**Cross-Platform Features:**

- Standardized compatibility headers for consistent behavior
- Error handling and validation across different AI systems
- Temperature and parameter recommendations for optimal results

## Prompt Categories

### Simple Prompts (18 prompts)

Generate professional documents and content ready for immediate use.

#### Business and Professional

- **Business Plan Creator** - Executive summaries, market analysis, financial projections
- **Competitor Analysis** - Strategic market positioning and competitive intelligence
- **Decision Making Helper** - Systematic analysis frameworks for complex choices
- **Financial Analysis** - Investment evaluation, budget planning, performance assessment
- **Legal Document Analysis** - Contract review, risk assessment, plain-language summaries

#### Industry-Specific Applications

- **Healthcare Communication** - Patient instructions, medical documentation, care coordination
- **Real Estate Analysis** - Property valuation, market research, investment assessment
- **Professional Communication** - Business emails, presentations, meeting documentation
- **Educational Tools** - Lesson planning, assessment creation, curriculum development

#### Career and Professional Development

- **Resume Builder** - ATS-optimized professional resumes
- **Interview Preparation** - Comprehensive job interview planning and practice
- **Task Organization** - Priority management and productivity optimization

#### Creative and Content Development

- **Blog Content Planning** - Editorial calendars and content strategies
- **Social Media Strategy** - Platform-specific content planning and campaigns

### Structured Prompts (13 prompts)

Generate machine-readable data outputs for automation and integration workflows.

#### Data Classification and Processing

- **Email Classification** - Automated message routing and priority assignment
- **Sentiment Analysis** - Text emotion and opinion detection with confidence scoring
- **Content Categorization** - Automated content classification and tagging
- **Support Ticket Routing** - Customer service automation and workflow optimization

#### Data Extraction and Templates

- **Job Data Extraction** - Structured parsing of employment postings
- **FAQ Generation** - Automated frequently asked questions from documentation
- **CSV Message Export** - Structured data export for reporting and analysis

#### Advanced Processing

- **Chain-of-Thought Reasoning** - Complex problem-solving with transparent logic
- **Context Management** - Long document processing and analysis
- **Error Handling Templates** - Robust error recovery and validation patterns

#### System Integration

- **System Role Definitions** - AI behavior customization for specialized tasks
- **Few-Shot Learning** - Pattern recognition and adaptive response generation

## Quick Start Guide

### For Document Generation

1. Navigate to `prompts/simple/[category]/`
2. Select the appropriate prompt file for your use case
3. Copy the complete prompt text
4. Replace all bracketed placeholders `[EXAMPLE]` with your specific information
5. Execute the prompt in your preferred large language model
6. Receive professionally formatted output ready for immediate use

### For Data Processing

1. Navigate to `prompts/structured/[category]/`
2. Select the appropriate structured prompt
3. Ensure your input data matches the specified format requirements
4. Execute the prompt with temperature setting of 0.1 for consistent results
5. Receive valid JSON or CSV output suitable for automated processing

## Quality Assurance

### Testing Framework

- **31 total prompts** across 11 professional categories
- **28 realistic test scenarios** covering diverse use cases
- **Automated validation** for structured outputs and cross-platform compatibility
- **Golden output benchmarks** for quality comparison and regression testing

### Validation Tools

```bash
# Complete test suite execution
bash scripts/run-all-tests.sh

# Category-specific validation
python3 tests/test-runner.py --category [business|healthcare|legal|finance]

# JSON output verification
python3 scripts/validate_json_examples.py
```

### Quality Standards

- Cross-platform compatibility verified on multiple large language models
- Professional-grade output quality suitable for business and academic use
- Comprehensive error handling and edge case management
- Regular testing and validation to ensure continued reliability

## Target Applications

### Business and Enterprise

Strategic planning, financial analysis, legal document review, competitive intelligence, and operational decision-making tools for organizations of all sizes.

### Healthcare and Medical

Patient communication, medical documentation, treatment planning, and healthcare administration tools designed for medical professionals and healthcare organizations.

### Legal and Compliance

Contract analysis, document review, legal research, and compliance documentation tools for legal professionals and business legal departments.

### Education and Training

Curriculum development, assessment creation, educational content planning, and academic administration tools for educators and training organizations.

### Technical and Development

Data processing, classification systems, automated workflows, and integration tools for developers and technical teams.

## Contributing and Maintenance

### Development Guidelines

Comprehensive contribution guidelines are available in `CONTRIBUTING.md`, including:

- Prompt development standards and best practices
- Testing requirements and validation procedures
- Documentation standards and formatting guidelines
- Quality assurance processes and review criteria

### Issue Resolution

Common problems and solutions are documented in `TROUBLESHOOTING.md`, covering:

- Platform-specific compatibility issues
- Input formatting and validation problems
- Output quality optimization techniques
- Cross-platform behavior differences

### Testing Methodology

Detailed testing procedures are explained in `TESTING_EXPLAINED.md`, including:

- Automated testing framework architecture
- Manual validation procedures
- Quality benchmark establishment
- Regression testing protocols

## Project Statistics

- **31 production-ready prompts** spanning 11 professional categories
- **18 simple prompts** for document generation and content creation
- **13 structured prompts** for data processing and automation workflows
- **28 comprehensive test scenarios** with realistic input data
- **Cross-platform compatibility** verified on major large language model platforms
- **Open-source license** with active community contribution framework

## License and Support

This project is open-source and actively maintained. Community contributions are welcome through the established guidelines in `CONTRIBUTING.md`. For technical support and issue reporting, please refer to the project's issue tracking system and documentation resources.
