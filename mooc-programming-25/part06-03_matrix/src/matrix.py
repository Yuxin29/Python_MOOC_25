def matrix_sum():
    with open("src/matrix.txt") as new_file:
        list_sum = 0
        for line in new_file:
            arr = line.split(",")
            for item in arr:
                int_item = int(item)
                list_sum += int_item
        return list_sum
def matrix_max():
    with open("src/matrix.txt") as new_file:
        list_max = []
        for line in new_file:
            arr = line.split(",")
            for item in arr:
                int_item = int(item)
                list_max.append(int_item)
        return max(list_max)
def row_sums():
    with open("src/matrix.txt") as new_file:
        sum_row = []
        for line in new_file:
            list_rows = []
            arr = line.split(",")
            for item in arr:
                int_item = int(item)
                list_rows.append(int_item)
                sum0 = sum(list_rows)
            sum_row.append(sum0)
        return sum_row

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())