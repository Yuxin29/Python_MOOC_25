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
          
def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    grid_copy = []
    for row in sudoku:
        row_copy = row[:]
        grid_copy.append(row_copy)
    grid_copy[row_no][column_no] = number
    return grid_copy
    
if __name__ == "__main__":
    sudoku = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 5, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    ]
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)