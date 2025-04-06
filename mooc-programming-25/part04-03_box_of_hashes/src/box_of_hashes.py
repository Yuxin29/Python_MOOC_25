def line(times, word):
    if word != "":
        word = word[0:1]
        print(word*times)
    else:
        print("*"*times)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    line(10, "#")
    num0 = 1
    while num0 < height:
        line(10, "#")
        num0 += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
