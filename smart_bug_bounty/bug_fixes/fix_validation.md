# Fix Validation

All commands below were run from the `smart_bug_bounty/bug_fixes/` directory.
Each fix was executed and the real output is shown, so every result can be reproduced.

## Directory structure

```text
smart_bug_bounty/
└── bug_fixes/
    ├── bug1_fixed.py
    ├── bug2_fixed.js
    ├── bug3_fixed.java
    ├── bug4_fixed.py
    ├── bug5_fixed.js
    ├── bug6_fixed.sql
    └── fix_validation.md
```

Mapping of original files to fixed files:

| Original (`bug_snippets/`) | Fixed (`bug_fixes/`) |
|----------------------------|----------------------|
| `bug1.py`   | `bug1_fixed.py`   |
| `bug2.js`   | `bug2_fixed.js`   |
| `bug3.java` | `bug3_fixed.java` |
| `bug4.py`   | `bug4_fixed.py`   |
| `bug5.js`   | `bug5_fixed.js`   |
| `bug6.sql`  | `bug6_fixed.sql`  |

---

## bug1.py -> bug1_fixed.py

- **Original Issue:** The average calculation used an incorrect `- 1` adjustment.
- **Fix Applied:** Removed the `- 1` adjustment so the average is `total / len(numbers)`.
- **Command:** `python3 bug1_fixed.py`
- **Actual Output:**
  ```text
  [0.5, 1.0, 1.5]
  ```
- **Extra check:** `average([10, 20, 30]) == 20.0` and `normalize_scores([10, 20, 30]) == [0.5, 1.0, 1.5]` (both asserts passed).
- **Test Results:** 2/2 checks passed
- **Result:** PASS

## bug2.js -> bug2_fixed.js

- **Original Issue:** The loop used `<=` and could access an index outside the array. A missing user could also cause unsafe property access.
- **Fix Applied:** Changed the loop condition to `i < users.length` and `getUserName` returns `null` when no user is found.
- **Command:** `node bug2_fixed.js`
- **Actual Output:**
  ```text
  Alice
  null
  ```
- **Test Results:** 2/2 cases passed (existing ID `1` -> `Alice`, missing ID `3` -> `null`, no crash)
- **Result:** PASS

## bug3.java -> bug3_fixed.java

- **Original Issue:** The original implementation modified the input list while iterating over it, which could skip elements.
- **Fix Applied:** Created a separate `result` list and added each value only when it was not already present.
- **Command:** `java bug3_fixed.java`
- **Actual Output:**
  ```text
  [1, 2, 3]
  ```
- **Test Results:** 1/1 case passed (input `[1, 2, 2, 3, 3]` -> `[1, 2, 3]`)
- **Result:** PASS

## bug4.py -> bug4_fixed.py

- **Original Issue:** A new word was initialized with count `0`, so the first occurrence was missed.
- **Fix Applied:** A new word is initialized with count `1`.
- **Command:** `python3 bug4_fixed.py`
- **Actual Output:**
  ```text
  {'python': 2, 'code': 1}
  python
  ```
- **Test Results:** 2/2 checks passed (correct counts, most common word is `python`)
- **Result:** PASS

## bug5.js -> bug5_fixed.js

- **Original Issue:** The error handler logged the fetch error but did not reject the Promise, so callers could not handle the failure.
- **Fix Applied:** Cleared the timeout and called `reject(error)` inside `.catch()`.
- **Test method:** `fetch` was replaced with a mock (preloaded via `node -r`) because the real URL is not reachable.
- **Command (success):** `node -r ./mock_ok.js bug5_fixed.js`
  ```text
  { ok: true, items: [ 1, 2 ] }
  ```
- **Command (failure):** `node -r ./mock_fail.js bug5_fixed.js`
  ```text
  Request failed: Error: Network down
  ...
  Error: Network down
  ```
  The second `Error: Network down` line is printed by the final `.catch(error => console.error(error))`,
  which proves the rejection is propagated to the caller.
- **Test Results:** 2/2 cases passed (success resolves, failure rejects)
- **Result:** PASS

## bug6.sql -> bug6_fixed.sql

- **Original Issue:** The query used a SELECT alias in `HAVING`, which is not portable across SQL implementations.
- **Fix Applied:** Replaced the alias in `HAVING` with the aggregate expression `SUM(amount) > 60`.
- **Command:** executed with SQLite (in-memory database) using Python's `sqlite3` module.
- **Actual Output (`customer_id`, `total_spent`):**
  ```text
  [(102, 80)]
  ```
- **Test Results:** 1/1 case passed (customer `101` has paid total 50.00 and is filtered out; customer `102` has 80.00 and is returned)
- **Result:** PASS

---

## Summary

| Fix | Command | Result |
|-----|---------|--------|
| bug1_fixed.py   | `python3 bug1_fixed.py`   | PASS |
| bug2_fixed.js   | `node bug2_fixed.js`      | PASS |
| bug3_fixed.java | `java bug3_fixed.java`    | PASS |
| bug4_fixed.py   | `python3 bug4_fixed.py`   | PASS |
| bug5_fixed.js   | `node -r ./mock_*.js bug5_fixed.js` | PASS |
| bug6_fixed.sql  | SQLite in-memory run      | PASS |

6/6 fixes validated with real command output.
