from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Esercizio 2")

la = ttk.Label(root)

def funzione(*args):
    if lb.select_includes(0):
        la["background"] = "red"
    elif lb.select_includes(1):
        la["background"] = "blue"
    elif lb.select_includes(2):
        la["background"] = "yellow"
    elif lb.select_includes(3):
        la["background"] = "white"

colori = ["red", "blue", "yellow", "white"]
coloriVar = StringVar(value=colori)
lb = Listbox(root, listvariable=coloriVar, height=4)
lb.bind('<Button-1>', funzione)

root.rowconfigure(0, weight=4)
root.columnconfigure(0, weight=4)
lb.grid(column=0, row=1, sticky="nswe")
la.grid(column=0, row=0, sticky="nswe")
root.mainloop()