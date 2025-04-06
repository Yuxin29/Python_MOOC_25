def shortest(my_list: list):
    long = ""
    for item in my_list:
        if len(item) >= len(long):
            long = item
    length = len(long)
    short = long
    for item in my_list:
        if len(item) <= len(short):
            short = item
    return short

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print(shortest(my_list))