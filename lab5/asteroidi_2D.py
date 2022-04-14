from tkinter import *
from tkinter import ttk
from random import randint

pd=10 #spostamento del personaggio (di quanti pixel si sposta con le frecce)
punti=0

def inizio():
    global continua
    continua=False
    canvas.delete("all")
    w=Toplevel() #creo una nuova finestra
    w.title("Nuova Partita")
    l=ttk.Label(w,text="Come ti chiami?")
    l.grid(row=0,column=0)
    e=ttk.Entry(w) #metto una entry nella finestra
    m=messaggio.get().split()[0]
    if m!="Punti":
        e.insert(0,messaggio.get().split()[0])
    e.grid(row=1,column=0)
    e.focus_set() #per aprire la finestra e avere il focus direttamente sulla Entry
    b=ttk.Button(w,text="Gioca!",command=lambda: pronto(e.get(),w)) #e.get() è ciò che ha scritto il giocatore, w è la finestra
    b.grid(row=2,column=0)
    w.bind("<Return>",lambda ev:pronto(e.get(),w))

def pronto(nome,w):
    global personaggio, conta, continua, frequenza, velocita, punti #setto gli elementi del gioco e azzero tutti quando ricomincio la partita
    punti=0
    conta = 0
    continua = True
    frequenza = 30
    velocita = 10
    messaggio.set(nome+" Punti: "+str(punti)) #la StrinVar del punteggio
    w.destroy()
    personaggio = canvas.create_image(250,250,image=foto)
    arrivo()
    arrivo() #ogni arrivo fa arrivare un nuovo asteroide in contemporanea agli altri

def arrivo():
    if continua:
        global velocita
        bordo=randint(0,3) #scelgo uno dei quattro bordi da cui far entrare gli asteroidi
        posizione=randint(1,499) #scelgo la posizione (il pixel) da cui entra l'asteroide
        uscita=randint(1,499) #scelgo la posizione da cui esce l'asteroide
        dif=uscita-posizione #avrò un percorso lungo 500 e largo la differenza tra dove entra ed esce l'asteroide
        if bordo==0: #il meteorite si muoverà lungo la diagonale
            x=-50
            y=posizione
            direzioneY=(velocita*dif)//(abs(dif)+500)
            direzioneX=velocita-abs(direzioneY)
        elif bordo==1:
            x=500
            y=posizione
            direzioneY=(velocita*dif)//(abs(dif)+500)
            direzioneX=-velocita+abs(direzioneY)
        elif bordo==1:
            y=-50
            x=posizione
            direzioneX=(velocita*dif)//(abs(dif)+500)
            direzioneY=velocita-abs(direzioneX)
        else:
            y=500
            x=posizione
            direzioneX=(velocita*dif)//(abs(dif)+500)
            direzioneY=abs(direzioneX)-velocita

        # meteorite=canvas.create_oval(x,y,x+50,y+50, fill="black")
        meteorite=canvas.create_image(x+25,y+25,image=foto_a)
        muovi((meteorite,direzioneX,direzioneY)) #muovi prende una tupla di 3 valori
        if continua:
            global frequenza
            canvas.after(100*frequenza,lambda: arrivo()) #programmo l'arrivo di un nuovo elemento
            if frequenza > 5: #all'inizio non voglio che l'asteroide sia troppo veloce
                frequenza-=1
            if frequenza%5==0:#faccio muovere sempre più velocemente gli asteroidi
                velocita+=1


def muovi(e):
    global punti
    (m, dX, dY)=e
    if continua:
        canvas.move(m,dX,dY)
        c=canvas.coords(m)
        if c[0]>-25 and c[1]>-25 and c[0]<525 and c[1]< 525: #se il meteorite è ancora dentro controllo la collisione
            if controlla(m): #se non è avvenuta la collisione faccio muovere l'asteroide ulteriormente
                canvas.after(50,lambda e=(m,dX,dY): muovi(e))
        else:
            canvas.delete(m)
            punti+=1
            print("PUNTO:",punti)
            testo=messaggio.get().rsplit(" ",1)
            messaggio.set(testo[0]+" "+str(punti))


def controlla(m):
    global continua
    astro=canvas.coords(personaggio) #coordinate personaggio
    cm=canvas.coords(m) #coordinate meteorite
    #centroA=(astro[0]+astro[2])//2,(astro[1]+astro[3])//2
    centroA = astro
    # centroM=(cm[0]+cm[2])//2,(cm[1]+cm[3])//2
    centroM=cm
    #raggioA=(astro[2]-astro[0])//2
    raggioA=25
    raggioM=25
    # raggioM=(cm[2]-cm[0])//2
    if (centroA[0]-centroM[0])**2+(centroA[1]-centroM[1])**2<(raggioA+raggioM)**2: #stabilisco se c'è stato un impatto in base alla distanza tra il centro del personaggio e quella del cerchio
        continua=False
        print("COLLISIONE")
        canvas.delete("all")
        return False
    else:
        return True


def nord():
    canvas.move(personaggio, 0, -pd)
def sud():
    canvas.move(personaggio, 0, pd)
def est():
    canvas.move(personaggio, pd, 0)
def west():
    canvas.move(personaggio, -pd, 0)

#parte grafica:
continua=True #quando finisce la partita voglio che gli oggetti si blocchino: distruggo gli elementi nel canvas
root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
messaggio=StringVar()
messaggio.set("Punti")
schermo=ttk.Label(root,textvariable=messaggio,background="white")
schermo.grid(row=0,column=0,sticky="snew")
canvas = Canvas(root, width= 500, height= 500)
x=10
foto=PhotoImage(file="personaggio.gif")
foto_a=PhotoImage(file="asteroide.gif")

canvas.grid(column=0, row=1,sticky=(N, W, E, S))

root.option_add('*tearOff', FALSE)
menubar = Menu(root)
root['menu'] = menubar
menu_gioca = Menu(menubar)
menubar.add_cascade(menu=menu_gioca, label='Gioca')
menu_gioca.add_command(label='New Game', command=inizio)

i=0
nuovo=True
root.bind("<Return>",lambda e :inizio()) #con Enter inizio una nuova partita
root.bind('<Up>',lambda e:nord())
root.bind('<Down>',lambda e:sud())
root.bind('<Left>',lambda e:west())
root.bind('<Right>',lambda e:est())


root.mainloop()

