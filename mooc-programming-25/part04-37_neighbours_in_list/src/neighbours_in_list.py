def longest_series_of_neighbours(my_list: list):
    length = []
    number = 1
    while number < len(my_list):
        len0 = 0
        n0 = 0
        while my_list[n0] - my_list[n0 + 1] == 1 or -1:
            n0 = 0
            len0 += 1
        length.append(len0)
        number += 1
    return max.length

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))