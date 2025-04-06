def most_common_character(word):
    number0 = 1
    for character in word:
        number = word.count(character)
        if number >= number0:
            number0 = number
            cha = character
    return cha

if __name__ == "__main__":
    word = "abcdbde"
    print(most_common_character(word))    