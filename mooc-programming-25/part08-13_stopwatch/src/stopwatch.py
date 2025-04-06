class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.minutes < 60:
            if self.seconds == 59 and self.minutes == 59:
                self.minutes = 0
                self.seconds = 0
            elif self.seconds < 59:
                self.seconds += 1
            else:
                self.seconds = 0
                self.minutes += 1

    def __str__(self):
        if self.minutes < 9:
            if self.seconds < 9:
                return f"0{self.minutes}:0{self.seconds}"
            else:
                return f"0{self.minutes}:{self.seconds}"
        else:
            if self.seconds < 9:
                return f"{self.minutes}:0{self.seconds}"
            else:
                return f"{self.minutes}:{self.seconds}"

if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3602):
        print(watch)
        watch.tick()