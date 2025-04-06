print("1 - add an entry, 2 - read entries, 0 - quit")
choice = int(input("Function: "))
while choice != 0:
    if choice == 1:
        with open("diary.txt", "a") as my_file:
            entry = input("Diary entry: ")
            my_file.write(f"{entry}\n")
            print("Diary saved")
            choice = int(input("Function: "))
    else:
        with open("diary.txt") as new_file:
            print("Entries:")
            contents = new_file.read()
            print(contents)
            choice = int(input("Function: "))
else:
    print("Bye now!")
    