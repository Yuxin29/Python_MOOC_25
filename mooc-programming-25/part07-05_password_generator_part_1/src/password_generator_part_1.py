from random import choice
def generate_password(length: int):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i = 1
    password = ""
    while i <= length:
        letter = choice(letters)
        password += letter
        i += 1
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))