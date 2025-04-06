def row_correct(sudoku: list, row_no: int):
    # go through each row and select the item at the chosen position
    list_row = []
    for i in sudoku[row_no]:
        if i > 0:
            list_row.append(i)
    num = len(list_row)
    num0 = 0
    list_new = []
    for num0 in range (0,num):
        if list_row[num0] not in list_new:
            list_new.append(list_row[num0])
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
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))