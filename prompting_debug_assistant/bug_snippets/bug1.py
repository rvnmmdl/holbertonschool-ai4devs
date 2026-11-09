def get_last_items(items, n):
    start = len(items) - n
    result = []

    for i in range(start, len(items) - 1):
        result.append(items[i])

    return result


numbers = [10, 20, 30, 40, 50]
print(get_last_items(numbers, 3))
