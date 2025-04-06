def list_of_stars(my_list):
    index = 0
    leng = len(my_list)
    while index < leng:
        print("*" * my_list[index])
        index += 1

if __name__ == "__main__":
    my_list = [1, 3, 5, 1]
    list_of_stars(my_list)