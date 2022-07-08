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

    def is_dead(self) -> bool:
        return not self._life_points>0

    def __repr__(self) -> str:
        return f"{self._name} {self._attack} {self._life_points} {self._mana_cost}"

    @staticmethod
    def fight(card1: "Card", card2: "Card") -> None:
        card1._life_points -= card2._attack
        card2._life_points -= card1._attack


class Player:
    def __init__(self, name: str) -> None:
        self._name = name
        self._field = {}
        self._hand = {}
        self._mana = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def field(self) -> List[Card]:
        return list(self._field.values())

    @property
    def hand(self) -> List[Card]:
        return list(self._hand.values())

    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, mana) -> None:
        self._mana = mana

    def draw(self, card: Card) -> None:
        self._hand[card.name] = card

    def play(self, card_name: str) -> None:
        card = self._hand[card_name]
        if card.mana_cost>self._mana:
            raise GameException("Mana non sufficenti")
        self._mana -= card.mana_cost
        self._field[card_name] = card
        self._hand.pop(card_name)

    def find_best_two(self) -> List[str]:
        first = second = None

        #-PRIMA-#
        mana_costs = []
        for card in self.hand:
            mana_costs.append(card.mana_cost)
        min_mana_cost = min(mana_costs)

        max_attack = 0
        for card in self.hand:
            if (self.mana - card.mana_cost) >= min_mana_cost:
                if card.attack > max_attack:
                    max_attack = card.attack
                    first = card

        #-SECONDA-#
        if first != None:
            max_attack = 0
            for card in self.hand:
                if card.mana_cost <= (self.mana - first.mana_cost):
                    if card.name != first:
                        if card.attack > max_attack:
                            max_attack = card.attack
                            second = card

        if first==None or second==None:
            return []

        return [first.name, second.name]


class Tournament:
    def __init__(self) -> None:
        self._players = {}
        self._cards = {}
        self._uses = {}

    def add_player(self, player) -> None:
        if player.name in self._players:
            raise GameException("Player con lo stesso nome già inserito")
        self._players[player.name] = player
        self._uses[player.name] = []

    def add_card(self, card) -> None:
        self._cards[card.name] = card

    def player_uses_card(self, player_name, card_name) -> None:
        self._uses[player_name].append(card_name)

    def get_cards_of_player(self, player_name, sort_res=False) -> List[Card]:
        cards = []
        if sort_res:
            # ordino la lista di chiavi (nomi delle carte)
            sorted_card_names = sorted(self._uses[player_name])
            card_names = sorted_card_names
        else:
            # recupero la lista di chiavi (nomi delle carte)
            card_names = self._uses[player_name]
        # creo la lista di carte
        for card_name in card_names:
            cards.append(self._cards[card_name])
        return cards

    def get_players_of_card(self, card_name) -> List[str]:
        players = []
        for player_name in self._uses.keys():
            if card_name in self._uses[player_name]:
                players.append(player_name)
        return players