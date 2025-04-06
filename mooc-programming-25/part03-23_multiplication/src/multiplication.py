num = int(input("Please type in a number:"))
s1 = 1
s2 = 0
while s1 < num:
    while s2 < num:
        s2 += 1 
        print(f"{s1} x {s2} = {s1 * s2}")
    else:
        s2 = 0
    s1 += 1
    while s2 < num:
        s2 += 1 
        print(f"{s1} x {s2} = {s1 * s2}")
    else:
        s2 += 0