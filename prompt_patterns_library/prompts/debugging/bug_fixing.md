# Bug Fixing Prompt Template

**Role or Perspective:** Act as a careful software engineer responsible for fixing defects with minimal regression risk.

**Task Description:** Reproduce the described behavior conceptually from the provided details, locate the likely defect, and propose the smallest reliable correction. Preserve unrelated functionality and avoid broad rewrites. If the input is insufficient to identify the defect, state what is missing.

**Input Placeholder:**
```text
[BUG_DESCRIPTION]
[RELEVANT_SOURCE_CODE]
[REPRODUCTION_STEPS]
[EXPECTED_RESULT]
[ACTUAL_RESULT]
[TESTS_OR_CONSTRAINTS]
```

**Expected Output Format:**
1. Root-cause explanation (or clearly labeled hypotheses).
2. Minimal patch or corrected code.
3. Explanation of the change.
4. Regression tests covering the reported issue.
5. Remaining risks or unanswered questions.
