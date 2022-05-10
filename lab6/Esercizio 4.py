class Matrix:

    def __init__(self, tabella):
        self._tabella = tabella

    def get_numero_righe(self):
        return len(self._tabella)

    def get_numero_colonne(self):
        return len(self._tabella[0])

    def __add__(self, other): #other è un'istanza di Matrix (una matrice 2x2)
        tabella = []
        for i in range(self.get_numero_righe()):
            riga = []
            for j in range(self.get_numero_colonne()):
                ris = self._tabella[i][j] + other._tabella[i][j]
                riga.append(ris)
            tabella.append(riga)
        return Matrix(tabella) #tabella è una matrice 2x2 --> tabella = self.tabella + other

    def __sub__(self, other):
        tabella = []
        for i in range(self.get_numero_righe()):
            riga = []
            for j in range(self.get_numero_colonne()):
                ris = self._tabella[i][j] - other._tabella[i][j]
                riga.append(ris)
            tabella.append(riga)
        return Matrix(tabella)

    def __mul__(self, other):
        tabella = [[0]*self.get_numero_colonne() for i in range(self.get_numero_righe())]
        for i in range(self.get_numero_righe()):
            for j in range(other.get_numero_colonne()):
                for k in range(self.get_numero_colonne()):
                    tabella[i][j] += self._tabella[i][k] * other._tabella[k][j]
        return Matrix(tabella) #tabella è una lista di due elementi (dovrebbe essere un vettore colonna)

    def __eq__(self, other):
        uguali = True
        # if self.get_numero_righe() != other.get_numero_righe or self.get_numero_colonne() != other.get_numero_colonne():
        #     uguali = False
        for i in range(self.get_numero_righe()):
            for j in range(self.get_numero_colonne()):
                if uguali and self._tabella[i][j] != other._tabella[i][j]:
                    uguali = False
        return uguali

    def __repr__(self):
        tabella = ""
        for i in range(self.get_numero_righe()):
                for j in range(self.get_numero_colonne()):
                    tabella += f'{self._tabella[i][j]:3} '
                tabella += "\n"
        return tabella


def main():
    matrice1 = Matrix([[1, 2], [3, 4]])
    matrice2 = Matrix([[2, 6], [1, 4]])
    print(matrice1 + matrice2)
    print(matrice1 - matrice2)
    print(matrice1 * matrice2)
    print(matrice1 == matrice2)
    print(matrice1)
    print(matrice2)
    print(matrice1.get_numero_colonne())
    print(matrice1.get_numero_righe())

main()