# Edge Case Identification Prompt Template

**Role or Perspective:** Act as a quality engineer focused on boundary conditions, unusual inputs, and failure paths.

**Task Description:** Identify edge cases for the supplied feature or function. Consider empty, missing, malformed, extreme, duplicate, out-of-order, and unexpected inputs where relevant. Tailor cases to the actual requirements; do not add arbitrary cases that cannot occur.

**Input Placeholder:**
```text
[FEATURE_OR_FUNCTION_DESCRIPTION]
[RELEVANT_CODE_OR_INTERFACE]
[INPUT_TYPES_AND_VALIDATION_RULES]
[BUSINESS_RULES]
[KNOWN_LIMITS_AND_CONSTRAINTS]
```

**Expected Output Format:**
A table containing:
- Edge case
- Example input or condition
- Expected behavior
- Priority (high, medium, low)
- Suggested test

Finish with the highest-priority cases to implement first and any requirement gaps that need clarification.
