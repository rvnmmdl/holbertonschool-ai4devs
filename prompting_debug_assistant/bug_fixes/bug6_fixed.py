import io
from contextlib import redirect_stdout


def remove_negatives(numbers):
    """Remove all negative numbers from the list and return it."""
    for n in numbers[:]:
        if n < 0:
            numbers.remove(n)
    return numbers


def count_down(start):
    """Print numbers from start down to 1."""
    i = start
    while i > 0:
        print(i)
        i -= 1
    print("Liftoff!")


def check(label, expected, actual):
    status = "PASS" if expected == actual else "FAIL"
    print(f"{label} | expected={expected!r} | actual={actual!r} | {status}")
    assert expected == actual


def captured_count_down(start):
    buf = io.StringIO()
    with redirect_stdout(buf):
        count_down(start)
    return buf.getvalue()


if __name__ == "__main__":
    check("remove_negatives([3,-1,-2,5,-7,8])", [3, 5, 8], remove_negatives([3, -1, -2, 5, -7, 8]))
    check("remove_negatives([])", [], remove_negatives([]))
    check("remove_negatives([-1,-2])", [], remove_negatives([-1, -2]))
    check("remove_negatives([1,2])", [1, 2], remove_negatives([1, 2]))
    data = [4, -4]
    check("remove_negatives is in place", True, remove_negatives(data) is data)
    check("count_down(3)", "3\n2\n1\nLiftoff!\n", captured_count_down(3))
    check("count_down(0)", "Liftoff!\n", captured_count_down(0))
    print("All tests passed")
