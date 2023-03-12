from board import Board

class HumanPlayer:
    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.symbol = symbol

    def make_move(self, board: Board) -> bool:
        #board.insert_piece(0, self.symbol)
        #return True
        while True:
            try:
                col = int(input(f"{self.name}, inserisci una colonna (1-7): "))
                if col < 1 or col > 7:
                    raise ValueError
                #if not board.is_valid_move(col - 1):
                #    raise ValueError
                board.insert_piece(col - 1, self.symbol)
                return True
            except ValueError:
                print("Inserisci una colonna valida!")
