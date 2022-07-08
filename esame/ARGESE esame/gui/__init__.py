from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from games.card_game import Card


def esegui():
    global stringvar1, stringvar2, stringvar3, stringvar4, lista_mazzo
    nome = stringvar1.get()
    attacco = stringvar2.get()
    life_points = stringvar3.get()
    mana = stringvar4.get()
    new_card = Card(nome, attacco, life_points, mana)
    lista_mazzo.append(new_card)


def esegui_mazzo():
    global lista_mazzo, root
    mazzo = ttk.Label(root, text=str(lista_mazzo))
    mazzo.grid(column=1, row=4)

def main():
    global stringvar1, stringvar2, stringvar3, stringvar4, lista_mazzo, root
    root = Tk()
    root.title("Gioco")

    lista_mazzo = []

    label1= ttk.Label(root, text="Inserisci nome carta")
    label1.grid(column=0, row=0)
    label2 = ttk.Label(root, text="Inserisci attacco")
    label2.grid(column=0, row=1)
    label3 = ttk.Label(root, text="Inserisci life points")
    label3.grid(column=0, row=2)
    label4 = ttk.Label(root, text="Inserisci mana")
    label4.grid(column=0, row=3)

    stringvar1 = StringVar()
    entry1 = ttk.Entry(root, textvariable=stringvar1)
    entry1.grid(row=0, column=1)
    stringvar2 = StringVar()
    entry2 = ttk.Entry(root, textvariable=stringvar2)
    entry2.grid(row=1, column=1)
    stringvar3 = StringVar()
    entry3 = ttk.Entry(root, textvariable=stringvar3)
    entry3.grid(row=2, column=1)
    stringvar4 = StringVar()
    entry4 = ttk.Entry(root, textvariable=stringvar4)
    entry4.grid(row=3, column=1)

    bott1 = ttk.Button(root, text="Inserisci carta\nnel mazzo", command=esegui)
    bott1.grid(rowspan=4, row=0, column=2)
    bott2 = ttk.Button(root, text="Visualizza mazzo", command=esegui_mazzo)
    bott2.grid(row=4, column=0)


    root.mainloop()

main()