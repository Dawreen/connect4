import numpy as np
from colorama import init, Fore, Style


class Board:
    def __init__(self, ROWS, COLS):
        self.ROWS = ROWS
        self.COLS = COLS
        self.grid = np.zeros((ROWS, COLS), dtype=int)

    def insert_piece(self, col: int, symbol: int) -> bool:
        self.grid[self.ROWS-1][col] = symbol
        return True
        '''
        if self.is_valid_move(col):
            row = self.ROWS - 1
            while row >= 0:
                if self.grid[row][col] == 0:
                    self.grid[row][col] = symbol
                    return True
                row -= 1
        return False
        '''
    
    # Resto del codice

    def print_board(self):
        init()
        for row in self.grid:
            for cell in row:
                if cell == 1:
                    print(Fore.YELLOW + " ●" + Style.RESET_ALL, end=" ")
                elif cell == 2:
                    print(Fore.RED + " ●" + Style.RESET_ALL, end=" ")
                else:
                    print(" ○" + Style.RESET_ALL, end=" ")
            print("\n")
        print("---------------------\n")
        

# create
def new_board(rows, cols):
    return np.zeros((rows, cols), dtype=int)

def insert_piece():
    # todo
    return False

def get_piece():
    # todo
    return False

def is_valid_move():
    return False


def print_board(matrix):
    init()
    for row in matrix:
        for cell in row:
            if cell == 1:
                print(Fore.YELLOW + "●", end=" ")
            elif cell == 2:
                print(Fore.RED + "●", end=" ")
            else:
                print("○", end=" ")
        print(Style.RESET_ALL)
