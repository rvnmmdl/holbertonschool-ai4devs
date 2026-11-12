def count_words(text):
    counts = {}

    for word in text.lower().split(" "):
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 0

    return counts


def most_common_word(text):
    counts = count_words(text)
    return max(counts, key=counts.get)


text = "python python code"
print(count_words(text))
print(most_common_word(text))
