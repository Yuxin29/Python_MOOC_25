from fractions import Fraction

def fractionate(amount: int):
    i = 0
    list = []
    part = Fraction(1, amount)
    while i < amount:
        i += 1
        list.append(part)
    return(list)

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)
    print()
    print(fractionate(4))