# Fix Validation

## Bug 1 – bug1_fixed.py
- **Input**: `[1,2,3,4,5]`, n=3
- **Expected Output**: `[3,4,5]`
- **Actual Output**: `[3,4,5]` ✅

- **Input**: `[1,2,3,4,5]`, n=2
- **Expected Output**: `[4,5]`
- **Actual Output**: `[4,5]` ✅

- **Input**: `[1,2,3,4,5]`, n=5
- **Expected Output**: `[1,2,3,4,5]`
- **Actual Output**: `[1,2,3,4,5]` ✅

- **Input**: `[1,2,3,4,5]`, n=0
- **Expected Output**: `[]`
- **Actual Output**: `[]` ✅

- **Input**: `[7]`, n=1
- **Expected Output**: `[7]`
- **Actual Output**: `[7]` ✅

- **Input**: `[]`, n=0
- **Expected Output**: `[]`
- **Actual Output**: `[]` ✅

**Manual tweaks**: None.

## Bug 2 – bug2_fixed.js
- **Input**: `getCity(1)`
- **Expected Output**: `BAKU`
- **Actual Output**: `BAKU` ✅

- **Input**: `getCity(2)` (user without address)
- **Expected Output**: `UNKNOWN`
- **Actual Output**: `UNKNOWN` ✅

- **Input**: `getCity(3)`
- **Expected Output**: `GANJA`
- **Actual Output**: `GANJA` ✅

- **Input**: `getCity(4)` (user does not exist)
- **Expected Output**: `UNKNOWN`
- **Actual Output**: `UNKNOWN` ✅

**Manual tweaks**: Added the default value `"UNKNOWN"` (not part of the AI suggestion).

## Bug 3 – bug3_fixed.java
- **Input**: `add(10, 5)`
- **Expected Output**: `15`
- **Actual Output**: `15` ✅

- **Input**: `add(-1, 1)`
- **Expected Output**: `0`
- **Actual Output**: `0` ✅

- **Input**: `divide(10, 5)`
- **Expected Output**: `2.0`
- **Actual Output**: `2.0` ✅

- **Input**: `divide(7, 2)`
- **Expected Output**: `3.5`
- **Actual Output**: `3.5` ✅

- **Input**: `divide(1, 0)`
- **Expected Output**: `0.0` (prints "Cannot divide by zero")
- **Actual Output**: `0.0` (prints "Cannot divide by zero") ✅

**Manual tweaks**: Removed `public` from the class so the file name can differ from the class name.

## Bug 4 – bug4_fixed.py
- **Input**: `load_config('{"currency": "AZN", "tax": 0.18}')`, key `currency`
- **Expected Output**: `AZN`
- **Actual Output**: `AZN` ✅

- **Input**: same config, key `tax`
- **Expected Output**: `0.18`
- **Actual Output**: `0.18` ✅

- **Input**: `total_price(["10.5","20","5.25"])`
- **Expected Output**: `35.75`
- **Actual Output**: `35.75` ✅

- **Input**: `total_price([])`
- **Expected Output**: `0`
- **Actual Output**: `0` ✅

- **Input**: `is_adult("25")`
- **Expected Output**: `True`
- **Actual Output**: `True` ✅

- **Input**: `is_adult("10")`
- **Expected Output**: `False`
- **Actual Output**: `False` ✅

- **Input**: `parse_deadline("2026-11-09")`
- **Expected Output**: `2026-11-09 00:00:00`
- **Actual Output**: `2026-11-09 00:00:00` ✅

- **Input**: `parse_deadline("09/11/2026")`
- **Expected Output**: `ValueError` raised
- **Actual Output**: `ValueError` raised ✅

**Manual tweaks**: Refactored the script into functions so it can be tested without `input()`.

## Bug 5 – bug5_fixed.js
- **Input**: `getGrade(95)`
- **Expected Output**: `A`
- **Actual Output**: `A` ✅

- **Input**: `getGrade(90)`
- **Expected Output**: `A`
- **Actual Output**: `A` ✅

- **Input**: `getGrade(89)`
- **Expected Output**: `C`
- **Actual Output**: `C` ✅

- **Input**: `getGrade(72)`
- **Expected Output**: `C`
- **Actual Output**: `C` ✅

- **Input**: `getGrade(70)`
- **Expected Output**: `C`
- **Actual Output**: `C` ✅

- **Input**: `getGrade(69)`
- **Expected Output**: `E`
- **Actual Output**: `E` ✅

- **Input**: `getGrade(50)`
- **Expected Output**: `E`
- **Actual Output**: `E` ✅

- **Input**: `getGrade(49)`
- **Expected Output**: `F`
- **Actual Output**: `F` ✅

- **Input**: `getGrade(30)`
- **Expected Output**: `F`
- **Actual Output**: `F` ✅

- **Input**: `isPassing(50)`
- **Expected Output**: `true`
- **Actual Output**: `true` ✅

- **Input**: `isPassing(49)`
- **Expected Output**: `false`
- **Actual Output**: `false` ✅

- **Input**: `isPassing(95)`
- **Expected Output**: `true`
- **Actual Output**: `true` ✅

**Manual tweaks**: None.

## Bug 6 – bug6_fixed.py
- **Input**: `remove_negatives([3,-1,-2,5,-7,8])`
- **Expected Output**: `[3,5,8]`
- **Actual Output**: `[3,5,8]` ✅

- **Input**: `remove_negatives([])`
- **Expected Output**: `[]`
- **Actual Output**: `[]` ✅

- **Input**: `remove_negatives([-1,-2])`
- **Expected Output**: `[]`
- **Actual Output**: `[]` ✅

- **Input**: `remove_negatives([1,2])`
- **Expected Output**: `[1,2]`
- **Actual Output**: `[1,2]` ✅

- **Input**: `remove_negatives(d) is d` for `d = [4,-4]` (in place)
- **Expected Output**: `True`
- **Actual Output**: `True` ✅

- **Input**: printed output of `count_down(3)`
- **Expected Output**: `3\n2\n1\nLiftoff!\n`
- **Actual Output**: `3\n2\n1\nLiftoff!\n` ✅

- **Input**: printed output of `count_down(0)`
- **Expected Output**: `Liftoff!\n`
- **Actual Output**: `Liftoff!\n` ✅

**Manual tweaks**: None.
