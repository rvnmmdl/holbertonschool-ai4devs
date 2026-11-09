# Unit Test Generation Prompt Template

**Role or Perspective:** Act as a test engineer specializing in isolated, deterministic unit tests.

**Task Description:** Generate unit tests for the supplied function, class, or module using the stated test framework. Cover normal behavior, boundary conditions, and relevant failures. Mock external dependencies where appropriate; do not test implementation details unnecessarily.

**Input Placeholder:**
```text
[LANGUAGE_AND_TEST_FRAMEWORK]
[SOURCE_CODE]
[DEPENDENCIES_TO_MOCK]
[EXPECTED_BEHAVIOR_OR_ACCEPTANCE_CRITERIA]
[EXISTING_TEST_CONVENTIONS]
```

**Expected Output Format:**
1. Test coverage plan.
2. Complete test code in a language-labeled code block.
3. Explanation of each test case.
4. Command to run the tests.
5. Any assumptions or uncovered cases.
