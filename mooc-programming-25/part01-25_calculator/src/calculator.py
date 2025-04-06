num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
Ope = input("Operation: ")
if Ope == "add":
    print(f"{num1} + {num2} = {num1 + num2}")
elif Ope == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")
elif Ope == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")
else:
    print()