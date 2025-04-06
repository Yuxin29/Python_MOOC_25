def line(times, word):
    if word != "":
        word = word[0:1]
        print(word*times)
    else:
        print("*"*times)

def square(times, word):
    # You should call function line here with proper parameters
    line(times, word)
    num0 = 1
    while num0 < times:
        line(times, word)
        num0 += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")