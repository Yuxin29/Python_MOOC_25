def print_sudoku(sudoku: list):
    row0 = 0
    for row in sudoku:
        if (row0 + 1) % 3 != 0:
            num0 = 0
            for i in row:
                if (num0 + 1) % 3 == 0:
                    if i == 0:
                        print("_  ", end="")
                        num0 += 1
                    else:
                        print(f"{i}  ", end="")
                        num0 += 1
                else:
                    if i == 0:
                        print("_ ", end="")
                        num0 += 1
                    else:
                        print(f"{i} ", end="")
                        num0 += 1
            print()
            row0 += 1
        else:
            num0 = 0
            for i in row:
                if (num0 + 1) % 3 == 0:
                    if i == 0:
                        print("_  ", end="")
                        num0 += 1
                    else:
                        print(f"{i}  ", end="")
                        num0 += 1
                else:
                    if i == 0:
                        print("_ ", end="")
                        num0 += 1
                    else:
                        print(f"{i} ", end="")
                        num0 += 1
            print()
            print()
            row0 += 1
          
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
    
if __name__ == "__main__":
    s = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
    [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
    [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
    [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
    [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
    [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
    [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
    ]
    print_sudoku(s)

    #return
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)