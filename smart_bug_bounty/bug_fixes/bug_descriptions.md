# Bug Descriptions

## bug1.py
- **Intended Behavior**: Calculate the average of a list and normalize each score by that average.
- **Current Issue**: The average calculation subtracts `1` from the correct result, producing incorrect normalized scores.

## bug2.js
- **Intended Behavior**: Find a user by ID and return the user's name.
- **Current Issue**: The loop uses `<=` instead of `<`, which can access an element beyond the end of the array. The caller also assumes a user was found and dereferences `null`.

## bug3.java
- **Intended Behavior**: Return a list containing each integer only once while preserving its original order.
- **Current Issue**: The method removes elements from `values` while iterating over the same list. This changes the indexes during iteration and causes elements to be skipped.

## bug4.py
- **Intended Behavior**: Count how many times each word occurs and return the most common word.
- **Current Issue**: A first occurrence is initialized to `0` instead of `1`, so every word's count is one lower than it should be. The result can also be misleading for single-occurrence words.

## bug5.js
- **Intended Behavior**: Fetch JSON data, reject on timeout, and propagate network or parsing errors to the caller.
- **Current Issue**: The `catch` handler logs the error but never calls `reject`, leaving the returned Promise pending when the fetch fails.

## bug6.sql
- **Intended Behavior**: Return paid orders grouped by customer whose total paid amount is greater than 60.
- **Current Issue**: The query uses the `total_spent` SELECT alias in `HAVING`. This is not portable SQL and fails on database systems that do not allow SELECT aliases in `HAVING`; the aggregate expression should be used directly.
