from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Esercizio 4")

spinval = StringVar()
spinval.set(0) # spinval.set(value=0)
spinbox = ttk.Spinbox(root,from_=0,to=100,textvariable=spinval,wrap=True)
spinbox.state(["readonly"])

def incrementaDiUno():
    spinbox["increment"] = 1
def incrementaDiDue():
    spinbox["increment"] = 2
def incrementaDiQuattro():
    spinbox["increment"] = 4
def incrementaDiOtto():
    spinbox["increment"] = 8
button_1 = ttk.Button(root, text='incrementa di 1', command=incrementaDiUno)
button_2 = ttk.Button(root, text='incrementa di 2', command=incrementaDiDue)
button_3 = ttk.Button(root, text='incrementa di 4', command=incrementaDiQuattro)
button_4 = ttk.Button(root, text='incrementa di 8', command=incrementaDiOtto)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
spinbox.grid(column=0, row=0, columnspan=2, sticky="nswe")
button_1.grid(column=0, row=1, sticky="nswe")
button_2.grid(column=0, row=2, sticky="nswe")
button_3.grid(column=1, row=1, sticky="nswe")
button_4.grid(column=1, row=2, sticky="nswe")
root.mainloop()