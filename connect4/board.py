import numpy as np
from colorama import init, Fore, Style

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
