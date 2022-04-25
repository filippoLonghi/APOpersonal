class Player:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.team = None

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def set_team(self, team):
        self.team = team.get_name()

    def get_team(self):
        return self.team

class Team:

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.players = []

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

    def add_player(self, player):
        self.players.append(f'{player.get_name()} {player.get_surname()}')

    def get_players(self):
        return self.players

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