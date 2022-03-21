fin = open(".\data\schieramento.txt", "r")
tutto = fin.read()
fin.close()
tabella = tutto.split()

#Alternativa per creare una tabella dal file in cui ogni valore è un intero:
#for riga in fin:
#    tabella.append([int(n) for n in riga.strip()])

larghezza = 0
for riga in tabella:
    for carattere in riga:
        if carattere == "1":
            larghezza += 1
#Alternativa veloce:
# larghezza = tutto.count("1")

lunghezza = "0"
for riga in tabella:
    for carattere in riga:
        if carattere > lunghezza:
            lunghezza = carattere
#Alternativa veloce:
# lunghezza = max(tutto.replace("\n",""))

i = 0
trovato = False
while i < len(tabella) and not trovato:
    j = 0
    while j < len(tabella[0]) and not trovato:
        if tabella[i][j] == "2":
            trovato = True
        else: #per non sommare a j l'1 ancora una volta trovato il valore
            j += 1
    if not trovato: #per non sommare a j l'1 ancora una volta trovato il valore
        i += 1
if i>0 and tabella[i-1][j] == "1":
    print("Nord")
elif i<len(tabella)-1 and tabella[i+1][j] == "1":
    print("Sud")
elif j>0 and tabella[i][j-1] == "1":
    print("Ovest")
else:
    print("Est")

minimo = larghezza
fila = 1
for i in range(2, int(lunghezza)+1):
    if minimo > tutto.count(str(i)):
        minimo = tutto.count(str(i))
        fila = i
file = [0]*(int(lunghezza)+1) #creo un array di 0 lungo quanto la larghezza dello schieramento
for riga in tabella:
    for carattere in riga:
        file[int(carattere)]+=1
if fila == 1:
    print("0 buchi")
else:
    print("fila",fila)