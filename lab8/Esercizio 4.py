class Ticket:

    def __init__(self, owner, pos_num):
        self._owner = owner
        self._pos_num = pos_num

    def get_queue_pos(self):
        return self._pos_num

    def __repr__(self):
        return f'{self._owner} {self._pos_num}'

    def __lt__(self, other):
        return self.get_queue_pos() < other.get_queue_pos()

class PriorityTicket(Ticket):

    def __init__(self, owner, pos_num, priority_num):
        super().__init__(owner, pos_num)
        self._priority_num = priority_num

    def get_queue_pos(self):
        return super().get_queue_pos() - self._priority_num * 10
        #return self._pos_num - (self._priority_num * 10)

    def __repr__(self):
        return super().__repr__() + f' p{self._priority_num}'

# def main():
#     biglietto1 = Ticket("Filippo",3)
#     print(biglietto1.get_queue_pos())
#     print(biglietto1)
#     biglietto2 = Ticket("Gianni", 4)
#     if biglietto1 < biglietto2:
#         print("Filippo prima di Gianni")
#
#     biglietto3 = PriorityTicket("Marco", 5, 2)
#     print(biglietto3.get_queue_pos())
#     print(biglietto3)
#
#     biglietti = [biglietto3, biglietto1, biglietto2]
#     biglietti.sort()
#     print(biglietti)

def main():
    t1 = Ticket("Mario Rossi", 37)
    t2 = Ticket("Enrico Bianchi", 25)
    t3 = PriorityTicket("Luca Gialli",43, 2)

    # coda non ordinata
    queue = [t1, t2, t3]
    print(queue)

    # coda ordinata usando __lt__() per confrontare elementi
    queue.sort()
    print(queue)

    # stessa cosa con sorted()
    queue = [t1, t2, t3]
    queue = sorted(queue)
    print(queue)

main()