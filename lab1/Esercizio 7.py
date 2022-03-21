from operator import itemgetter
from re import split

infile = open("C:\\Users\\Filippo Longhi\\OneDrive - Politecnico di Torino\\Politecnico\\Algoritmi e Programmazione "
                 "ad Oggetti\\Laboratori\\APOpersonal\\lab1\\data\\promessi_sposi.txt", "r")

parole = infile.read()
infile.close()
parole = split("[^a-zA-Z]", parole)

#In alternativa:
#for i in range(len(parole)):
#    if not parole[i].isalpha():
#        parole = parole[:i] + " " + parole[i+1:]
#parole = parole.split()

#in alternativa:
#parole = ""
#c = infile.read(1)
#while c!= "":
#   if c.isalpha():
#       parole += c
#   else:
#       parole += " "
#   c = infile.read(1)
#infile.close()
#parole = parole.split()

valori={}
for p in parole:
    if p in valori:
        valori[p] += 1
    else:
        valori[p] = 1

#in alternativa:
#for p in parole:
#   valori[p] = valori.get(p,0)+1

risultato = sorted(valori.items(), key=itemgetter(1))[:-100:-1]
print(risultato)