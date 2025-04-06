from math import sqrt
#Please write a program which asks the user for integer numbers.
#f the number is below zero, the program should print out the message "Invalid number".
#If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
#In either case, the program should then ask for another number.
#If the user inputs the number zero, the program should stop asking for numbers and exit the loop.
num = int(input("Please type in a number:"))
while num != 0:
    if num < 0:
        print("Invalid number")
        num = int(input("Please type in a number:"))
    else :
        print(sqrt(num))
        num = int(input("Please type in a number:"))
print("Exiting...") 