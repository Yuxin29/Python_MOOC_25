import datetime

def is_it_valid(pic: str):
    date = int(pic[0:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    identifier = (pic[7:10])
    string_controller = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    dbirth = pic[0:2] + pic[2:4] + pic[4:6]
    summ = dbirth + identifier
    number = (int(summ)) % 31
    controller = string_controller[number]
    length = len(pic)
    if month <= 12:
        j1 = (pic[10] == controller)
        j2 = (length == 11)
        if pic[6] == "+":
            year = int("18" + pic[4:6])
            date_start = datetime.datetime(1800, 1, 1)
            date_end = datetime.datetime(1899, 12, 31)
            correctDate = None
            try:
                newDate = datetime.datetime(year=year, month=month, day=date)
                correctDate = True
            except ValueError:
                correctDate = False
            if correctDate == True:
                j3 = (date_start <= newDate <= date_end)
            else:
                j3 = False
        elif pic[6] == "-":
            year = int("19" + pic[4:6])
            date_start = datetime.datetime(1900, 1, 1)
            date_end = datetime.datetime(1999, 12, 31)
            correctDate = None
            try:
                newDate = datetime.datetime(year=year, month=month, day=date)
                correctDate = True
            except ValueError:
                correctDate = False
            if correctDate == True:
                j3 = (date_start <= newDate <= date_end)
            else:
                j3 = False
        elif pic[6] == "A":
            year = int("20" + pic[4:6])
            date_start = datetime.datetime(2000, 1, 1)
            time_now = datetime.datetime.now()
            correctDate = None
            try:
                newDate = datetime.datetime(year=year, month=month, day=date)
                correctDate = True
            except ValueError:
                correctDate = False
            if correctDate == True:
                j3 = (date_start <= newDate <= time_now)
            else:
                j3 = False
        judge = [j1, j2, j3, correctDate]
        if all(judge) == True:
            return True
        else:
            return False
    else: 
        return False
if __name__ == "__main__":
    print(is_it_valid("310286+713J"))