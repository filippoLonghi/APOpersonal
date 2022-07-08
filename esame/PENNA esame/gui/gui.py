from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from games.card_game import Card

class View(Tk):

    def __init__(self, model, controller):
        super().__init__()
        self._model = model
        self._controller = controller

        self.title("Card Game")

        # Labels
        ttk.Label(self, text="Card Game").grid(column=0, row=0, columnspan=4, padx=5, pady=5)
        ttk.Label(self, text="Card name").grid(column=0, row=1)
        ttk.Label(self, text="Card attack").grid(column=0, row=2)

        # StringVars
        name = StringVar()
        attack = StringVar()
        life_points = 10
        mana_cost = 5

        # Entries
        ttk.Entry(self, textvariable=name).grid(column=1, row=1)
        ttk.Entry(self, textvariable=attack).grid(column=1, row=2)

        # Buttons
        b1 = ttk.Button(self, text="Add", command=lambda: self._controller.add(name.get(), int(attack.get()), life_points, mana_cost))
        b1.grid(column=0, row=5, padx=5, pady=5)
        b2 = ttk.Button(self, text="View", command=lambda: self._controller.view())
        b2.grid(column=1, row=5, padx=5, pady=5)


    # metodo che permette di mostrare un messaggio di info o di errore
    def show_message(self, title, message):
        messagebox.showinfo(title, message)


class Controller:

    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    def add(self, name, attack, life_points, mana_cost):
        self._model.add_card(name, attack, life_points, mana_cost)
        self._view.show_message("Fatto", "Carta aggiunta correttamente")

    def view(self):
        cards = self._model.cards
        ris = ""
        for c in cards:
            ris += f"{c.name} -> attack: {c.attack}, life points: {c.life_points}, mana cost: {c.mana_cost}\n"
        self._view.show_message("Carte create", ris)


class Model():
    def __init__(self):
        self._cards = []

    def add_card(self, name, attack, life_points, mana_cost):
        card = Card(name, attack, life_points, mana_cost)
        self._cards.append(card)

    @property
    def cards(self):
        return self._cards


def main():
    model = Model()
    controller = Controller(model)
    view = View(model, controller)
    controller.set_view(view)
    view.mainloop()

main()