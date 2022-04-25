class Canestri:

    def __init__(self):
        self._canestri_tot = 0
        self._media = 0
        self._squadre = []
        self._partite_tot = 0

    def add_match(self, squadra, canestri):
        self._canestri_tot += canestri
        self._partite_tot += 1
        self._media = self._canestri_tot / self._partite_tot
        self._squadre.append(squadra)

    def get_average(self):
        return self._media

    def get_teams(self):
        return self._squadre

    def get_summary(self):
        return f'{self._canestri_tot} {self._media}'

def main():
    torneo = Canestri()
    torneo.add_match("Torino", 30)
    torneo.add_match("Palermo", 15)
    media = torneo.get_average()
    print(media)
    squadre = torneo.get_teams()
    print(squadre)
    sommario = torneo.get_summary()
    print(sommario)

main()
