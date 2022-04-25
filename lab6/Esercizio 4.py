class Matrix:

    def __init__(self, tabella):
        self.tabella = tabella

    def get_numero_righe(self):
        return len(self.tabella)

    def get_numero_colonne(self):
        return len(self.tabella[0])

    def __add__(self, other): #other è un'istanza di Matrix (una matrice 2x2)
        tabella = []
        for i in range(2):
            riga = []
            for j in range(2):
                ris = self.tabella[i][j] + other.tabella[i][j]
                riga.append(ris)
            tabella.append(riga)
        return Matrix(tabella) #tabella è una matrice 2x2 --> tabella = self.tabella + other

    def __sub__(self, other):
        tabella = []
        for i in range(2):
            riga = []
            for j in range(2):
                ris = self.tabella[i][j] - other.tabella[i][j]
                riga.append(ris)
            tabella.append(riga)
        return Matrix(tabella)

    def __mul__(self, other):
        tabella = []
        for i in range(2):
            riga = []
            tot = 0
            for j in range(2):
                ris = self.tabella[i][j] * other.tabella[j][i]
                tot += ris
            riga.append(tot)
            tabella.append(riga)
        return Matrix(tabella) #tabella è una lista di due elementi (dovrebbe essere un vettore colonna)

    def __eq__(self, other):
        uguali = True
        for i in range(2):
            for j in range(2):
                if uguali and self.tabella[i][j] != other.tabella[i][j]:
                    uguali = False
        return uguali

    def __repr__(self):
        tabella = ""
        if len(self.tabella[0]) == 2:
                for i in range(2):
                    for j in range(2):
                        tabella += str(self.tabella[i][j]) + " "
                    tabella += "\n"
        else:
            tabella = str(self.tabella[0][0]) + "\n" + str(self.tabella[1][0])
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