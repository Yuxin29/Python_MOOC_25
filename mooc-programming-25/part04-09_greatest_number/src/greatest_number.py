def greatest_number(x, y, z):
    if x >= y >= z or x > z >= y:
        return x
    elif y >= x >= z or y >= z >= x:
        return y
    else:
        return z

if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)