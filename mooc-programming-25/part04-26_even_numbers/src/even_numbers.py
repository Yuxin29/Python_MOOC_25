def even_numbers(my_list):
    list_e = []
    for i in my_list:
        if i % 2 == 0:
            list_e.append(i)
    return list_e

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)