num = int(input("PIN: "))
time = 1
if num == 4321:
    print("Correct! It only took you one single attempt!")
else:
    print("Wrong")
    num = int(input("PIN: "))
    time = time + 1
    while num != 4321:
        print("Wrong")
        time = time + 1
        num = int(input("PIN: "))
    print(f"Correct! It took you {time} attempts")