import operator


class Player:
    def __init__(self, name: str, nationality: str, age: int) -> None:
        self._name = name
        self._nationality = nationality
        self._age = age
        self._boards = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def add_board(self, board):
        self._boards.append(board)

    def get_board(self):
        return self._boards

    def __repr__(self) -> str:
        return f'{self._name},{self._nationality},{self._age}'


class Tournament:
    def __init__(self, name):
        self._name = name
        self._scores = {} #{Player(): score}

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def add_player_score(self, player, score):
        self._scores[player] = score

    def get_leading_player(self):
        if self._scores != {}:
            match = sorted(self._scores.items(), key = operator.itemgetter(1))
            player = match[-1][0]
            score = match[-1][1]
            return f'{player.name}:{score}'
        else:
            return None