# User Stories

Project: **AI Bug Triage Assistant**

Personas: **Reporter** (anyone submitting a bug), **Developer** (fixes bugs), **Team Lead** (prioritizes and assigns work).

| ID    | User Story | Acceptance Criteria |
|-------|------------|---------------------|
| US-1  | As a **Reporter**, I want to submit a bug report with a title, description and steps to reproduce, so that the team knows about the problem. | Form validates required fields; report is saved and a confirmation is shown. |
| US-2  | As a **Reporter**, I want the system to automatically classify my bug's severity, so that I don't have to guess how serious it is. | Severity (Low / Medium / High / Critical) is assigned within a few seconds of submission. |
| US-3  | As a **Developer**, I want each bug to have an AI-suggested category (UI, backend, performance, security, etc.), so that I can quickly find bugs in my area. | Category is shown on the bug and can be used as a filter. |
| US-4  | As a **Developer**, I want to see probable root causes and suggested next steps for a bug, so that I can start debugging faster. | Each triaged bug shows at least one suggested cause and one next step. |
| US-5  | As a **Reporter**, I want to be warned if a similar bug already exists, so that I don't create duplicates. | Possible duplicates are listed with a similarity indicator before or after submission. |
| US-6  | As a **Team Lead**, I want a dashboard of all triaged bugs sorted by severity, so that I can see what to handle first. | Dashboard lists bugs, supports sorting and filtering by severity, category and status. |
| US-7  | As a **Team Lead**, I want to override the AI's severity or category, so that human judgment has the final say. | Severity and category can be edited; edits are saved and marked as manually set. |
| US-8  | As a **Team Lead**, I want to assign a bug to a developer and change its status, so that work is tracked. | Bug has an assignee and status (Open / In Progress / Resolved) that can be updated. |
| US-9  | As a **Developer**, I want to add comments to a bug, so that the team can discuss it in one place. | Comments are saved with author and timestamp and shown in order. |
| US-10 | As a **Team Lead**, I want to give feedback on whether the AI triage was helpful, so that the prompts can be improved over time. | Thumbs up/down on each AI result is stored and viewable. |
