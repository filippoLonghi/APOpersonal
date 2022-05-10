class Player:

    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age
        self._team = None

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_age(self):
        return self._age

    def set_team(self, team):
        self._team = team.get_name()

    def get_team(self):
        return self._team

class Team:

    def __init__(self, name, city):
        self._name = name
        self._city = city
        self._players = []

    def get_name(self):
        return self._name

    def get_city(self):
        return self._city

    def add_player(self, player):
        self._players.append(f'{player.get_name()} {player.get_surname()}')

    def get_players(self):
        return self._players

def main():
    primo_player = Player("Giacomo", "Berrettini", 22)
    secondo_player = Player("Umberto", "Galimberti", 32)
    terzo_player = Player("Cesare", "Nosiglia", 76)
    primo_team = Team("HypeSquad2", "Benevento")
    secondo_team = Team ("PazziSgravati", "Torino")
    primo_player.set_team(primo_team)
    secondo_player.set_team(primo_team)
    terzo_player.set_team(secondo_team)
    print(primo_player.get_team()) #HypeSquad2
    print(secondo_player.get_team()) #HypeSquad2
    print(terzo_player.get_team()) #PazziSgravati
    primo_team.add_player(primo_player)
    primo_team.add_player(secondo_player)
    secondo_team.add_player(terzo_player)
    print(primo_team.get_players())
    print(secondo_team.get_players())

main()