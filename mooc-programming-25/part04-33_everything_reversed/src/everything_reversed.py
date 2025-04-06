def everything_reversed(my_list: list):
    list_reverse = []
    for word in my_list:
        word_reverse = word[::-1]
        list_reverse.append(word_reverse)
    new_list = list_reverse[::-1]
    return new_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    print(everything_reversed(my_list))    