def all_the_longest(my_list: list):
    length = 0
    for item in my_list:
        if len(item) > length:
            length = len(item)
    longest = []
    for item in my_list:
        if len(item) == length:
            longest.append(item)
    return longest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print(all_the_longest(my_list))