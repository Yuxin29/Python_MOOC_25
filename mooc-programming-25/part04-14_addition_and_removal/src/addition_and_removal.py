my_list = []
print(f"The list is now []")
choice = input("a(d)d, (r)emove or e(x)it: ")
n0 = 1
while choice == "d":
    my_list.append(n0)
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")
    n0 += 1
    while choice == "r":
        my_list.pop((n0 - 2))
        print(f"The list is now {my_list}")
        choice = input("a(d)d, (r)emove or e(x)it: ")
        n0 -= 1
else:
    print("Bye!")