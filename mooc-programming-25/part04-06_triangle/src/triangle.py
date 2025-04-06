def line(times, word):
    if word != "":
        word = word[0:1]
        print(word*times)
    else:
        print("*"*times)

def triangle(size):
    num0 = 1
    while num0 <= size:
        line(num0, "#")
        num0 += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
