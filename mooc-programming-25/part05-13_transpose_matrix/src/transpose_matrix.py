def transpose(matrix: list):
    num = len(matrix)
    lst = []
    for row in range(num):
        print(row)
        line = [0] * num
        lst.append(line)

    for row in range(num):
        for col in range(num):
            lst[row][col] = matrix[col][row]

    for row in range(num):
        for col in range(num):
            matrix[row][col] = lst[row][col]

if __name__ == "__main__":
    matrix = [
        [9, 4],
        [3, 0]
        ]  
    matrix = [
        [1, 2],
        [1, 2]
        ]  
    print(transpose(matrix))