from chess.board import Board, ChessException, Piece
from chess.competition import Player, Tournament
from typing import List, Optional


class ChessManager:
    def __init__(self) -> None:
        self._boards = {} #{board_name: Board()}
        self._players = {} #{player_name: Player()}
        self._tournaments = {} #{tournament_name: Tournaments()}

    # R2
    def add_board(self, board: Board) -> None:
        self._boards[board.name] = board

    def get_board(self, name: str) -> Board:
        return self._boards[name]

    def add_player(self, player: Player) -> None:
        self._players[player.name] = player

    def get_player(self, name: str) -> Player:
        return self._players[name]

    def add_player_to_board(self, player_name: str, board_name: str) -> None:
        self._players[player_name].add_board(self._boards[board_name])

    def get_boards_of_player(self, name: str) -> List[Board]:
        return self._players[name].get_board()

    # R3
    def create_tournament(self, name: str) -> None:
        if name in self._tournaments:
            raise ChessException("Torneo con lo stesso nome già creato")
        self._tournaments[name] = Tournament(name)

    def add_player_score(self, tournament_name: str, player_name: str, score: int) -> None:
        if player_name not in self._players:
            raise ChessException("Giocatore non definito")
        self._tournaments[tournament_name].add_player_score(self._players[player_name], score)

    def get_leading_player(self, tournament_name: str) -> Optional[str]:
        return self._tournaments[tournament_name].get_leading_player()

    # R5
    def fill_queens(self, board_name: str, board_size: int) -> Board:
        queens_board = Board(board_name, board_size)
        for k in range(board_size):
            for i in range(board_size):
                for j in range(board_size):
                    if self.check_queen(queens_board, i,j):
                        queens_board.add_piece(Piece.QUEEN, i, j)
        return queens_board

    @staticmethod
    # METODO GIÀ FORNITO
    # controlla se è possibile inserire regina in posizione x, y:
    # - cella vuota
    # - non sotto attacco da altre regine
    def check_queen(board: Board, x: int, y: int) -> bool:
        # controllo riga-colonna
        for i in range(board.dim):
            if board.get_piece(i, y) is not None or board.get_piece(x, i) is not None:
                return False
        # controllo diagonale primaria
        x_pos = x - min(x, y)
        y_pos = y - min(x, y)
        while x_pos < board.dim and y_pos < board.dim:
            if board.get_piece(x_pos, y_pos) is not None:
                return False
            x_pos += 1
            y_pos += 1
        # controllo diagonale secondaria
        x_pos = x - min(x, board.dim - y - 1)
        y_pos = y + min(x, board.dim - y - 1)
        while x_pos < board.dim and y_pos >= 0:
            if board.get_piece(x_pos, y_pos) is not None:
                return False
            x_pos += 1
            y_pos -= 1
        return True















