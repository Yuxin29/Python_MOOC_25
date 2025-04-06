word = input("Word: ")
num = len(word)
if num % 2 == 0:
    space = (28 - num) // 2
    print("*"*30)
    print("*" + " "*space + word + " "*space + "*")
    print("*"*30)
else:
    space1 = (28 - num) // 2
    space2 = space1 + 1
    print("*"*30)
    print("*" + " "*space1 + word + " "*space2 + "*")
    print("*"*30)