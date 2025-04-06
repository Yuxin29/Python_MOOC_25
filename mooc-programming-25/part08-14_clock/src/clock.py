class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def tick(self):
        if self.hours == 23:
            if self.minutes == 59:
                if self.seconds == 59:
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0
                else:
                    self.seconds += 1
            else:
                if self.seconds == 59:
                    self.seconds = 0
                    self.minutes += 1
                else:
                    self.seconds += 1
        else:
            if self.minutes == 59:
                if self.seconds == 59:
                    self.seconds = 0
                    self.minutes = 0
                    self.hours += 1
                else:
                    self.seconds += 1
            else:
                if self.seconds == 59:
                    self.seconds = 0
                    self.minutes += 1
                else:
                    self.seconds += 1

    def set(self, new_hours: int, new_minutes: int):
        self.seconds = 0
        self.minutes = new_minutes
        self.hours = new_hours

    def __str__(self):
        if self.hours < 9:
            if self.minutes < 9:
                if self.seconds < 9:
                    return f"0{self.hours}:0{self.minutes}:0{self.seconds}"
                else:
                    return f"0{self.hours}:0{self.minutes}:{self.seconds}"
            else:
                if self.seconds < 9:
                    return f"0{self.hours}:{self.minutes}:0{self.seconds}"
                else:
                    return f"0{self.hours}:{self.minutes}:{self.seconds}"
        else:
            if self.minutes < 9:
                if self.seconds < 9:
                    return f"{self.hours}:0{self.minutes}:0{self.seconds}"
                else:
                    return f"{self.hours}:0{self.minutes}:{self.seconds}"
            else:
                if self.seconds < 9:
                    return f"{self.hours}:{self.minutes}:0{self.seconds}"
                else:
                    return f"{self.hours}:{self.minutes}:{self.seconds}"

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.set(12, 5)
    print(clock)