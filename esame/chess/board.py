from typing import Optional


class ChessException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Piece:
    KING = "KING"
    QUEEN = "QUEEN"
    BISHOP = "BISHOP"
    KNIGHT = "KNIGHT"
    ROOK = "ROOK"
    PAWN = "PAWN"


class Board:
    def __init__(self, name: str, dim: int) -> None:
        self._name = name
        self._dim = dim
        self._board = [[None]*dim for i in range(dim)]

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def dim(self) -> int:
        return self._dim

    @dim.setter
    def dim(self, dim):
        self._name = dim

    def add_piece(self, piece: Optional[str], x: int, y: int) -> None:
        if x >= self._dim or y >= self._dim:
            raise ChessException("Posizione fornita non valida") #usa try except con IndexError
        self._board[x][y] = piece

    def get_piece(self, x: int, y: int) -> Optional[str]:
        if x >= self._dim or y >= self._dim:
            raise ChessException("Posizione fornita non valida")
        return self._board[x][y]
