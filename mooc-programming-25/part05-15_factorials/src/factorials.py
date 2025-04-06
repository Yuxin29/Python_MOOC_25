def factorials(n: int):
    fac = {}
    num0 = 1
    while num0 <= n:
        num = 1
        fac[num0] = 1
        while num <= num0:
            fac[num0] = fac[num0] * num
            num += 1
        num0 += 1
    return fac

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])