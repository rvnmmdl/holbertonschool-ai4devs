# API Documentation Prompt Template

**Role or Perspective:** Act as an API documentation specialist writing clear, developer-focused reference material.

**Task Description:** Document the supplied API endpoints according to the provided contract or implementation. Include method, path, purpose, authentication, parameters, request and response schemas, status codes, and examples. Do not invent undocumented behavior.

**Input Placeholder:**
```text
[API_SPECIFICATION_OR_ROUTE_CODE]
[AUTHENTICATION_METHOD]
[SCHEMAS_AND_TYPES]
[ERROR_RESPONSES]
[BASE_URL_PLACEHOLDER]
```

**Expected Output Format:**
1. API overview and authentication notes.
2. One section per endpoint with method and path.
3. Parameters and request body schema.
4. Successful response schema and example.
5. Known error status codes and examples.
6. Notes on pagination, rate limits, or versioning only if specified.
