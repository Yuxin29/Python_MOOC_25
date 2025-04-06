lett1 = input("1st letter: ")
lett2 = input("2nd letter: ")
lett3 = input("3rd letter: ")
if lett1 > lett2:
    if lett2 > lett3:
        print(f"The letter in the middle is {lett2}")
    else:
        if lett3 > lett1:
            print(f"The letter in the middle is {lett1}")
        else:
            print(f"The letter in the middle is {lett3}")
else:  
    if lett2 < lett3:
        print(f"The letter in the middle is {lett2}")
    else:    
        if lett1 > lett3:
            print(f"The letter in the middle is {lett1}")
        else:
            print(f"The letter in the middle is {lett3}")
