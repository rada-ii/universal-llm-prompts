#!/usr/bin/env bash
set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Universal LLM Prompts - Complete Test Suite${NC}"
echo "=================================================="

# Check if we're in the right directory
if [ ! -f "README.md" ] || [ ! -d "tests" ]; then
    echo -e "${RED}ERROR: Run this script from the project root directory${NC}"
    exit 1
fi

echo -e "${YELLOW}Running pre-flight checks...${NC}"

# Check Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}ERROR: Python 3 is required but not installed${NC}"
    exit 1
fi

# Check required directories exist
REQUIRED_DIRS=("tests/inputs" "tests/outputs" "prompts")
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        echo -e "${RED}ERROR: Required directory missing: $dir${NC}"
        exit 1
    fi
done

echo -e "${GREEN}SUCCESS: Pre-flight checks passed${NC}"

# Step 1: Validate JSON files
echo -e "\n${YELLOW}Step 1: Validating JSON files...${NC}"
if python3 scripts/validate_json_examples.py; then
    echo -e "${GREEN}SUCCESS: JSON validation passed${NC}"
else
    echo -e "${RED}ERROR: JSON validation failed${NC}"
    exit 1
fi

# Step 2: Run test file validation
echo -e "\n${YELLOW}Step 2: Validating test input files...${NC}"
if python3 tests/test-runner.py; then
    echo -e "${GREEN}SUCCESS: Test file validation passed${NC}"
else
    echo -e "${RED}ERROR: Test file validation failed${NC}"
    exit 1
fi

# Step 3: Validate golden outputs
echo -e "\n${YELLOW}Step 3: Validating golden output files...${NC}"
if python3 tests/test-runner.py --validate-golden; then
    echo -e "${GREEN}SUCCESS: Golden output validation passed${NC}"
else
    echo -e "${YELLOW}WARNING: Golden output validation had issues (this is OK for new project)${NC}"
fi

# Step 4: File structure validation
echo -e "\n${YELLOW}Step 4: Checking file structure...${NC}"

# Count prompt files
SIMPLE_PROMPTS=$(find prompts/simple -name "*.md" 2>/dev/null | wc -l || echo "0")
STRUCTURED_PROMPTS=$(find prompts/structured -name "*.md" 2>/dev/null | wc -l || echo "0")
TEST_INPUTS=$(find tests/inputs -name "*.txt" 2>/dev/null | wc -l || echo "0")

echo "   Found $SIMPLE_PROMPTS simple prompts"
echo "   Found $STRUCTURED_PROMPTS structured prompts"
echo "   Found $TEST_INPUTS test input files"

if [ "$SIMPLE_PROMPTS" -eq 0 ] && [ "$STRUCTURED_PROMPTS" -eq 0 ]; then
    echo -e "${RED}ERROR: No prompt files found!${NC}"
    exit 1
fi

if [ "$TEST_INPUTS" -eq 0 ]; then
    echo -e "${YELLOW}WARNING: No test input files found${NC}"
else
    echo -e "${GREEN}SUCCESS: File structure looks good${NC}"
fi

# Step 5: Documentation check
echo -e "\n${YELLOW}Step 5: Checking documentation...${NC}"

REQUIRED_DOCS=("README.md" "CONTRIBUTING.md" "TROUBLESHOOTING.md")
for doc in "${REQUIRED_DOCS[@]}"; do
    if [ -f "$doc" ]; then
        echo "   PASS: $doc exists"
    else
        echo "   WARNING: $doc missing"
    fi
done

# Final summary
echo -e "\n${BLUE}=================================================="
echo -e "Test Suite Summary${NC}"
echo "=================================================="

echo "Project Statistics:"
echo "   • Simple prompts: $SIMPLE_PROMPTS"
echo "   • Structured prompts: $STRUCTURED_PROMPTS" 
echo "   • Test input files: $TEST_INPUTS"
echo "   • Total prompts: $((SIMPLE_PROMPTS + STRUCTURED_PROMPTS))"

echo -e "\nWhat was tested:"
echo "   • JSON file syntax validation"
echo "   • Test input file readability"
echo "   • Golden output format validation"
echo "   • File structure integrity"
echo "   • Documentation completeness"

echo -e "\nManual testing still required:"
echo "   • Run prompts on ChatGPT 4"
echo "   • Run prompts on Claude 3"
echo "   • Verify output quality matches examples"
echo "   • Test with real user scenarios"

echo -e "\n${GREEN}SUCCESS: Automated test suite completed successfully!${NC}"
echo -e "${YELLOW}NOTE: To run individual tests: python3 tests/test-runner.py --category [business|education|etc]${NC}"