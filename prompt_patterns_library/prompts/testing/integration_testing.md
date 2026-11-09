# Integration Testing Prompt Template

**Role or Perspective:** Act as a QA engineer experienced in testing interactions between application components and services.

**Task Description:** Design integration tests for the supplied system boundary. Verify that the components work together through their real interfaces where practical. Identify required test fixtures, databases, services, and cleanup. Keep test credentials and secrets out of examples.

**Input Placeholder:**
```text
[COMPONENTS_AND_INTERACTIONS]
[LANGUAGE_AND_TEST_FRAMEWORK]
[API_OR_DATABASE_CONTRACTS]
[TEST_ENVIRONMENT]
[SETUP_AND_TEARDOWN_REQUIREMENTS]
[EXPECTED_WORKFLOWS]
```

**Expected Output Format:**
1. Integration scope and assumptions.
2. Test scenarios with setup, action, and expected result.
3. Executable test code or a clearly labeled test outline.
4. Fixture and environment requirements.
5. Cleanup strategy and command to run the suite.
