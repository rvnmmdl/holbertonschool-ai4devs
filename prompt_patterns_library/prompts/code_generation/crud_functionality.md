# CRUD Functionality Prompt Template

**Role or Perspective:** Act as a full-stack software engineer designing maintainable create, read, update, and delete workflows.

**Task Description:** Implement CRUD functionality for the specified resource using the given stack and data model. Respect validation, authorization, and existing architecture. Include confirmation and error handling for destructive actions. Do not assume permissions or schema fields that were not provided.

**Input Placeholder:**
```text
[LANGUAGE_AND_FRAMEWORK]
[RESOURCE_NAME_AND_DATA_MODEL]
[DATABASE_OR_API_LAYER]
[CRUD_REQUIREMENTS]
[AUTHORIZATION_AND_VALIDATION_RULES]
[UI_REQUIREMENTS_IF_APPLICABLE]
[EXISTING_PROJECT_CONVENTIONS]
```

**Expected Output Format:**
1. Proposed file structure and implementation plan.
2. Create, read, update, and delete implementation.
3. Validation and authorization handling.
4. Example requests or UI usage.
5. Tests for success, invalid input, unauthorized access, missing records, and relevant failure cases.
