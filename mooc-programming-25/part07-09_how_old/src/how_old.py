from datetime import datetime, timedelta
day = int(input("Day:"))
month = int(input("Month:"))
year = int(input("Year:"))
birthday = datetime(year, month, day)
millennium = datetime(1999, 12, 31)

if birthday > millennium:
    print("You weren't born yet on the eve of the new millennium.")
else:
    difference = millennium - birthday
    print(f"You were {difference.days} days old on the eve of the new millennium.")