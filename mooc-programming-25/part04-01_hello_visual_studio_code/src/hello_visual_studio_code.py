choice = input("Editor: ")
choice = choice.lower()
while choice != "visual studio code":
    if choice == "word" or choice == "notepad":
        print("awful")
        choice = input("Editor: ")
        choice = choice.lower()
    else:
        print("not good")
        choice = input("Editor: ")
        choice = choice.lower()
else:
    print("an excellent choice!")