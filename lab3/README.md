# Laboratorio 3
In questo laboratorio si introducono le interfacce grafiche.
I concetti principali su sui prendere confidenza sono:
- utilizzo di widget grafici comuni
- gestione di eventi tramite callback
- utilizzo di geometry manager

Inoltre, durante il laboratorio, verranno introdotti i concetti base della configurazione di progetti python,
ovvero la creazione di progetti con più file, 
organizzazione in moduli e pacchetti,
utilizzo di virtual environments e installazione di librerie.

## Esercizio 1
Creare un'interfaccia grafica contenente una label e un bottone.
Ogni volta che il bottone è premuto la label deve cambiare proprio colore di sfondo.

Scegliere a piacere quali e quanti colori utilizzare.
Una volta passati tutti i colori di sfondo, ricominciare dal primo.

## Esercizio 2
Modificare l'interfaccia grafica sviluppata al punto precedente 
per permettere all'utente di selezionare direttamente il colore di sfondo
da una selezione messa disposizione dal programmatore.

Inoltre, se non già fatto precedentemente,
cercare di prevenire comportamenti non voluti quando si ridimensiona la finestra.
Ad esempio:
- widged non si ridimensionano
- widget non occupano spazio a disposizione e lasciano aree bianche
- la finestra inizialmente creata è troppo piccola
- ecc... 

Farsi aiutare da frame e geometry manager (grid è preferibile).

## Esercizio 3
Creare un'interfaccia grafica che permetta di visualizzare il contenuto
del file *sabato.txt*, mantenendo gli a capo quando presenti.

L'intero testo non deve essere visibile contemporaneamente,
ma deve essere accessibile tramite una barra di scorrimento verticale posta a lato.

## Esercizio 4
Creare un'interfaccia grafica che gestisca un contatore circolare
e visualizzi il valore attuale, limitato all'intervallo *[0, 100]*.
L'utente deve poter incrementare e decrementare il valore con step *1*, *2*, *4* e *8*.

## Esercizio 5
Creare un'interfaccia grafica che permetta d'inserire
nomi di giocatori e i rispettivi punteggi (floating point).
L'interfaccia deve aggiornare e visualizzare, in modo ordinato,
nomi e punteggi dei tre miglior giocatori.

Se un giocatore viene inserito più volte esso non deve essere duplicato,
ma il suo ponteggio deve essere aggiornato all'ultimo fornito.