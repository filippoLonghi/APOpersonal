
class SortableCouple:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a_value(self):
        return self._a

    @property
    def b_value(self):
        return self._b

    def __repr__(self):
        return f'{(self._a, self._b)}'

    def __lt__(self, other):
        return self._a + self._b < other._a + other._b

class CoupleSorter:

    def __call__(self, sort_coup):
        return sort_coup.a_value - sort_coup.b_value

class WeightedSorter:

    def __init__(self, weight):
        if 0 <= weight <= 1:
            self._weight = weight

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        if 0 <= new_weight <= 1:
            self._weight = new_weight

    def __call__(self, sort_coup):
        return sort_coup.a_value * self.weight + sort_coup.b_value * (1 - self.weight)


def ordinamento_pesato(weight):
    def f(sort_coup):
        return sort_coup.a_value * weight + sort_coup.b_value * (1 - weight)
    return f

# def main():
#     tupla = SortableCouple(3,10)
#     print(tupla.a_value)
#     print(tupla.b_value)
#     print(tupla)
#     tupla2 = SortableCouple(0,4)
#     tupla3 = SortableCouple(1,2)
#     tupla4 = SortableCouple(2, 1)
#     tuple = [tupla3, tupla, tupla2, tupla4]
#     print(sorted(tuple))
#     print(sorted(tuple, key = lambda tupla: tupla.a_value*tupla.b_value))
#     ordinatore_di_coppie = CoupleSorter()
#     print(sorted(tuple, key = ordinatore_di_coppie))
#
#     ord_pesato = WeightedSorter(0.1)
#     print(ord_pesato.weight)
#     ord_pesato.weight = 0.4
#     print(ord_pesato.weight)
#     print(sorted(tuple, key=ord_pesato))
#
#     fun_di_ord = ordinamento_pesato(0.4)
#     for i in tuple:
#         print(fun_di_ord(i))
#     print(sorted(tuple, key=ordinamento_pesato(0.4)))

    #Il parametro Key nel sort vuole una funzione che dato un elemento nella lista mi da il valore che devo analizzare
    # per ordinare. Usa la funzione che gli passo in Key, la esegue su ogni elemento e da a sort il valore da analizzare.
    #l = sort(Key=abs) ordina la lista l secondo il valore assoluto.
    #Itemgetter è una closur factory del tipo: crea delle funzioni f che data una lista restituiscono l'elemento i esimo del parametro.

def main():
    a = SortableCouple(3, 3)
    b = SortableCouple(1, 5)
    c = SortableCouple(5, 0)

    couple_list = [a, b, c]

    couple_list.sort()
    print(couple_list)

    couple_list.sort(key=lambda x: x.a_value * x.b_value)
    print(couple_list)

    couple_list.sort(key=CoupleSorter())
    print(couple_list)

    a = SortableCouple(2, 2)
    b = SortableCouple(1, 3)
    c = SortableCouple(3, 1)

    couple_list = [a, b, c]

    sorter_cls = WeightedSorter(weight=0.2)
    sorter_fn = ordinamento_pesato(weight=0.8)

    couple_list.sort(key=sorter_cls)
    print(couple_list)

    couple_list.sort(key=sorter_fn)
    print(couple_list)


main()