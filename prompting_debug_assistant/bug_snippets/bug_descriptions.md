# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return the last `n` items of a list.
**Issue Type**: Off-by-one error.
**Notes**: The loop starts at `len(items) - n - 1`, so it returns `n + 1` items. When `n == len(items)`, the start index becomes `-1`, which silently wraps to the last element instead of raising an error. The start index should be `len(items) - n`.

## Bug 2 – bug2.js
**Intended Behavior**: Return the upper-cased city of the user with the given id.
**Issue Type**: Runtime exception (`TypeError`).
**Notes**: User 2 has no `address`, so `user.address.city` throws `Cannot read properties of undefined`. User 4 does not exist, so `find()` returns `undefined` and the same error occurs. Needs null checks or optional chaining (`user?.address?.city`).

## Bug 3 – bug3.java
**Intended Behavior**: A small calculator with `add` and `divide` methods that prints the results.
**Issue Type**: Syntax errors.
**Notes**: Several compile-time errors: missing semicolon after `return a + b`, missing `)` in `if (b == 0`, missing `)` in the `println` call for the quotient, a single-quoted `'Done'` used as a `String` (Java requires double quotes), and a missing closing `}` for the class.

## Bug 4 – bug4.py
**Intended Behavior**: Load a config, sum a list of prices, check whether the user is an adult, and parse a date.
**Issue Type**: Misuse of data types or libraries.
**Notes**: Four problems: `json.loads()` is given a `dict` instead of a JSON string (`TypeError`); `total_price` adds strings to an integer (`TypeError`) because prices are not converted with `float()`; `input()` returns a `str`, so `age > 18` fails (needs `int(age)`); `strptime` uses the format `%d/%m/%Y` for a string written as `YYYY-MM-DD` (`ValueError`, should be `%Y-%m-%d`).

## Bug 5 – bug5.js
**Intended Behavior**: Convert a score to a letter grade (90+ = A, 70+ = C, 50+ = E, else F) and tell whether a score is passing (50 or more).
**Issue Type**: Logical error.
**Notes**: Conditions are ordered from lowest to highest, so any score of 50 or more returns "E" and the "C" and "A" branches are never reached. `isPassing` uses `>` instead of `>=`, so a score of exactly 50 is reported as failing.

## Bug 6 – bug6.py
**Intended Behavior**: Remove all negative numbers from a list, and count down from a start value to 1.
**Issue Type**: Loop logic issues (modifying a list while iterating, infinite loop).
**Notes**: `remove_negatives` removes items from the list while iterating over it, which skips elements (`-2` stays in the result). `count_down` never decrements `i`, so the `while` loop runs forever and "Liftoff!" is never printed.
