def who_won(game_board: list):
    sum1 = 0
    sum2 = 0
    for row in game_board:
        for square in row:
            if square == 1:
                sum1 += 1
            elif square == 2:
                sum2 += 1
            else:
                print()
    if sum1 > sum2:
        return 1
    elif sum2 > sum1:
        return 2
    else:
        return 0

if __name__ == "__main__":
    game_board = [[1, 2, 1], [0, 1, 1], [1, 2, 2]]
    who_won(game_board)