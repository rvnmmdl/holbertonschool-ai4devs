def is_even(number):
    if number % 2 == 1:
        return True
    else:
        return False


numbers = [2, 4, 6, 7, 9]

for number in numbers:
    if is_even(number):
        print(number, "is even")
