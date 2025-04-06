word = input("Please type in a string: ")
num = len(word)
if word[num - 2] != word[1]:
    print("The second and the second to last characters are different")
else:
    print(f"The second and the second to last characters are {word[1]}")