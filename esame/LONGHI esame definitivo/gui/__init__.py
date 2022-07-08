from tkinter import *
from tkinter import ttk, messagebox
from games.card_game import Card, Player, GameException, Tournament


# classe View eredita da TK
class View(Tk):
    def __init__(self, model, controller):
        super().__init__()
        # salvo model e controller
        self._model = model
        self._controller = controller

        # creo finestra
        self.title("Card game")
        self.minsize(500, 300)

        # configuro grid
        for i in range(4):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # creo StringVar per campi di input
        self._name = StringVar()
        self._attack = StringVar()

        # creo labels per campi in di input
        self._name_label = ttk.Label(self, text="Name: ")
        self._cals_label = ttk.Label(self, text="Attack: ")

        # creo campi di input per materia prima
        self._name_entry = ttk.Entry(self, textvariable=self._name)
        self._cals_entry = ttk.Entry(self, textvariable=self._attack)

        # posiziono labels
        self._name_label.grid(column=0, row=0, sticky=(N, S, W, E))
        self._cals_label.grid(column=0, row=1, sticky=(N, S, W, E))

        # posiziono campi di input
        self._name_entry.grid(column=1, row=0, sticky=(N, S, W, E))
        self._cals_entry.grid(column=1, row=1, sticky=(N, S, W, E))

        # aggiungo bottoni, callback evento è un metodo del controller
        self._b1 = ttk.Button(self, text="Add card", command=self._controller.add_card)
        self._b2 = ttk.Button(self, text="Get cards", command=self._controller.get_cards)
        self._b1.grid(column=0, row=2, columnspan=2, sticky=(N, S, W, E))
        self._b2.grid(column=0, row=3, columnspan=2, sticky=(N, S, W, E))

    @staticmethod
    def show_message_box(title, message):
        messagebox.showinfo(title=title, message=message)

    # proprietà della view
    @property
    def name(self):
        return self._name.get()

    @property
    def attack(self):
        return self._attack.get()

class Controller:
    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    def add_card(self):
        self._model.add_card(Card(self._view.name, int(self._view.attack), 0, 0))
        self._view.show_message_box(title="Done", message="Carta aggiunta")

    def get_cards(self):
        cards = self._model.get_cards()
        # uso la view per visualizzarle
        msg_str = "\n".join([f'name:{elm.name}, attack:{elm.attack}' for elm in cards])
        self._view.show_message_box(title="Raw materials", message=msg_str)



def main():
    # come modello uso la classe food
    m = Tournament()
    # creo controller e passo il modello
    c = Controller(model=m)
    # creo view e passo model e controller
    v = View(model=m, controller=c)
    # passo la view al controller
    c.set_view(v)

    # avvio l'event loop
    v.mainloop()


if __name__ == "__main__":
    main()