class Item:
    def __init__(self, name: str, kg: int):
        self.__name = name
        self.__kg = kg
    def name(self):
        return self.__name
    def weight(self):
        return self.__kg
    def __str__(self) -> str:
        return f"{self.__name} ({self.__kg} kg)"

class Suitcase:
    def __init__(self, max: int):
        self.max_weight = max
        self.things = []
        self.num = 0
        self.total = 0
    def add_item(self, thing: Item):
        if self.total + thing.weight() <= self.max_weight:
            self.things.append(thing)
            self.num += 1
            self.total += thing.weight()
            self.heaviest_wei = 0
            self.heaviest = Item
        else:
            pass
    def __str__(self):
        if self.num > 1 or self.num == 0:
            return f"{self.num} items ({self.total} kg)"
        else:
            return f"{self.num} item ({self.total} kg)"
    def print_items(self):
        for thing in self.things:
            print(f"{thing.name()} ({thing.weight()} kg)")
    def weight(self):
        return self.total
    def heaviest_item(self):
        if self.num == 0:
            return None
        else:
            for thing in self.things:
                if thing.weight() > self.heaviest_wei:
                    self.heaviest_wei = thing.weight()
                    self.heaviest = thing
            return self.heaviest

class CargoHold:
    def __init__(self, cargo_max: int):
        self.cargo_max = cargo_max
        self.hold = []
        self.case_num = 0
        self.total_wei_left = cargo_max
    def add_suitcase(self, case: Suitcase):
        if self.total_wei_left >= case.weight():
            self.hold.append(case)
            self.case_num += 1
            self.total_wei_left -= case.weight() 
        else:
            pass
    def __str__(self):
        if self.case_num > 1 or self.case_num == 0:
            return f"{self.case_num} suitcases, space for {self.total_wei_left} kg"
        else:
            return f"{self.case_num} suitcase, space for {self.total_wei_left} kg"
    def print_items(self):
        for case in self.hold:
            for thing in case.things:
                print(f"{thing.name()} ({thing.weight()} kg)")
if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()