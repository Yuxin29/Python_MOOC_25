# Write your solution here
# You can test your function by calling it within the following block
def line(times, word):
    if word != "":
        word = word[0:1]
        print(word*times)
    else:
        print("*"*times)