from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Esercizio 3")

in_file = open(".\data\sabato.txt", "r", encoding="utf-8")
testo = in_file.read()
in_file.close()

text = Text(root, wrap="word") #non ho usato width e high perchè con sticky="nswe" il testo occupa tutto lo schermo disponibile
text.insert(0.0, testo)

scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=text.yview)
text.configure(yscrollcommand=scrollbar.set)

root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=1)
text.grid(column=0, row=0, sticky="nswe")
scrollbar.grid(column=1, row=0, sticky="nswe")

root.mainloop()