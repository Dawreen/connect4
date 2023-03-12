from board import new_board, print_board

#the original game is 6 by 7
ROWS = 6 
COLS = 7 


if __name__ == "__main__":
    # Start game
    # create game, board ecc. 

    matrix = new_board(ROWS, COLS)
    print_board(matrix)