def even_numbers(beginning: int, maximum: int):
    if beginning % 2 == 0:
        first = beginning
    else:
        first = beginning + 1
    while first <= maximum:
        yield first
        first += 2

if __name__ == "__main__":
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)