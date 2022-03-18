from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Esercizio 1")

la = ttk.Label(root, text='questo spazio cambierà colore')

colori = ["red", "blue", "yellow", "white"]
coloriVar = StringVar(value=colori)
lb = Listbox(root, listvariable=coloriVar, height=4)

lb.pack()
la.pack()
root.mainloop()