year0 = int(input("Year: "))
if year0 % 4 == 0 and year0 % 400 == 0:
    year1 = year0 + 4
    print(f"The next leap year after {year0} is {year1}")
elif year0 % 4 == 0 and (year0 + 4) % 400 == 0:
    year1 = year0 + 4
    print(f"The next leap year after {year0} is {year1}")
elif year0 % 4 == 0 and (year0 + 4) % 100 == 0 and (year0 + 4) % 400 != 0:
    year1 = year0 + 8
    print(f"The next leap year after {year0} is {year1}")
elif year0 % 4 == 0 and year0 % 100 == 0:
    year1 = year0 + 4
    print(f"The next leap year after {year0} is {year1}")
elif year0 % 4 == 0 and year0 % 100 != 0:
    year1 = year0 + 4
    print(f"The next leap year after {year0} is {year1}")
else:
    year2 = year0
    while year2 % 4 != 0 or year2 % 100 == 0 and year2 % 400 != 0:
        year2 = year2 + 1
    print(f"The next leap year after {year0} is {year2}")