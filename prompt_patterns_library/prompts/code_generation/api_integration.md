# API Integration Prompt Template

**Role or Perspective:** Act as a full-stack engineer experienced in reliable frontend-to-backend API integration.

**Task Description:** Implement the requested API integration using the supplied endpoint contract and application architecture. Include loading, success, empty, and error states as relevant. Handle configuration safely, avoid hardcoded secrets, and follow the project's existing data-fetching conventions.

**Input Placeholder:**
```text
[FRAMEWORK_AND_LANGUAGE]
[API_CONTRACT_AND_ENDPOINTS]
[AUTHENTICATION_REQUIREMENTS_WITH_SECRETS_REDACTED]
[REQUEST_AND_RESPONSE_TYPES]
[EXISTING_PROJECT_ARCHITECTURE]
[UI_OR_WORKFLOW_REQUIREMENTS]
```

**Expected Output Format:**
1. Files to create or modify.
2. Implementation code for each file.
3. Type definitions and configuration requirements.
4. Error-handling and state-management explanation.
5. Verification steps and tests.
