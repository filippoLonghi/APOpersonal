import operator
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Esercizio 5")

label = ttk.Label(root, text='Nome del giocatore e punteggio:')

input_utente = StringVar()
entry = ttk.Entry(root, textvariable=input_utente, width=50)

text = Text(root, width=50, height=3)

diz = {}
def Inserisci():
    dato = input_utente.get()
    dato = dato.rsplit(maxsplit=1)
    diz[dato[0]] = int(dato[1])
    list = sorted(diz.items(), key=operator.itemgetter(1), reverse=True)
    text.delete('1.0','4.0')
    if len(list) == 1:
        text.insert("1.0", f'{list[0][0]:20}{list[0][1]}')
    if len(list) == 2:
        text.insert("1.0", f'{list[0][0]:20}{list[0][1]}\n{list[1][0]:20}{list[1][1]}')
    if len(list) > 2:
        text.insert("1.0", f'{list[0][0]:20}{list[0][1]}\n{list[1][0]:20}{list[1][1]}\n{list[2][0]:20}{list[2][1]}')
    # for s, p in list[:3]:
    #     text.insert(END, f"{s}: {p}\n")
    input_utente.set("")
button = ttk.Button(root, text='Aggiorna classifica', command=Inserisci)
root.bind("<Return>", lambda e: Inserisci())

label.pack()
entry.pack()
button.pack()
text.pack()
root.mainloop()