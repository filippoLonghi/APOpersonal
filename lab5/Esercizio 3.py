from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
root.title("Asteroid")
bestscore = 0

def main():
    global asteroidi, canvas, ship, vel, punteggio, testo_punteggio, bestscore, testo_bestscore
    vel = 3  # velocità della navicella
    punteggio = 0
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    canvas = Canvas(root, width= 500, height= 500)
    canvas.grid(column=0, row=0,sticky="nwes")
    canvas.create_rectangle(0,0,500,500,outline="white", fill="black")
    CENTER = 250 #posizione di partenza della navicella
    ship = canvas.create_polygon((0+CENTER,30+CENTER,30+CENTER,30+CENTER,15+CENTER,0+CENTER), outline="white", fill="black", width=3)
    root.bind("<Right>", lambda e: muovi_destra())
    root.bind("<Left>", lambda e: muovi_sinistra())
    root.bind("<Up>", lambda e: muovi_sopra())
    root.bind("<Down>", lambda e: muovi_sotto())
    testo_punteggio = canvas.create_text(40, 20, font = 40, fill = 'blue', text = "Points: " + str(punteggio))
    testo_bestscore = canvas.create_text(54, 40, font=40, fill='blue', text="Bestscore: " + str(bestscore))
    asteroidi = []
    muoviAsteroide()
    creaAsteroide()
    root.mainloop()

def muovi_destra():
    c = canvas.coords(ship)
    if c[2] < 500 and c[3] < 500:
        canvas.move(ship,vel,0)
def muovi_sinistra():
    c = canvas.coords(ship)
    if c[0] > 0 and c[1] < 500:
        canvas.move(ship,-vel,0)
def muovi_sopra():
    c = canvas.coords(ship)
    if c[5] > 0:
        canvas.move(ship,0,-vel)
def muovi_sotto():
    c = canvas.coords(ship)
    if c[1] < 500 and c[3] < 500:
        canvas.move(ship,0,vel)

def muoviAsteroide():
    global punteggio, testo_punteggio, bestscore,testo_bestscore
    for asteroide in asteroidi:
        canvas.move(asteroide, 0, 1)
        c = canvas.coords(asteroide)
        s = canvas.coords(ship)
        if len(canvas.find_overlapping(s[0],s[1],s[2],s[3]))==3:
            main()
        if c[1] > 500:
            canvas.delete(asteroide)
            asteroidi.remove(asteroide)
            punteggio += 1
            canvas.delete(testo_punteggio)
            testo_punteggio = canvas.create_text(40, 20, font=40, fill='blue', text= "Points: " + str(punteggio))
            if punteggio > bestscore:
                bestscore = punteggio
                canvas.delete(testo_bestscore)
                testo_bestscore = canvas.create_text(54, 40, font=40, fill='blue', text="Bestscore: " + str(bestscore))
    canvas.after(20, muoviAsteroide) #velocità delle asteroidi

def creaAsteroide():
    MAX = 80 #grandezza massima meteorite
    MIN = 40 #grandezza minima meteorite
    a = randint(MIN, MAX)
    asteroide = canvas.create_oval((0,0,a,a), outline="white", fill="black", width=2)
    canvas.move(asteroide, randint(a,500-a), -MAX)  # genera le asteroidi al di fuori del campo visibile dall'utente
    asteroidi.append(asteroide)
    canvas.after(2000,creaAsteroide) #numero di asteroidi generate

main()

