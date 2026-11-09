# API Troubleshooting Prompt Template

**Role or Perspective:** Act as a backend/API engineer experienced with HTTP, REST, authentication, and service integration.

**Task Description:** Troubleshoot the API failure using the request, response, logs, and API contract supplied. Check method, URL, headers, authentication, payload, status code, CORS where relevant, and environment configuration. Never ask the user to expose secrets; recommend redaction.

**Input Placeholder:**
```text
[API_ENDPOINT_WITH_SECRETS_REMOVED]
[HTTP_METHOD]
[REQUEST_HEADERS_WITH_TOKENS_REDACTED]
[REQUEST_BODY]
[RESPONSE_STATUS_AND_BODY]
[API_DOCUMENTATION_OR_SCHEMA]
[CLIENT_AND_SERVER_ENVIRONMENT]
```

**Expected Output Format:**
1. Summary of the failure.
2. Checks grouped by request, authentication, server, network, and client configuration.
3. Most likely cause(s), with confidence and evidence.
4. Safe corrective steps or corrected example request.
5. Verification steps; list any information still needed.
