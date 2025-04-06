times = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch? "))
gro = float(input("How much money do you spend on groceries in a week? "))
sum = times * price + gro
print()
print("Average food expenditure:")
print(f"Daily: {sum / 7} euros")
print(f"Weekly: {sum} euros")