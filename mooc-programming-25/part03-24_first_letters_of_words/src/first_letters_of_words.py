sen = input("Please type in a sentence: ")
space = " "
index = sen.find(space)
num = len(sen)
letter = sen[0:1]
while index >= 0:
    print(letter)
    sen = sen[(index + 1):num]
    index = sen.find(space)
    num = len(sen)
    letter = sen[0:1]
print(letter)