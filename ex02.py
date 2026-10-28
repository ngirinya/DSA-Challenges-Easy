def find_smaller(numbers):
    if not numbers:
        return None

    smaller = numbers[0]

    for number in numbers:
        if number > smaller:
            smaller = number

    return smaller