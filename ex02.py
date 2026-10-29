def find_smaller(numbers):
    if not numbers:
        return None

    smaller = numbers[0]

    for number in numbers:
        if number < smaller:
            smaller = number

    return smaller

print(find_smaller([8, 3, 12, 1, 7]))
print(find_smaller([-3, -10, -1, -6]))    