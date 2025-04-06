list = []
item = int(input("New item: "))
while item != 0:
    list.append(item)
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")
    item = int(input("New item: "))
else:
    print("Bye!")