def average(numbers):
    total = 0
    for number in numbers:
        total += number

    return total / len(numbers)


def normalize_scores(scores):
    avg = average(scores)
    return [score / avg for score in scores]


if __name__ == "__main__":
    print(normalize_scores([10, 20, 30]))
