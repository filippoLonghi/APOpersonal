#creo una tabella con i dati nel foglio di testo
#itero sulla tabella
#larghezza: numero di 1 nella tabella
#numero di file: numero maggiore nella tabella
#direzione: vedere quale numero è maggiore di quello attuale nelle quattro posizioni adiacenti
#fila con più buchi: fai un contatore che ti conta quanti numeri ci sono per ogni fila, il minore è la fila con più buchi

inputFile = open(".\data\schieramento.txt", "r")

schieramento = []
line = inputFile.readline()
while line != "":
    line = line.strip()
    riga = []
    for char in line:
        riga.append(int(char))
    schieramento.append(riga)
    line = inputFile.readline()

larghezza = 0
numero_di_file = 0
direzione = ""
file_rimanenti = {}
Found = False
for rig in range(len(schieramento)):
    for col in range(len(schieramento[0])):
        if schieramento[rig][col] == 1:
            larghezza += 1
        if schieramento[rig][col] > numero_di_file:
            numero_di_file = schieramento[rig][col]
        if schieramento[rig][col]==1 and rig-1 > 0 and schieramento[rig-1][col] > schieramento[rig][col] and not Found:
            direzione += "Sud"
            Found = True
        elif schieramento[rig][col]==1 and rig+1 > 0 and schieramento[rig+1][col] > schieramento[rig][col] and not Found:
            direzione += "Nord"
            Found = True
        elif schieramento[rig][col]==1 and col+1 > 0 and schieramento[rig][col+1] > schieramento[rig][col] and not Found:
            direzione += "Ovest"
            Found = True
        elif schieramento[rig][col]==1 and col-1 > 0 and schieramento[rig][col-1] > schieramento[rig][col] and not Found:
            direzione += "Est"
            Found = True
        if schieramento[rig][col] not in file_rimanenti:
            file_rimanenti[schieramento[rig][col]]=1
        else:
            file_rimanenti[schieramento[rig][col]]+=1
        fila_con_più_buchi =

