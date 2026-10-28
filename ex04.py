def count_even(numbers):
    if not numbers:
        return 0

    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 6]))                