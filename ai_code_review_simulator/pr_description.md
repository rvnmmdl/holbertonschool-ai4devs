# Pull Request: Add Automated Code Review Summary Feature

## Summary

Implements an automated code review summary feature for the AI Code Review Simulator.

The feature analyzes Python source code and generates structured feedback about common code-quality issues, helping developers identify problems before submitting a pull request.

## Changes

- Added automated source-code analysis.
- Added detection for long functions.
- Added detection for missing function documentation.
- Added detection for excessive nesting.
- Added detection for unused imports.
- Added structured review results with severity levels.
- Added recommendations for detected issues.
- Added input validation.
- Added unit tests for the new review functionality.

## Context

Developers can miss common code-quality issues during development, especially before creating a pull request.

This feature provides quick automated feedback and helps developers identify simple problems before human code review.

Related issue: #42

## Implementation

- Approximately 100–200 LOC.
- No external dependencies required.
- Designed as a small MVP feature.
- The automated review complements, but does not replace, human code review.

## Testing

- Added tests for valid Python code.
- Added tests for empty input.
- Added tests for long functions.
- Added tests for missing documentation.
- Added tests for excessive nesting.
- Added tests for unused imports.

All existing and new tests should pass before merging.