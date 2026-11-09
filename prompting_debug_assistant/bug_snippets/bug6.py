def remove_negatives(numbers):
    """Remove all negative numbers from the list and return it."""
    for n in numbers:
        if n < 0:
            numbers.remove(n)
    return numbers


def count_down(start):
    """Print numbers from start down to 1."""
    i = start
    while i > 0:
        print(i)
    print("Liftoff!")


data = [3, -1, -2, 5, -7, 8]
print(remove_negatives(data))   # expected: [3, 5, 8]
count_down(3)
