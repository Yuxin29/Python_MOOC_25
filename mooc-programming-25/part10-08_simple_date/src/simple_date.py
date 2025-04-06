class SimpleDate:
    def __init__(self, date: int, month: int, year: int):
        self.date = date
        self.month = month
        self.year = year
    def __str__(self):
        return f"{self.date}.{self.month}.{self.year}"
    def __eq__(self, another):
        if self.date == another.date and self.month == another.month and self.year == another.year:
            return True
        else:
            return False
    def __not_eq__(self, another):
        if self.date != another.date or self.month != another.month or self.year != another.year:
            return True
        else:
            return False
    def __lt__(self, another):
        if self.year < another.year:
            return True
        elif self.year == another.year and self.month < another.month:
            return True
        elif self.year == another.year and self.month == another.month and self.date < another.date:
            return True
        else:
            return False
    def __gt__(self, another):
        if self.year > another.year:
            return True
        elif self.year == another.year and self.month > another.month:
            return True
        elif self.year == another.year and self.month == another.month and self.date > another.date:
            return True
        else:
            return False
    def __add__(self, day):
        new_add = SimpleDate({self.date}, self.month, self.year)
        if day + self.date <= 30:
            new_add.date = self.date + day
        elif 30 < self.month * 30 + day + self.date <= 360:
            month_plus = (day + self.date) // 30
            day_plus = (day + self.date) % 30
            new_add.date = day_plus
            new_add.month = self.month + month_plus
        else:
            year_plus = (self.month * 30 + day + self.date) // 360
            month_plus = (day + self.date) // 30
            day_plus = (day + self.date) % 30
            new_add.date = day_plus
            if self.month + month_plus < 13:
                new_add.month = self.month + month_plus
                new_add.year = self.year + year_plus
            else:
                new_add.month = self.month + month_plus - 12 * year_plus
                new_add.year = self.year + year_plus
        return new_add
    def __sub__(self, day):
        differ = 0
        if self.year == day.year:
            if self.month ==day.month:
                differ = day.date - self.date
                if differ < 0:
                    differ = - differ
            else:
                differ = (day.month - self.month) * 30 + (day.date - self.date)
                if differ < 0:
                    differ = - differ
        else: 
            differ = (day.year - self.year) * 360 + (day.month - self.month) * 30 + (day.date - self.date)
            if differ < 0:
                    differ = - differ
        return differ

        
if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)