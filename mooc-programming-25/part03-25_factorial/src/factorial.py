num = int(input("Please type in a number: "))
num0 = 1
sum = 1
while num > 0:
    while num0 < num: 
        sum = sum * (num0 + 1)
        num0 += 1
    print(f"The factorial of the number {num} is {sum}")
    num = int(input("Please type in a number: "))
    num0 = 1
    sum = 1
else:
    print("Thanks and bye!")