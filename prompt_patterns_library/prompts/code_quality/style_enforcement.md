# Style Enforcement Prompt Template

**Role or Perspective:** Act as a code reviewer enforcing the conventions of the specified language, framework, and project.

**Task Description:** Review the input for style and consistency issues. Apply the supplied style guide; if none is supplied, use widely accepted conventions for the stated language and clearly identify the conventions assumed. Do not make unrelated logic changes.

**Input Placeholder:**
```text
[LANGUAGE_AND_FRAMEWORK]
[STYLE_GUIDE_OR_LINTER_CONFIG]
[CODE_BLOCK]
```

**Expected Output Format:**
1. A table with issue, location, and recommended correction.
2. Corrected code in a language-labeled code block.
3. A short list of conventions applied.
4. Any unresolved ambiguity that requires the project owner's decision.
