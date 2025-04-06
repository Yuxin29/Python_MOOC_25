n0 = 0
list = []
word = input("Word: ")
while word not in list:
    list.append(word)
    n0 += 1
    word = input("Word: ")
else:
    print(f"You typed in {n0} different words")