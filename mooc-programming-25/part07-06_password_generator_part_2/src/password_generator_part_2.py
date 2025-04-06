import string
from random import choice
from string import ascii_letters, digits, punctuation
import operator as op
def generate_strong_password(length: int, arguement1, arguement2):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    character = ["!", "?", "=", "+", "-", "(", ")", "#"]
    number = ["1", "2", "3", "4", "5","6", "7", "8", "9"]
    string.letter = "abcdefghijklmnopqrstuvwxyz"
    string.cha = "!?=+-()#"
    string.num = "0123456789"
    combine1 = letters + number
    combine2 = letters + character
    combine3 = letters + number + character
    if arguement1 == False and arguement2 == False:
        password = ""
        num = 1
        while num <= length:
            cha = choice(letters)
            password += cha
            num += 1
        return password
    elif arguement1 == True and arguement2 == False:
        password = "!"
        j1 = [password in string.ascii_letters, password in string.digits]
        while all(j1) != True:
            password = ""
            num = 1
            while num <= length:
                cha = choice(combine1)
                password += cha
                num += 1
            print(password)
            flag_l = False
            flag_2 = False
            for i in password:
                if op.countOf(string.letter, i) > 0:
                    flag_1 = True
                if op.countOf( string.num, i) > 0:
                    flag_2 = True
            j1 = [flag_1, flag_2]   
            print(j1)
        return password
    elif arguement1 == False and arguement2 == True:
        password = "2"
        j2 = [password in string.ascii_letters, password in string.cha]
        while all(j2) != True:
            password = ""
            num = 1
            while num <= length:
                cha = choice(combine2)
                password += cha
                num += 1
            flag_l = False
            flag_2 = False
            for i in password:
                if op.countOf(string.letter, i) > 0:
                    flag_1 = True
                if op.countOf(string.cha, i) > 0:
                    flag_2 = True
            j2 = [flag_1, flag_2]   
        return password
    else:
        password = "3"
        j3 = [password in string.ascii_letters, password in string.digits, password in string.cha]
        while all(j3) != True:
            password = ""
            num = 1
            while num <= length:
                cha = choice(combine3)
                password += cha
                num += 1
            flag_l = False
            flag_2 = False
            flag_3 = False
            for i in password:
                if op.countOf(string.letter, i) > 0:
                    flag_1 = True
                if op.countOf(string.cha, i) > 0:
                    flag_2 = True
                if op.countOf( string.num, i) > 0:
                    flag_3 = True
            j3 = [flag_1, flag_2, flag_3]   
        return password

if __name__ == "__main__":
    for i in range(2):
        print(generate_strong_password(8, True, False))