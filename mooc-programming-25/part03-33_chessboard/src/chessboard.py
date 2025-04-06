def chessboard(num):
    if num % 2 == 0:
        num0 = 0
        while num0 + 1 < num:
            print("10"*(num // 2))
            print("01"*(num // 2))
            num0 = num0 + 2
    else:
        num0 = 0
        while num0 + 1 < num:
            print("10"*(num // 2) + "1")
            print("01"*(num // 2) + "0")
            num0 = num0 + 2
        print("10"*(num // 2) + "1")

# Testing the function
if __name__ == "__main__":
    chessboard(6)
