# (xx°F − 32) × 5/9 = 12,778°C
fah = int(input("Please type in a temperature (F):"))
cel = (fah - 32) * 5 / 9
if cel >= 0:
    print(f"{fah} degrees Fahrenheit equals {cel} degrees Celsius")
else:
    print(f"{fah} degrees Fahrenheit equals {cel} degrees Celsius")
    print("Brr! It's cold in here!")