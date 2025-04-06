word = input("Please type in a string: ")
word[0] != ""
num = len(word)
while num != 0:
    print(word)
    print("-"*num)
    print("")
    word = input("Please type in a string: ")
    num = len(word)