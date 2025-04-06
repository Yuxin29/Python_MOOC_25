def histogram(word):
    groups = {}
    for letter in word:
        if letter not in groups:
            groups[letter] = []
            groups[letter] = 0
        groups[letter] += 1
    for key, value in groups.items():
        print(f"{key} {'*' * value}")

if __name__ == "__main__":
    print(histogram("statistically"))