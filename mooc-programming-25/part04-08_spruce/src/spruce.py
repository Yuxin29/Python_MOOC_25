def spruce(num):
    print("a spruce!")
    num0 = 1
    n = 1
    total = (2 * (num - 1) + 1)
    while n < num:
        empty = ((total - num0) // 2 - 1)
        print(" " * empty, "*" * num0, " " * empty)
        num0 = 2 * n + 1
        n += 1
    print("*" * ((2 * num) - 1))
    print(" " * ((total - 1) // 2 - 1),  "*")

if __name__ == "__main__":
    spruce(5)