def remove_smallest(numbers: list):
    mini = min(numbers)
    numbers = numbers.remove(mini)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)