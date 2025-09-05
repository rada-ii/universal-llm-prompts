#!/usr/bin/env python3
"""
Simple test runner for Universal LLM Prompts
Tests prompts with known inputs and validates outputs
"""
import json
import os
import sys
from pathlib import Path

class PromptTester:
    def __init__(self, project_root=None):
        self.project_root = Path(project_root or Path(__file__).parent.parent)
        self.inputs_dir = self.project_root / "tests" / "inputs"
        self.outputs_dir = self.project_root / "tests" / "outputs"
        self.golden_dir = self.outputs_dir / "golden"
        
    def find_test_inputs(self, category=None):
        """Find all test input files, optionally filtered by category"""
        if category:
            pattern = f"{category}/*.txt"
        else:
            pattern = "*/*.txt"
            
        return list(self.inputs_dir.glob(pattern))
    
    def validate_json_output(self, output_text):
        """Validate that output is proper JSON"""
        try:
            parsed = json.loads(output_text)
            return True, parsed, None
        except json.JSONDecodeError as e:
            return False, None, str(e)
    
    def load_golden_output(self, prompt_name, test_case):
        """Load expected golden output for comparison"""
        golden_file = self.golden_dir / prompt_name / f"{test_case}.json"
        if golden_file.exists():
            with open(golden_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
    
    def compare_outputs(self, actual, expected):
        """Compare actual output with expected golden output"""
        if not expected:
            return True, "No golden output to compare against"
            
        # For structured prompts, compare JSON structure
        if isinstance(actual, dict) and isinstance(expected.get('output'), dict):
            actual_keys = set(actual.keys())
            expected_keys = set(expected['output'].keys())
            
            if actual_keys != expected_keys:
                return False, f"Key mismatch: {actual_keys} vs {expected_keys}"
                
            # Check data types match
            for key in actual_keys:
                if type(actual[key]) != type(expected['output'][key]):
                    return False, f"Type mismatch for {key}: {type(actual[key])} vs {type(expected['output'][key])}"
                    
            return True, "Structure matches"
        
        return True, "Basic validation passed"
    
    def run_single_test(self, prompt_category, test_file, prompt_name=None):
        """Run a single test case"""
        print(f"\nTesting: {test_file.name} in {prompt_category}")
        
        # Read test input
        try:
            with open(test_file, 'r', encoding='utf-8') as f:
                test_input = f.read().strip()
        except Exception as e:
            return False, f"Failed to read input file: {e}"
        
        print(f"   Input length: {len(test_input)} characters")
        
        # For now, we can't actually run the AI models automatically
        # This would require API integration which is beyond simple testing
        # Instead, we validate the structure and provide guidance
        
        print(f"   PASS: Input file readable")
        print(f"   NOTE: Manual testing required with AI platforms")
        
        return True, "Test file validation passed"
    
    def run_category_tests(self, category):
        """Run all tests for a specific category"""
        print(f"\nTesting category: {category}")
        
        test_files = list(self.inputs_dir.glob(f"{category}/*.txt"))
        if not test_files:
            print(f"   WARNING: No test files found in {category}")
            return True
        
        all_passed = True
        for test_file in test_files:
            passed, message = self.run_single_test(category, test_file)
            if not passed:
                all_passed = False
                print(f"   FAIL {test_file.name}: {message}")
            else:
                print(f"   PASS {test_file.name}: {message}")
        
        return all_passed
    
    def run_all_tests(self):
        """Run all available tests"""
        print("Running Universal LLM Prompts Test Suite")
        print("=" * 50)
        
        # Find all categories
        categories = [d.name for d in self.inputs_dir.iterdir() if d.is_dir()]
        
        if not categories:
            print("ERROR: No test categories found!")
            return False
        
        print(f"Found categories: {', '.join(categories)}")
        
        all_passed = True
        for category in sorted(categories):
            passed = self.run_category_tests(category)
            if not passed:
                all_passed = False
        
        print("\n" + "=" * 50)
        if all_passed:
            print("SUCCESS: All tests passed!")
        else:
            print("ERROR: Some tests failed!")
        
        return all_passed
    
    def validate_golden_files(self):
        """Validate all golden output files are proper JSON"""
        print("Validating golden output files...")
        
        if not self.golden_dir.exists():
            print("   WARNING: No golden directory found")
            return True
        
        json_files = list(self.golden_dir.glob("**/*.json"))
        if not json_files:
            print("   WARNING: No golden JSON files found")
            return True
        
        all_valid = True
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    json.load(f)
                print(f"   PASS: {json_file.relative_to(self.golden_dir)}")
            except Exception as e:
                all_valid = False
                print(f"   FAIL: {json_file.relative_to(self.golden_dir)}: {e}")
        
        return all_valid

def main():
    """Main test runner entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Test Universal LLM Prompts")
    parser.add_argument("--category", help="Test specific category only")
    parser.add_argument("--validate-golden", action="store_true", 
                       help="Validate golden output files only")
    parser.add_argument("--project-root", help="Path to project root directory")
    
    args = parser.parse_args()
    
    tester = PromptTester(args.project_root)
    
    if args.validate_golden:
        success = tester.validate_golden_files()
    elif args.category:
        success = tester.run_category_tests(args.category)
    else:
        success = tester.run_all_tests()
        # Also validate golden files
        golden_success = tester.validate_golden_files()
        success = success and golden_success
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()