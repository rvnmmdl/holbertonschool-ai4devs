def last_n_items(items, n):
    """Return the last n items of a list."""
    result = []
    for i in range(len(items) - n, len(items)):
        result.append(items[i])
    return result


def check(items, n, expected):
    actual = last_n_items(items, n)
    status = "PASS" if actual == expected else "FAIL"
    print(f"input={items}, n={n} | expected={expected} | actual={actual} | {status}")
    assert actual == expected


if __name__ == "__main__":
    check([1, 2, 3, 4, 5], 3, [3, 4, 5])
    check([1, 2, 3, 4, 5], 2, [4, 5])
    check([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5])
    check([1, 2, 3, 4, 5], 0, [])
    check([7], 1, [7])
    check([], 0, [])
    print("All tests passed")
