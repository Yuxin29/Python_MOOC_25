def column_correct(sudoku: list, column_no: int):
    # go through each row and select the item at the chosen position
    list_column = []
    for row in sudoku:
        if row[column_no] > 0:
            list_column.append(row[column_no])

    num = len(list_column)
    num0 = 0
    list_new = []
    for num0 in range(0, num):
        if list_column[num0] not in list_new:
            list_new.append(list_column[num0])
            num0 += 1
    if len(list_new) == num:
        return True
    else:
        return False

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]
    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))