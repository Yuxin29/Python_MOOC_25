name = input("Please tell me your name:")
if name == "Jerry":
    print("Next please!")
else:
    port = int(input("How many portions of soup?"))
    print(f"The total cost is {port * 5.90}")
    print("Next please!")