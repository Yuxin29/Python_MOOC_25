class ListHelper:
    def __init__(self):
        self.biggest_frequency = 0
        self.most_frequence = 0
        self.double_times = []
    def greatest_frequency(self, my_list: list):
        for i in my_list:
            if count.my_list(i) > self.biggest_frequency:
                self.biggest_frequency = count.my_list(i)
                self.most_frequence = i
        return self.biggest_frequency
    def doubles(self, my_list: list):
        for i in my_list:
            if count.my_list(i) > 1:
                self.double_times.append(i)
        return self.double_times

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))