from math import sqrt, log
def hypotenuse(leg1: float, leg2: float):
    sum = leg1 * leg1 + leg2 * leg2
    side = float(sqrt(sum))
    return(side)


if __name__ == "__name__":
    print(hypotenuse(3,4))