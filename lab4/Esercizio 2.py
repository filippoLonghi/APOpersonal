matrice = [["","",""],["","",""],["","",""]]
simboli = ["0", "X"]
turno = 0
mosse = 0
vittoria = False
def chekVittoria(tot):
    global vittoria, mosse
    if not vittoria and "000" in tot:
        label["text"] = "Ha vinto il giocatore 1 (0)"
        vittoria = True
    if not vittoria and "XXX" in tot:
        label["text"] = "Ha vinto il giocatore 2 (X)"
        vittoria = True
    if not vittoria and mosse == 8:
        label["text"] = "Pareggio"
def controllaVittoria():
    for i in range(3):
        totali = ["",""]
        for j in range(3):
            totali[0] += matrice[i][j]
            totali[1] += matrice[j][i]
        chekVittoria(totali)
    totali = ["",""]
    for j in range(3):
        totali[0] += matrice[j][j]
        totali[1] += matrice[j][2-j]
    chekVittoria(totali)

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Tris")
label = ttk.Label(root, text='', font=300)
label.grid(row = 4, column = 1, columnspan=3, sticky = "nswe")
def p(r,c):
    global turno, mosse
    if not vittoria and matrice[r][c] == "":
        matrice[r][c] = simboli[turno]
        if matrice[r][c] == "X":
            b[r][c].create_line((10, 10, 190, 190), width=5)
            b[r][c].create_line((10, 190, 190, 10), width=5)
        elif matrice[r][c] == "0":
            b[r][c].create_oval((10, 10, 190, 190), width=5)
        controllaVittoria()
        turno = (turno+1)%2
        mosse += 1
    return
b = [[0,0,0],[0,0,0],[0,0,0]]
for r in range(3):
    for c in range (3):
        b[r][c] = Canvas(root, width=200, height=200)
        quadrato = b[r][c].create_rectangle((0, 0, 200, 200), fill="yellow", width=5)
        b[r][c].tag_bind(quadrato, "<Button-1>", lambda e, a=r, b=c: p(a, b))
        b[r][c].grid(row = r, column = c, sticky = "nswe")
root.mainloop()