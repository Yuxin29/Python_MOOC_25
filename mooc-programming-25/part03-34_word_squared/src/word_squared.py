def squared(word, times):
    if len(word) >= times:
        num0 = 0
        word = word*times
        while num0 < times:
            print(word[0:times])
            word = word[times:]
            num0 = num0 + 1
    else:
        num0 = 0
        word = word* (len(word) * times * times)
        while num0 < times:
            print(word[0:times])
            word = word[times:]
            num0 = num0 + 1
if __name__ == "__main__":
    squared("asgd",22)