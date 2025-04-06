class LotteryNumbers:
    def __init__(self, week: int, week_numbers: list):
        self.week = week
        self.week_numbers = week_numbers

    def number_of_hits(self, my_numbers: list):
        return len([number for number in my_numbers if number in self.week_numbers])

    def hits_in_place(self, numbers):
        return [number if number in self.week_numbers else -1 for number in numbers]
        
if __name__ == "__main__ ":
    week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
    my_numbers = [1,4,7,11,13,19,24]

    print(week5.number_of_hits(my_numbers))