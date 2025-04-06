import string
def separate_characters(my_string: str):
    (first, second, third) = ("","","")
    for i in my_string:
        if i in string.ascii_letters:
            first += i
        elif i in string.punctuation:
            second += i
        else:
            third += i
    parts = (first, second, third)
    return parts

if __name__ == "__name__":
    separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])