from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Esercizio 1")

label = ttk.Label(root, text='questo spazio cambierà colore')

num = 0
def changeColor():
    global num
    colors = ["red", "blue", "yellow", "white"]
    label["background"] = colors[num]
    if num < 3:
        num += 1
    else:
        num = 0

b = ttk.Button(root, text='Cambia colore', command=changeColor)

label.pack()
b.pack()
root.mainloop()