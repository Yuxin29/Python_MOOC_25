def list_sum(list1, list2):
    num = len(list1)
    index = 0
    list_new = []
    while index < num:
        num1 = list1[index] + list2[index]
        index += 1
        list_new.append(num1)
    return list_new

if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [7, 8, 9]
    print(list_sum(list1, list2)) 
# [8, 10, 12]