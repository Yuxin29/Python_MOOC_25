import re

def is_dotw(my_string: str):
    if re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string):
        return True
    else:
        return False
def all_vowels(my_string: str):
    if re.search("[bcdfghjklmnpqrstvwxyz]", my_string):
        return False
    else:
        return True
def time_of_day(my_string: str):
    if my_string[0:2] in re.search("[0-24]", my_string[0:2]):
        if my_string[2:4] in re.search("[0-59]", my_string[2:4]):
            if my_string[4:6] in re.search("[0-59]", my_string[4:6]):
                return True
            else: 
                return False
        else: 
                return False
    else: 
                return False
    
if __name__ == "__main__":
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))