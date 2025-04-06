def no_shouting(my_list):
    pruned_list = []
    for word in my_list:
        if word.isupper() != True:
            pruned_list.append(word)
    return pruned_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    print(no_shouting(my_list))