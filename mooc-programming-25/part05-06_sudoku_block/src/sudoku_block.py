def block_correct(sudoku: list, row_no: int, column_no: int):
    list_block = []
    rown = 0
    while rown < 3:
        row = sudoku[row_no + rown]
        columnn = 0
        while columnn < 3:
            list_block.append(row[column_no + columnn])
            columnn += 1
        rown += 1

    list_block_new = []
    for i in list_block:
        if i > 0:
            list_block_new.append(i)

    num = len(list_block_new)
    num0 = 0
    list_new = []
    for num0 in range (0,num):
        if list_block_new[num0] not in list_new:
            list_new.append(list_block_new[num0])
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
    print(block_correct(sudoku, 1, 2))