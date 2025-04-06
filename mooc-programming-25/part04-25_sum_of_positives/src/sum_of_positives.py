def sum_of_positives(my_list):
    list_p = []
    for i in my_list:
        if i > 0:
            list_p.append(i)
    return sum(list_p)

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
    