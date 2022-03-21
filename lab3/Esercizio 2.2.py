from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Esercizio 2")

la = ttk.Label(root)

def yellowColor():
    la["background"] = "yellow"
b_yellow = ttk.Button(root, text='Yellow', command=yellowColor)
def redColor():
    la["background"] = "red"
b_red = ttk.Button(root, text='Red', command=redColor)
def blueColor():
    la["background"] = "blue"
b_blue = ttk.Button(root, text='Blue', command=blueColor)
def whiteColor():
    la["background"] = "white"
b_white = ttk.Button(root, text='White', command=whiteColor)

root.rowconfigure(0, weight=6)
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=2)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
la.grid(column=0, row=0, columnspan=2, sticky="nswe")
b_yellow.grid(column=0, row=1, sticky="nswe")
b_red.grid(column=0, row=2, sticky="nswe")
b_blue.grid(column=1, row=1, sticky="nswe")
b_white.grid(column=1, row=2, sticky="nswe")
root.mainloop()