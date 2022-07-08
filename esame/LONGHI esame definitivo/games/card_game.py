from typing import List


class GameException(Exception):
    pass


class Card:
    def __init__(self, name: str, attack: int, life_points: int, mana_cost: int) -> None:
        self._name = name
        self._attack = attack
        self._life_points = life_points
        self._mana_cost = mana_cost
        self._tournament_players = []

    def set_tournament_players(self, player):
        self._tournament_players.append(player)

    def get_tournament_players(self):
        return self._tournament_players

    def __lt__(self, other):
        return self.name < other.name

    @property
    def name(self) -> str:
        return self._name

    @property
    def attack(self) -> int:
        return self._attack

    @property
    def life_points(self) -> int:
        return self._life_points

    @life_points.setter
    def life_points(self, life_points):
        self._life_points = life_points

    @property
    def mana_cost(self) -> int:
        return self._mana_cost

    def is_dead(self) -> bool:
        return self._life_points <= 0

    def __repr__(self) -> str:
        return f'{self._name} {self._attack} {self._life_points} {self._mana_cost}'

    @staticmethod
    def fight(card1: "Card", card2: "Card") -> None:
        card1._life_points = card1._life_points - card2._attack
        card2._life_points = card2._life_points - card1._attack


class Player:
    def __init__(self, name: str) -> None:
        self._name = name
        self._field = [] #[Card(), Card(), ...]
        self._hand = {} #{name:Card()}
        self._mana = 0
        self._tournament_cards = []

    def set_tournament_cards(self, card):
        self._tournament_cards.append(card)

    def get_tournament_cards(self):
        return self._tournament_cards

    @property
    def name(self) -> str:
        return self._name

    @property
    def field(self) -> List[Card]:
        return self._field

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
        if self._mana - self._hand[card_name]._mana_cost < 0:
            raise GameException("Mana troppo basso")
        self._field.append(self._hand[card_name])
        self._mana = self._mana - self._hand[card_name]._mana_cost
        self._hand.pop(card_name)


    # def find_best_two(self) -> List[str]:
    #     cards = sorted(self.hand, key = lambda c: c.attack, reverse = True)
    #     for c1 in cards:
    #         for c2 in cards:
    #             if c1 != c2:
    #                 if (c1.mana_cost + c2.mana_cost) <= self.mana:
    #                     return [c1.name, c2.name]
    #     return []


    #migliroe
    # def find_best_two(self) -> List[str]:
    #     best_cards = []
    #     if self._find_card(best_cards, self._mana):
    #         return best_cards
    #     else:
    #         return []
    #
    # def _find_card(self, best_cards, current_mana):
    #     for first_card in sorted(self.hand, key=lambda c: c.attack, reverse=True):
    #         for second_card in sorted(self.hand, key=lambda c: c.attack, reverse=True):
    #             if first_card != second_card and (first_card.mana_cost + second_card.mana_cost) <= current_mana: return best_cards.extend([first_card.name, second_card.name]), True


    def find_best_two(self):
        best_cards = []
        if self._find_card(best_cards, self._mana, dict(self._hand)):
            return best_cards
        else:
            return []

    def _find_card(self, best_cards, current_mana, current_hand):
        if current_hand == {}:
            done = True
            return True
        hand_mana_cost = 0
        for elm in best_cards:
            hand_mana_cost += elm._mana_cost
        max = 0
        max_card_name = ""
        for k, v in current_hand.items():
            if v.attack > max:
                max = v.attack
                max_card_name = k
        for k, v in self._hand.items():
            if v.attack == max and hand_mana_cost + v._mana_cost < current_mana:
                best_cards.append(v)
                current_hand.pop(k)
                if self._find_card(best_cards, current_mana - v._mana_cost, current_hand):
                    return True
        current_hand.pop(max_card_name)
        self._find_card(best_cards, current_mana, current_hand)






    # def find_best_two(self) -> List[str]:
    #     best_cards = []
    #     potential_cards = {}
    #     for k, v in self._hand.items():
    #         for c, h in self._hand.items():
    #             if v._mana_cost + h._mana_cost <= self._mana:
    #                 potential_cards[c] = h
    #     if self._find_card(best_cards, self._mana, potential_cards):
    #         return best_cards
    #     else:
    #         return []
    #
    #
    #
    # def _find_card(self, best_cards, current_mana, current_hand):
    #     if current_hand == {}:
    #         return True
    #     max = 0
    #     max_card_name = ""
    #     attack_points = []
    #     for k, v in current_hand.items():
    #         attack_points.append(v.attack)
    #         if v.attack > max:
    #             max = v.attack
    #             max_card_name = k
    #     sec_max = sorted(attack_points)[-2] if len(attack_points) >= 2 else 0
    #     for k, v in current_hand.items():
    #         if v.attack == max and current_mana - v._mana_cost - sec_max >= 0:
    #             best_cards.append(k)
    #             current_hand.pop(k)
    #             if self._find_card(best_cards, current_mana - v._mana_cost - sec_max, current_hand):
    #                 return True
    #     current_hand.pop(max_card_name)
    #     self._find_card(best_cards, current_mana, current_hand)


class Tournament:
    def __init__(self) -> None:
        self._players = {}
        self._cards = {}

    def add_player(self, player) -> None:
        if player.name in self._players:
            raise GameException("Giocatore già aggiunto")
        self._players[player.name] = player

    def add_card(self, card) -> None:
        self._cards[card.name] = card

    def get_cards(self):
        return list(self._cards.values())

    def player_uses_card(self, player_name, card_name) -> None:
        player = self._players[player_name]
        card = self._cards[card_name]
        player.set_tournament_cards(card)
        card.set_tournament_players(player)

    def get_cards_of_player(self, player_name, sort_res=False) -> List[Card]:
        player = self._players[player_name]
        if sort_res == False:
            return player.get_tournament_cards()
        else:
            return sorted(player.get_tournament_cards())

    def get_players_of_card(self, card_name) -> List[str]:
        card = self._cards[card_name]
        players_str = []
        players_obj = card.get_tournament_players()
        for elm in players_obj:
            players_str.append(elm.name)
        return players_str

