class PhoneBook:
    def __init__(self):
        self.__persons = {}
    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = []
        self.__persons[name].append(number)
    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]
    def get_names(self, numbers: str):
        for name, number in self.__persons.items():
            if number == numbers:
                return name
    def all_entries(self):
        return self.__persons

class FileHandler():
    def __init__(self, filename):
        self.__filename = filename
    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts
                names[name] = numbers
        return names
    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")
                
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 search by number")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("number unknown")
            return
        for number in numbers:
            print(number)
    
    def search_names(self):
        numbers = input("number: ")
        names = self.__phonebook.get_names(numbers)
        if names == None:
            print("number unknown")
            return
        print(name)
        #for name in names:
            #print(name)
    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.search_names()
            else:
                self.help()

# when you run the tests, nothing apart from these two lines should be placed in the main function, outside any class definitions 
application = PhoneBookApplication()
application.execute()