def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers) - 1


def normalize_scores(scores):
    avg = average(scores)
    return [score / avg for score in scores]


scores = [10, 20, 30]
print(normalize_scores(scores))
