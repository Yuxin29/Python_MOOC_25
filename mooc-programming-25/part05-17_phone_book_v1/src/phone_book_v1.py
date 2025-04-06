phone_book = {}
com = input("command (1 search, 2 add, 3 quit): ")
while com != "3":
    if com == "1":
        name = input("name: ")
        if name not in phone_book:
            print("no number")
        else:
            print(phone_book[name])
        com = input("command (1 search, 2 add, 3 quit): ")
    elif com == "2":
        name = input("name: ")
        number = input("number: ")
        phone_book[name] = number
        print("ok!")
        com = input("command (1 search, 2 add, 3 quit): ")
else:
    print("quitting...")