class Person:
    def __init__(self, name: str):
        self.name = name 
    def return_first_name(self):
        names = self.name.split()
        first_name = names[0]
        return first_name
    def return_last_name(self):
        names = self.name.split()
        last_name = names[1]
        return last_name
        

if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())
    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())











