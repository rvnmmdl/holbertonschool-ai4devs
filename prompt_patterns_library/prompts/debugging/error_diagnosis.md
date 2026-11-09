# Error Diagnosis Prompt Template

**Role or Perspective:** Act as an experienced debugging engineer who investigates problems systematically.

**Task Description:** Diagnose the reported error using only the supplied evidence. Trace the likely failure path, separate confirmed facts from hypotheses, and identify the smallest useful next check. Do not invent missing logs, files, or environment details.

**Input Placeholder:**
```text
[ERROR_MESSAGE_OR_STACK_TRACE]
[RELEVANT_CODE]
[ENVIRONMENT_AND_VERSIONS]
[STEPS_TO_REPRODUCE]
[EXPECTED_BEHAVIOR]
[ACTUAL_BEHAVIOR]
```

**Expected Output Format:**
1. Plain-language explanation of the error.
2. Most likely causes, ranked by confidence.
3. Evidence supporting each cause.
4. Step-by-step diagnostic checks.
5. Minimal fix if the evidence supports one; otherwise, request the exact missing information.
