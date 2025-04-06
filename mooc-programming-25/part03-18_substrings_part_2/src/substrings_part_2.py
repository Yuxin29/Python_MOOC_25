word = input("Please type in a string: ")
num = len(word)
num0 = 1
while num0 <= num:
    print(word[(num-num0):num])
    num0 += 1