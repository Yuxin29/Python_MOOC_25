def same_chars(word, n1, n2):
    if n1 >= len(word) or n2 >= len(word):
        return False
    a = word[n1] == word[n2]
    return a

if __name__ == "__main__":
    print(same_chars("aaaa", 1, 2))