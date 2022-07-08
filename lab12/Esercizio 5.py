class Nodo:
    def __init__(self, dato):
        self._dato = dato
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, dato):
        self._next = dato

    @property
    def dato(self):
        return self._dato

class Coda:
    def __init__(self):
        self._testa = None
        self._coda = None

    def append(self, dato):
        n = Nodo(dato)
        if self._testa == None:
            self._testa = n
            self._coda = n
        else:
            self._coda.next = n
            self._coda = n

    def pop(self):
        if self._testa == None:
            self._coda = None
            return None
        dato = self._testa.dato
        self._testa = self._testa.next
        return dato

    def __getitem__(self, pos):
        if pos == 0:
            return self._testa.dato
        elif pos < 0:
            return "Posizione non valida"
        else:
            i = 1
            n = self._testa.next
            while i < pos:
                if n.next != None:
                    n = n.next
                else:
                    return "Posizione non valida"
                i += 1
            return n.dato

    @property
    def testa(self):
        return self._testa.dato

    @property
    def coda(self):
        return self._coda.dato

    def __repr__(self):
        list = ""
        if self._testa == None:
            list = ""
        else:
            n = self._testa
            list += f'{n.dato} '
            while n.next != None:
                n = n.next
                list += f"{n.dato} "
        return list

def main():
    c = Coda()
    c.append(12) #[12]
    c.append(13) #[12, 13]
    c.append(1)  #[12, 13, 1]
    print(c.testa) #12
    print(c.coda) #1
    print(c[1]) #13
    print(c)
    print(c.pop()) #12

main()