num = int(input("Please type in a number:"))
n1 = 1
if num % 2 == 0:
    while n1 <= (num / 2):
        print(f"{n1}")
        print(f"{num - n1 + 1}")
        n1 += 1
else:
    while n1 < (num / 2):
        print(f"{n1}")
        print(f"{num - n1 + 1}")
        n1 += 1
    print(f"{num - n1 + 1}")