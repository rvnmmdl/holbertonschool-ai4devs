# Code Refactoring Prompt Template

**Role or Perspective:** Act as a senior software engineer experienced in clean code, maintainability, and software design principles.

**Task Description:** Refactor the supplied code to improve readability, structure, and maintainability without changing its externally observable behavior. Identify duplication and overly complex logic. Preserve existing APIs unless a change is explicitly requested. Explain any assumptions and flag behavior that cannot be safely inferred.

**Input Placeholder:**
```text
[LANGUAGE_AND_FRAMEWORK]
[CODE_BLOCK]
[OPTIONAL_CONSTRAINTS_OR_EXISTING_TESTS]
```

**Expected Output Format:**
1. Brief summary of the proposed refactoring.
2. Refactored code in a language-labeled code block.
3. Bullet list of important changes and why they help.
4. Compatibility risks or assumptions.
5. Suggested tests to confirm behavior is unchanged.
