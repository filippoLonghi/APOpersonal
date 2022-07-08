from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from chess.board import Board, Piece, ChessException
from chess.manager import ChessManager
from chess.competition import Player

class View(Tk):
    def __init__(self, model):
        super().__init__()
        self._board = model

        self.title("Chess")
        self.minsize(500, 300)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self._x = StringVar()
        self._y = StringVar()
        self._x_label = ttk.Label(self, text="X: ")
        self._y_label = ttk.Label(self, text="Y: ")
        self._x_entry = ttk.Entry(self, textvariable=self._x)
        self._y_entry = ttk.Entry(self, textvariable=self._y)
        self._x_label.grid(column=0, row=0, sticky=(N, S, W, E))
        self._y_label.grid(column=0, row=1, sticky=(N, S, W, E))
        self._x_entry.grid(column=1, row=0, sticky=(N, S, W, E))
        self._y_entry.grid(column=1, row=1, sticky=(N, S, W, E))

        self._b1 = ttk.Button(self, text="Remove piece", command=self.remove_piece)
        self._b2 = ttk.Button(self, text="Obtain piece", command=self.obtain_piece)
        self._b1.grid(column=0, row=2, sticky=(N, S, W, E))
        self._b2.grid(column=1, row=2, sticky=(N, S, W, E))

    def obtain_piece(self):
        x = int(self._x.get())
        y = int(self._y.get())
        try:
            message = f'{self._board.get_piece(x, y)} is in position ({x},{y})'
        except ChessException as e:
            message = str(e)
        messagebox.showinfo(title="Piece", message=message)

    def remove_piece(self):
        x = int(self._x.get())
        y = int(self._y.get())
        try:
            message = f'{self._board.get_piece(x, y)} removed from position ({x},{y})'
            self._board.add_piece(None, x, y)
        except ChessException as e:
            message = str(e)
        messagebox.showinfo(title="Piece", message=message)

def main():
    m = Board("b", 5)
    m.add_piece(Piece.ROOK, 0, 0)
    m.add_piece(Piece.KING, 4, 4)
    m.add_piece(Piece.BISHOP, 2, 3)
    m.add_piece(Piece.PAWN, 3, 0)
    v = View(m)
    v.mainloop()

main()