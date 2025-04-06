# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents
    def __str__(self):
        if self._cents >= 10:
            return f"{self._euros}.{self._cents} eur"
        else:
            return f"{self._euros}.0{self._cents} eur"
    def __eq__(self, another):
        if self._euros == another._euros and self._cents == another._cents:
            return True
        else:
            return False
    def __not_eq__(self, another):
        if self._euros != another._euros or self._cents != another._cents:
            return True
        else:
            return False
    def __lt__(self, another):
        if self._euros < another._euros:
            return True
        elif self._euros == another._euros and self._cents < another._cents:
            return True
        else:
            return False
    def __gt__(self, another):
        if self._euros > another._euros:
            return True
        elif self._euros == another._euros and self._cents > another._cents:
            return True
        else:
            return False
    def __add__(self, another):
        new_add = Money(0, 0)
        new_add._euros = self._euros + another._euros
        new_add._cents = self._cents + another._cents
        if new_add._cents >= 100:
            new_add._cents -= 100
            new_add._euros += 1
        return new_add
    def	__sub__(self, another):
        if self < another:
            raise ValueError(f"a negative result is not allowed")
            print("ValueError: a negative result is not allowed")
        else:
            new_sub = Money(0, 0)
            new_sub._euros = self._euros - another._euros
            new_sub._cents = self._cents - another._cents
            if new_sub._cents < 0:
                new_sub._cents += 100
                new_sub._euros -= 1
            return new_sub

if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)
    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1