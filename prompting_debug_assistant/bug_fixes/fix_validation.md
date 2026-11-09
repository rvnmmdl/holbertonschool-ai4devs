# Fix Validation

All fixed files are in `bug_fixes/`. Each file contains its own test cases (assertions plus printed results) and was executed after fixing:

| Language | Command used |
|---|---|
| Python | `python3 <file>` |
| JavaScript | `node <file>` (Node.js v22) |
| Java | `java bug3_fixed.java` (source-file mode) |

Every file ended with `All tests passed` and exit code `0`.

---

## Bug 1 – bug1_fixed.py
**Fix applied**: `range(len(items) - n - 1, len(items))` changed to `range(len(items) - n, len(items))`.
**Runs without errors?** Yes. **Passes intended test cases?** Yes.

| Input | Expected Output | Actual Output | Result |
|---|---|---|---|
| `[1,2,3,4,5]`, n=3 | `[3,4,5]` | `[3,4,5]` | ✅ |
| `[1,2,3,4,5]`, n=2 | `[4,5]` | `[4,5]` | ✅ |
| `[1,2,3,4,5]`, n=5 | `[1,2,3,4,5]` | `[1,2,3,4,5]` | ✅ |
| `[1,2,3,4,5]`, n=0 | `[]` | `[]` | ✅ |
| `[7]`, n=1 | `[7]` | `[7]` | ✅ |
| `[]`, n=0 | `[]` | `[]` | ✅ |

**Manual tweaks**: None. The AI's suggestion worked as given. I only added a `check()` helper and test cases.

---

## Bug 2 – bug2_fixed.js
**Fix applied**: `user.address.city.toUpperCase()` replaced with `user?.address?.city?.toUpperCase() ?? "UNKNOWN"`.
**Runs without errors?** Yes (the `TypeError` is gone). **Passes intended test cases?** Yes.

| Input (user id) | Expected Output | Actual Output | Result |
|---|---|---|---|
| `1` | `BAKU` | `BAKU` | ✅ |
| `2` (no address) | `UNKNOWN` | `UNKNOWN` | ✅ |
| `3` | `GANJA` | `GANJA` | ✅ |
| `4` (user does not exist) | `UNKNOWN` | `UNKNOWN` | ✅ |

**Manual tweaks**: None to the fix. The original code had no defined fallback value, so the choice of `"UNKNOWN"` as the default is my decision.

---

## Bug 3 – bug3_fixed.java
**Fix applied**: added `;` after `return a + b`, added the missing `)` in `if (b == 0)` and in the `println` call, changed `'Done'` to `"Done"`, and added the closing `}` of the class.
**Runs without errors?** Yes (the 7 compile errors are gone). **Passes intended test cases?** Yes.

| Input | Expected Output | Actual Output | Result |
|---|---|---|---|
| `add(10, 5)` | `15.0` | `15.0` | ✅ |
| `add(-1, 1)` | `0.0` | `0.0` | ✅ |
| `divide(10, 5)` | `2.0` | `2.0` | ✅ |
| `divide(7, 2)` | `3.5` | `3.5` | ✅ |
| `divide(1, 0)` | `0.0` (prints "Cannot divide by zero") | `0.0` (message printed) | ✅ |

The program's own output was also correct: `Sum: 15`, `Quotient: 2.0`, `Done`.

**Manual tweaks**: Removed the `public` keyword from `class Calculator`, so the file can have a different name (`bug3_fixed.java`) and still compile with `javac`. Added a small `check()` method for the tests, because plain `assert` needs the `-ea` flag. Values are compared as `double`, which is why `add` results show as `15.0`.

---

## Bug 4 – bug4_fixed.py
**Fix applied**: `json.loads` now receives a JSON string (`json.dumps(...)`), prices are converted with `float(p)`, the age is converted with `int(...)`, and the date format was changed to `%Y-%m-%d`.
**Runs without errors?** Yes. **Passes intended test cases?** Yes.

| Input | Expected Output | Actual Output | Result |
|---|---|---|---|
| `load_config('{"currency":"AZN","tax":0.18}')` → currency | `AZN` | `AZN` | ✅ |
| same → tax | `0.18` | `0.18` | ✅ |
| `total_price(["10.5","20","5.25"])` | `35.75` | `35.75` | ✅ |
| `total_price([])` | `0` | `0` | ✅ |
| `is_adult("25")` | `True` | `True` | ✅ |
| `is_adult("10")` | `False` | `False` | ✅ |
| `parse_deadline("2026-11-09")` | `datetime(2026, 11, 9)` | `2026-11-09 00:00:00` | ✅ |
| `parse_deadline("09/11/2026")` | raises `ValueError` | raises `ValueError` | ✅ |

**Manual tweaks**: The AI's four fixes were applied as suggested, but I also refactored the script into functions (`load_config`, `total_price`, `is_adult`, `parse_deadline`). The original had top-level code and a blocking `input()` call that cannot be tested automatically. `float` was used (as in the log); `Decimal` would be safer for real money. The original rule `age > 18` was kept unchanged, so `is_adult("18")` returns `False`; this was not tested because it is a business-rule question, not a bug.

---

## Bug 5 – bug5_fixed.js
**Fix applied**: `getGrade` now checks the highest threshold first (90, then 70, then 50), and `isPassing` uses `score >= 50`.
**Runs without errors?** Yes. **Passes intended test cases?** Yes.

| Input | Expected Output | Actual Output | Result |
|---|---|---|---|
| `getGrade(95)` | `A` | `A` | ✅ |
| `getGrade(90)` | `A` | `A` | ✅ |
| `getGrade(89)` | `C` | `C` | ✅ |
| `getGrade(72)` | `C` | `C` | ✅ |
| `getGrade(70)` | `C` | `C` | ✅ |
| `getGrade(69)` | `E` | `E` | ✅ |
| `getGrade(50)` | `E` | `E` | ✅ |
| `getGrade(49)` | `F` | `F` | ✅ |
| `getGrade(30)` | `F` | `F` | ✅ |
| `isPassing(50)` | `true` | `true` | ✅ |
| `isPassing(49)` | `false` | `false` | ✅ |
| `isPassing(95)` | `true` | `true` | ✅ |

**Manual tweaks**: None. The boundary values (90, 70, 50 and the values just below them) were added as test cases because off-by-one mistakes usually appear there.

---

## Bug 6 – bug6_fixed.py
**Fix applied**: `remove_negatives` now iterates over a copy (`numbers[:]`), and `count_down` decrements `i -= 1` inside the loop.
**Runs without errors?** Yes (no more infinite loop). **Passes intended test cases?** Yes.

| Input | Expected Output | Actual Output | Result |
|---|---|---|---|
| `remove_negatives([3,-1,-2,5,-7,8])` | `[3,5,8]` | `[3,5,8]` | ✅ |
| `remove_negatives([])` | `[]` | `[]` | ✅ |
| `remove_negatives([-1,-2])` | `[]` | `[]` | ✅ |
| `remove_negatives([1,2])` | `[1,2]` | `[1,2]` | ✅ |
| `remove_negatives(data) is data` | `True` (in place) | `True` | ✅ |
| `count_down(3)` output | `3\n2\n1\nLiftoff!\n` | `3\n2\n1\nLiftoff!\n` | ✅ |
| `count_down(0)` output | `Liftoff!\n` | `Liftoff!\n` | ✅ |

**Manual tweaks**: The AI's fix worked as given. To test `count_down`, I captured its printed output with `io.StringIO` and `redirect_stdout`.

---

## Summary

| Bug | File | Tests | Result |
|---|---|---|---|
| 1 | `bug1_fixed.py` | 6 | ✅ All passed |
| 2 | `bug2_fixed.js` | 4 | ✅ All passed |
| 3 | `bug3_fixed.java` | 5 | ✅ All passed |
| 4 | `bug4_fixed.py` | 8 | ✅ All passed |
| 5 | `bug5_fixed.js` | 12 | ✅ All passed |
| 6 | `bug6_fixed.py` | 7 | ✅ All passed |
