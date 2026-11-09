# README Generation Prompt Template

**Role or Perspective:** Act as an open-source documentation maintainer writing for developers who are new to the project.

**Task Description:** Create a practical README from the supplied project information. Explain what the project does, prerequisites, installation, configuration, usage, scripts, and contribution or support guidance when information is available. Do not invent commands, environment variables, or features.

**Input Placeholder:**
```text
[PROJECT_NAME_AND_PURPOSE]
[TECH_STACK_AND_PREREQUISITES]
[PROJECT_STRUCTURE]
[INSTALLATION_AND_RUN_COMMANDS]
[ENVIRONMENT_VARIABLES_WITHOUT_SECRET_VALUES]
[FEATURES_AND_USAGE_EXAMPLES]
[TEST_AND_BUILD_COMMANDS]
```

**Expected Output Format:**
A Markdown README with:
1. Project title and overview.
2. Features.
3. Prerequisites and installation.
4. Configuration.
5. Usage examples.
6. Available scripts and tests.
7. Project structure.
8. Contribution and license sections only when relevant information is provided.
