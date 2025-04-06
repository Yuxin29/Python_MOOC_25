def play_turn(game_board: list, x: int, y: int, piece: str):
    if 0 <= x <= 2 and 0 <= y <= 2:
        if game_board[y][x] == "":
            if piece == "X" or "O":
                game_board[y][x] = piece
                return True
            else:
                return False
        else:
            return False
    else:
        return False
 
if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)