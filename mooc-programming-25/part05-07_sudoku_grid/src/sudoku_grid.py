def row_correct(sudoku, row_no):
    list_row = []
    for int in sudoku[row_no]:
        if int > 0:
            list_row.append(int)
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

def column_correct(sudoku, column_no):
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

def block_correct(sudoku, row_no, column_no):
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

def sudoku_grid_correct(sudoku):
    row_no = 0
    juldge_list = []
    while row_no <= 6:
        column_no = 0
        while column_no <= 6:
            if row_correct(sudoku, row_no) == column_correct(sudoku, column_no) == block_correct(sudoku, row_no, column_no) == True:
                juldge_list.append("1")
            else:
                juldge_list.append("0")
            column_no += 3
        row_no += 3
    print(juldge_list)
    return "0" not in juldge_list

if __name__ == "__main__":
    sudoku1 = [
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
    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
        ]
    print(sudoku_grid_correct(sudoku1))
    print(sudoku_grid_correct(sudoku2))