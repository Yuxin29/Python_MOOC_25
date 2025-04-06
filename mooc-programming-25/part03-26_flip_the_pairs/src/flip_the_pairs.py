num = int(input("Please type in a number:"))
n1 = 1
n2 = 2
if num % 2 == 0:
    while n2 <= num:
        print(f"{n2}")
        print(f"{n1}")
        n1 += 2
        n2 += 2
else:
    while n1 < num:
        print(f"{n2}")
        print(f"{n1}")
        n1 += 2
        n2 += 2
    print(f"{num}")