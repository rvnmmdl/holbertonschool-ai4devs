# Fix Validation

## bug1.py -> bug_fixes/bug1_fixed.py

- **Original Issue:** The average calculation used an incorrect `- 1` adjustment.
- **Fix Applied:** Removed the `- 1` adjustment so the average is calculated as `total / len(numbers)`.
- **Validation:** `average([10, 20, 30])` returns `20.0`, and normalization returns `[0.5, 1.0, 1.5]`.
- **Result:** PASS

## bug2.js -> bug_fixes/bug2_fixed.js

- **Original Issue:** The loop could access an index outside the array because it used `<=`. Missing users could also cause unsafe property access.
- **Fix Applied:** Changed the loop condition to `< users.length` and returned `null` when no user is found.
- **Validation:** Existing user ID `1` returns `Alice`; missing user ID `3` returns `null`.
- **Result:** PASS

## bug3.java -> bug_fixes/bug3_fixed.java

- **Original Issue:** The original implementation modified the input list while iterating over it, which could skip elements.
- **Fix Applied:** Created a separate result list and added each value only when it was not already present.
- **Validation:** Input `[1, 2, 2, 3, 3]` produces `[1, 2, 3]`.
- **Result:** PASS

## bug4.py -> bug_fixes/bug4_fixed.py

- **Original Issue:** A new word was initialized with count `0`, causing the first occurrence to be missed.
- **Fix Applied:** Initialized a new word with count `1`.
- **Validation:** `"python python code"` produces `{'python': 2, 'code': 1}` and the most common word is `python`.
- **Result:** PASS

## bug5.js -> bug_fixes/bug5_fixed.js

- **Original Issue:** The original error handler logged the fetch error but did not reject the Promise, so callers could not properly handle the failure.
- **Fix Applied:** Cleared the timeout and called `reject(error)` inside `.catch()`.
- **Validation:** Successful responses resolve the Promise; fetch failures are propagated to the final `.catch()` handler.
- **Result:** PASS

## bug6.sql -> bug_fixes/bug6_fixed.sql

- **Original Issue:** The query used a SELECT alias in `HAVING`, which is not portable across SQL implementations.
- **Fix Applied:** Replaced the alias in `HAVING` with the aggregate expression `SUM(amount) > 60`.
- **Validation:** With the sample data, the query returns customer `102` with total paid amount `80.00`.
- **Result:** PASS

## Summary

All six fixed files have a direct one-to-one mapping to the original buggy files:

- `bug1.py` -> `bug_fixes/bug1_fixed.py`
- `bug2.js` -> `bug_fixes/bug2_fixed.js`
- `bug3.java` -> `bug_fixes/bug3_fixed.java`
- `bug4.py` -> `bug_fixes/bug4_fixed.py`
- `bug5.js` -> `bug_fixes/bug5_fixed.js`
- `bug6.sql` -> `bug_fixes/bug6_fixed.sql`

Each fix is explicitly validated against its corresponding original bug.
