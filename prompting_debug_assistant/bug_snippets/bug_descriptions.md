# Bug Descriptions

## Bug 1 - bug1.py

**Intended Behavior:** Return the last `n` items from a list.

**Issue Type:** Off-by-one error.

**Notes:** The loop stops at `len(items) - 1`, so the final item is never included in the result.

---

## Bug 2 - bug2.py

**Intended Behavior:** Calculate and return the average of a list of numbers.

**Issue Type:** Runtime exception.

**Notes:** When an empty list is passed, `len(numbers)` is `0`, causing a `ZeroDivisionError`.

---

## Bug 3 - bug3.py

**Intended Behavior:** Identify and print even numbers from a list.

**Issue Type:** Logical error.

**Notes:** The function checks whether `number % 2 == 1`, which identifies odd numbers instead of even numbers.

---

## Bug 4 - bug4.js

**Intended Behavior:** Calculate the total cost by multiplying the price by the quantity.

**Issue Type:** Logical error.

**Notes:** The function uses addition instead of multiplication, so the calculated total is incorrect.

---

## Bug 5 - bug5.c

**Intended Behavior:** Print every element of the `numbers` array exactly once.

**Issue Type:** Off-by-one / out-of-bounds error.

**Notes:** The loop uses `i <= 5`, but valid array indexes are only `0` through `4`. Accessing `numbers[5]` goes outside the array bounds.
