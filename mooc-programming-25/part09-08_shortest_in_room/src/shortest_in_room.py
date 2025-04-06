class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
    def __str__(self):
        return self.name
    
class Room:
    def __init__(self):
        self.all = []
        self.numbers = len(self.all)
        self.combined_height = 0
        for item in self.all:
            self.combined_height += self.person.height
        self.short = 300
        self.short_one = Person("One", 0)
    def add(self, person: Person):
        self.all.append(person)
        self.numbers += 1
        self.combined_height += person.height
    def is_empty(self):
        if len(self.all) == 0:
            return True
        else:
            return False
    def print_contents(self):
        print(f"There are {self.numbers} persons in the room, and their combined height is {self.combined_height} cm")
        for person in self.all:
            print(f"{person.name}({person.height} cm)")
    def shortest(self):
        if self.numbers == 0:
            return None
        else:
            for person in self.all:
                if person.height < self.short:
                    self.short = person.height
                    self.short_one = person
            return self.short_one
    def remove_shortest(self):
        if self.numbers == 0:
            return None
        else:
            self.shortest_person = self.shortest()
            shortest_person = self.shortest()
            self.shortest_person = self.shortest()
            self.all.remove(self.shortest_person)
            self.numbers -= 1
            self.combined_height -= self.shortest_person.height
            return shortest_person

if __name__ == "__main__":
    room = Room()
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()
    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")
    print()

    room.print_contents()