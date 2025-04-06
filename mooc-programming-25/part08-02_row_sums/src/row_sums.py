def row_sums(my_matrix: list):
    for row in my_matrix:
        sums = []
        for num in row:
            sums.append(num)
        all = sum(sums)
        row.append(all)

if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)