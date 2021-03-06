from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Esercizio 2")

la = ttk.Label(root)

def cambia_colore():
    la["background"] = colori[int(str(lb.curselection()).strip("(),"))]

colori = ["red", "blue", "yellow", "white"]
coloriVar = StringVar(value=colori)
lb = Listbox(root, listvariable=coloriVar, height=4)
lb.bind('<<ListboxSelect>>', lambda e: cambia_colore())

root.rowconfigure(0, weight=4)
root.columnconfigure(0, weight=4)
lb.grid(column=0, row=1, sticky="nswe")
la.grid(column=0, row=0, sticky="nswe")
root.mainloop()