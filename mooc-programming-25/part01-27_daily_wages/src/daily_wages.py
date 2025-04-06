wage1 = float(input("Hourly wage1: "))
#wage2 = float(input("Hourly wage2: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")
if day == "Sunday":
    print(f"Daily wages: {hours * wage1 * 2} euros")
else:
    print(f"Daily wages: {hours * wage1} euros")