point = int(input("How many points [0-100]:"))
if point < 0 or point > 100:
    print("Grade: impossible!")
elif point >= 0 and point <= 49:
    print("Grade: fail")
elif point >= 50 and point <= 59:
    print("Grade: 1")
elif point >= 60 and point <= 69:
    print("Grade: 2")
elif point >= 70 and point <= 79:
    print("Grade: 3")
elif point >= 80 and point <= 89:
    print("Grade: 4")
else:
    print("Grade: 5")