class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.sum = 0

    def add_number(self, number:int):
        self.number = number
        self.count += 1
        self.sum += self.number

    def count_numbers(self):
        return self.count
    
    def get_sum(self):
        return self.sum
    
    def average(self):
        if self.count != 0:
            ave = self.sum / self.count
            return ave
        else:
            return
    
stats_all = NumberStats()
stats_2 = NumberStats()
stats_1 = NumberStats()
num = int(input("Please type in integer numbers: "))
while num != -1:
    if (num % 2) == 0:
        stats_all.add_number(num)
        stats_2.add_number(num)
        num = int(input("Please type in integer numbers: "))
    else:
        stats_all.add_number(num)
        stats_1.add_number(num)
        num = int(input("Please type in integer numbers: "))

print("Sum of numbers:", stats_all.get_sum())
print("Mean of numbers:", stats_all.average())
print("Sum of even numbers:", stats_2.get_sum())
print("Sum of odd numbers:", stats_1.get_sum())