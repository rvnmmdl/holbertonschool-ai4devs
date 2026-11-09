import io
from contextlib import redirect_stdout

def remove_negatives(numbers):
    for n in numbers[:]:
        if n < 0:
            numbers.remove(n)
    return numbers


def count_down(start):
    i = start
    while i > 0:
        print(i)
        i -= 1
    print("Liftoff!")


def check(label, expected, actual):
    status = "PASS" if expected == actual else "FAIL"
    print(f"{label} | expected={expected!r} | actual={actual!r} | {status}")
    assert expected == actual


def output_of(start):
    buf = io.StringIO()
    with redirect_stdout(buf):
        count_down(start)
    return buf.getvalue()


if __name__ == "__main__":
    check("remove_negatives mixed", [3, 5, 8], remove_negatives([3, -1, -2, 5, -7, 8]))
    check("remove_negatives empty", [], remove_negatives([]))
    check("remove_negatives all negative", [], remove_negatives([-1, -2]))
    check("remove_negatives none negative", [1, 2], remove_negatives([1, 2]))
    check("remove_negatives is in place", True, remove_negatives(d := [4, -4]) is d)
    check("count_down(3)", "3\n2\n1\nLiftoff!\n", output_of(3))
    check("count_down(0)", "Liftoff!\n", output_of(0))
