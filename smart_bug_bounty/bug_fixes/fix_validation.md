# Fix Validation

## bug1.py
- **Original Issue**: Incorrect average caused by subtracting `1`.
- **Fix Applied**: Removed `- 1` from the average calculation.
- **Test Results**: Compilation passed; normalization returned `[0.5, 1.0, 1.5]`.

## bug2.js
- **Original Issue**: Out-of-range array access and unsafe access when a user is missing.
- **Fix Applied**: Changed `<=` to `<` and handled missing users with `null`.
- **Test Results**: Passed Node.js syntax and behavior tests. Existing user returned `Alice`; missing user returned `null`.

## bug3.java
- **Original Issue**: Input list was modified during indexed iteration, causing skipped elements.
- **Fix Applied**: Stopped removing elements from the input list during iteration.
- **Test Results**: Compilation passed; deduplication returned `[1, 2, 3]`.

## bug4.py
- **Original Issue**: First word occurrence was initialized to `0`.
- **Fix Applied**: Initialized new words with `1`.
- **Test Results**: Compilation passed; output was `{'python': 2, 'code': 1}` and `python`.

## bug5.js
- **Original Issue**: Fetch errors were logged without rejecting the Promise.
- **Fix Applied**: Added `reject(error)` and cleared the timeout on error.
- **Test Results**: Syntax check passed; local invalid-JSON test reached the rejection handler.

## bug6.sql
- **Original Issue**: `HAVING total_spent > 60` is not portable across SQL databases.
- **Fix Applied**: Changed it to `HAVING SUM(amount) > 60`.
- **Test Results**: SQLite execution passed; result was `[(102, 80)]`.

## Validation Summary
All 6 fixed snippets passed their applicable compilation/syntax and behavior tests.
