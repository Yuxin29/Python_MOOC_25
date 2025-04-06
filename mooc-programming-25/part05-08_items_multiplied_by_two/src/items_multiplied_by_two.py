def double_items(numbers: list):
    numbers_2 = []
    for i in numbers:
        numbers_2.append(i * 2)
    return numbers_2

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)