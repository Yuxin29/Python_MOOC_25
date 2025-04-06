#5 000 — 25 000	100	8
#25 000 — 55 000	1 700	10
#55 000 — 200 000	4 700	12
#200 000 — 1 000 000	22 100	15
#1 000 000 —	142 100	17
gift = int(input("Value of gift:"))
if gift <= 5000:
    print("No tax!")
elif gift <= 25000:
    print(f"Amount of tax: {100 + (gift - 5000) * 0.08} euros")
elif gift <= 55000:
    print(f"Amount of tax: {1700 + (gift - 25000) * 0.1} euros")
elif gift <= 200000:
    print(f"Amount of tax: {4700 + (gift - 55000) * 0.12} euros")
elif gift <= 1000000:
    print(f"Amount of tax: {22100 + (gift - 200000) * 0.15} euros")
else:
    print(f"Amount of tax: {142100 + (gift - 1000000) * 0.17} euros")