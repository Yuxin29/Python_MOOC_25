import random

def word_generator(characters: str, length: int, amount: int):
    new_word = random.choice(characters)
    yield new_word
    for i in range(amount):
        print(next(new_word))

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)