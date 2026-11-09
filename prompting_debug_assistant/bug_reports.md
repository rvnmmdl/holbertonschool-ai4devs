# Bug Reports

## Bug Report – bug1.py
- **File**: `bug1.py` (fixed version: `bug1_fixed.py`)
- **Summary**: Off-by-one error in `last_n_items`. The function returned `n + 1` items, and for `n == len(items)` it returned `[5, 1, 2, 3, 4, 5]` instead of `[1, 2, 3, 4, 5]`.
- **Root Cause**: The loop started at `len(items) - n - 1`, one index too early. When `n == len(items)` the start index is `-1`, which Python treats as the last element.
- **Resolution**:
  - *AI suggestion*: start the range at `len(items) - n`.
  - *Manual edits*: none to the logic. I only added a `check()` helper and test cases.
  ```python
  # Before
  for i in range(len(items) - n - 1, len(items)):
  # After
  for i in range(len(items) - n, len(items)):
  ```
- **Lesson Learned**: Always test edge cases with minimal input (`n = 0`, `n == len(items)`). Negative indices in Python can hide an off-by-one error instead of raising one.

## Bug Report – bug2.js
- **File**: `bug2.js` (fixed version: `bug2_fixed.js`)
- **Summary**: Runtime `TypeError: Cannot read properties of undefined (reading 'city')` when a user has no address or does not exist.
- **Root Cause**: `user.address.city` was accessed without checking that `user` and `user.address` exist. User 2 has no `address`, and `users.find()` returns `undefined` for id 4.
- **Resolution**:
  - *AI suggestion*: use optional chaining with a default value.
  - *Manual edits*: I chose `"UNKNOWN"` as the default value, because the original code had no defined fallback.
  ```js
  // Before
  return user.address.city.toUpperCase();
  // After
  return user?.address?.city?.toUpperCase() ?? "UNKNOWN";
  ```
- **Lesson Learned**: Data from `find()` or from optional fields may be `undefined`. Handle missing values explicitly instead of wrapping everything in `try/catch`, which would also hide unrelated errors.

## Bug Report – bug3.java
- **File**: `bug3.java` (fixed version: `bug3_fixed.java`)
- **Summary**: The program did not compile (7 compiler errors) because of five syntax mistakes.
- **Root Cause**: Missing `;` after `return a + b`, missing `)` in `if (b == 0` and in the `println` call, `'Done'` written with single quotes (a `char` literal, not a `String`), and a missing closing `}` for the class.
- **Resolution**:
  - *AI suggestion*: add the semicolon and both parentheses, change `'Done'` to `"Done"`, and add the final `}`.
  - *Manual edits*: removed `public` from `class Calculator` so the file name can differ from the class name, and added a small `check()` method for tests (plain `assert` needs the `-ea` flag).
  ```java
  // Before
  String message = 'Done';
  // After
  String message = "Done";
  ```
- **Lesson Learned**: Read the compiler errors from the first one, because one missing character can produce several follow-up errors. In Java, single quotes are for `char` and double quotes are for `String`.

## Bug Report – bug4.py
- **File**: `bug4.py` (fixed version: `bug4_fixed.py`)
- **Summary**: Four misuses of data types and libraries. The script crashed at `json.loads`, and three more errors were hidden behind that first one.
- **Root Cause**:
  1. `json.loads()` received a `dict`, but it only accepts a JSON string.
  2. `total_price` added strings (`"10.5"`) to an integer.
  3. `input()` returns a `str`, so `age > 18` raised `TypeError`.
  4. `strptime` used the format `%d/%m/%Y` for a date written as `YYYY-MM-DD`.
- **Resolution**:
  - *AI suggestion*: pass `json.dumps(...)` to `json.loads`, convert prices with `float(p)`, convert the age with `int(...)`, and use the format `%Y-%m-%d`.
  - *Manual edits*: refactored the top-level script into functions (`load_config`, `total_price`, `is_adult`, `parse_deadline`) so it can be tested without a blocking `input()` call. The original rule `age > 18` was kept unchanged.
  ```python
  # Before
  total += p
  age = input("Enter your age: ")
  # After
  total += float(p)
  age = int(input("Enter your age: "))
  ```
- **Lesson Learned**: Check the type a library function expects and the type your data really has (`input()` always returns text). One crash can hide other bugs, so fix and re-run until the script is clean. `Decimal` would be safer than `float` for real money calculations.

## Bug Report – bug5.js
- **File**: `bug5.js` (fixed version: `bug5_fixed.js`)
- **Summary**: Logical errors. `getGrade` never returned "C" or "A", and `isPassing(50)` returned `false`.
- **Root Cause**: In `getGrade`, the conditions were ordered from the lowest threshold to the highest, so every score of 50 or more matched `>= 50` first and returned "E". In `isPassing`, `>` was used instead of `>=`, so the minimum passing score of 50 failed.
- **Resolution**:
  - *AI suggestion*: check the highest threshold first and change `>` to `>=`.
  - *Manual edits*: none to the logic. I added boundary-value tests (90, 70, 50 and the values just below them).
  ```js
  // Before
  if (score >= 50) return "E"; else if (score >= 70) return "C"; ...
  return score > 50;
  // After
  if (score >= 90) return "A"; else if (score >= 70) return "C"; else if (score >= 50) return "E";
  return score >= 50;
  ```
- **Lesson Learned**: In an `if / else if` chain the order matters: put the most specific (highest) condition first. Always test the boundary values, because that is where `>` versus `>=` mistakes show up. Fixing only the operator is not enough when the order is also wrong.

## Bug Report – bug6.py
- **File**: `bug6.py` (fixed version: `bug6_fixed.py`)
- **Summary**: Two loop-logic bugs. `remove_negatives` left `-2` in the result (`[3, -2, 5, 8]`), and `count_down(3)` printed `3` forever.
- **Root Cause**: `remove_negatives` removed items from the list while iterating over the same list. The items shift left after a removal and the iterator skips the next one. In `count_down`, the loop variable `i` was never decremented, so `while i > 0` was always true.
- **Resolution**:
  - *AI suggestion*: iterate over a copy (`numbers[:]`) and add `i -= 1` inside the `while` loop.
  - *Manual edits*: none to the logic. The docstrings were removed from the fixed file only to keep it within the 40-line limit, and `io.StringIO` was used to capture the printed output for testing.
  ```python
  # Before
  for n in numbers:
  # After
  for n in numbers[:]:
  ```
- **Lesson Learned**: Never modify a collection while iterating over it; iterate over a copy or build a new list. Every `while` loop needs a statement that moves it toward its end condition.
