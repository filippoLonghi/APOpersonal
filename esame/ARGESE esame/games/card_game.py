from typing import List


class GameException(Exception):
    pass


class Card:
    def __init__(self, name: str, attack: int, life_points: int, mana_cost: int) -> None:
        self._name = name
        self._attack = attack
        self._life_points = life_points
        self._mana_cost = mana_cost

    @property
    def name(self) -> str:
        return self._name

    @property
    def attack(self) -> int:
        return self._attack

    @property
    def life_points(self) -> int:
        return self._life_points

    @property
    def mana_cost(self) -> int:
        return self._mana_cost

    @attack.setter
    def attack(self, new_attack):
        self._attack = new_attack

    @life_points.setter
    def life_points(self, new_points):
        self._life_points = new_points


    def is_dead(self) -> bool:
        if self._life_points > 0:
            return False
        else:
            return True

    def __repr__(self) -> str:
        return self._name + " " + str(self._attack) + " " + str(self._life_points) + " " + str(self._mana_cost)

    @staticmethod
    def fight(card1: "Card", card2: "Card") -> None:
        attacco_1 = card1.attack
        attacco_2 = card2.attack
        vita_1 = card1.life_points - attacco_2
        vita_2 = card2.life_points - attacco_1
        card1.life_points = vita_1
        card2.life_points = vita_2




class Player:
    def __init__(self, name: str) -> None:
        self._name = name
        self._field = []
        self._hand = []
        self._mana = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def field(self) -> List[Card]:
        return self._field

    @property
    def hand(self) -> List[Card]:
        return self._hand

    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, mana) -> None:
        self._mana = mana

    def draw(self, card: Card) -> None:
        self._hand.append(card)

    def play(self, card_name: str) -> None:
        if self.controllo_carte_uguali:
            for card in self._hand:
                if card.name == card_name:
                    self._field.append(card)
                    self._hand.remove(card)
                    costo_da_scalare = card.mana_cost
                    self._mana = self._mana - costo_da_scalare
                    if self._mana <= 0:
                        raise GameException


    def controllo_carte_uguali(self):
        lista_nomi = []
        for card in self._hand:
            lista_nomi.append(card.name)
        i = 0
        for card in lista_nomi:
            i += 1
            if i <= len(lista_nomi):
                for i in range(i, len(lista_nomi)):
                    if card == lista_nomi[i]:
                        raise GameException
            else:
                return True

    def find_best_two(self) -> List[str]:
        self._copy_hand = list(self._hand)
        self._lista_migliori = self.best_two(self._copy_hand, self.mana)
        lista_migliori_nomi = []
        for card in self._lista_migliori:
            lista_migliori_nomi.append(card.name)
        return lista_migliori_nomi

    def best_two(self, mazzo, mana):
        best_two = []
        max = 0
        max_card = None
        for card in mazzo:
            if card.attack > max:
                max_card = card
                mazzo.remove(card)
        best_two.append(max_card)
        max = 0
        for card in mazzo:
            if card.attack > max:
                max_card = card
                mazzo.remove(card)
        best_two.append(max_card)

        somma = best_two[0].attack + best_two[1].attack
        if somma <= mana:
            return best_two
        else:
            if best_two[0] in mazzo:
                mazzo.remove(best_two[0])
                if self.best_two(mazzo, mana):
                    return best_two
            else:
                return []


class Tournament:
    def __init__(self) -> None:
        self._partecipanti = {}
        self._mazzo = {}

    def add_player(self, player) -> None:
        if player not in self._partecipanti:
            self._partecipanti[player] = []
        else:
            raise GameException

    def add_card(self, card) -> None:
        if card not in self._mazzo:
            self._mazzo[card] = []
        else:
            raise GameException

    def player_uses_card(self, player_name, card_name) -> None:
        for player in self._partecipanti:
            if player.name == player_name:
                for card in self._mazzo:
                    if card.name == card_name:
                        self._mazzo[card].append(player)
                        self._partecipanti[player].append(card)

    def get_cards_of_player(self, player_name, sort_res=False) -> List[Card]:
        if sort_res == False:
            for player in self._partecipanti:
                if player.name == player_name:
                    return self._partecipanti[player]
        else:
            for player in self._partecipanti:
                if player.name == player_name:
                    lista = self._partecipanti[player]
            lista = sorted(lista, key=lambda c:c.name)
            return lista


    def get_players_of_card(self, card_name) -> List[str]:
        lista = []
        for card in self._mazzo:
            if card.name == card_name:
                for player in self._mazzo[card]:
                    lista.append(player.name)
        return lista

