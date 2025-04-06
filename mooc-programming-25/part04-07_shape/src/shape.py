def line(times, word):
    if word != "":
        word = word[0:1]
        print(word*times)
    else:
        print("*"*times)

def shape(times, word, lines, word2):
    num1 = 1
    while num1 <= times:
        line(num1, word)
        num1 += 1
    num2 = 1
    while num2 <= lines:
        line(times, word2)
        num2 += 1

if __name__ == "__main__":
    shape(5, "x", 2, "o")