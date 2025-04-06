def distinct_numbers(my_list):
    list_new = []
    for i in my_list:
        while i not in list_new:
            list_new.append(i)
    return sorted(list_new)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) 
# [1, 2, 3]