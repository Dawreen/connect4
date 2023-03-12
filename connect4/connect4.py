from board import Board, print_board
from player import HumanPlayer

#the original game is 6 by 7
ROWS = 6 
COLS = 7 


if __name__ == "__main__":
    # Start game
    # create game, board ecc. 

    player1 = HumanPlayer("Dan", 1)

    game_board = Board(ROWS, COLS)
    game_board.print_board()

    player1.make_move(game_board)
    game_board.print_board()
