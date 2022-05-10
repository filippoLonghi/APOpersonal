from Esercizio_2 import *

class Directory:

    def __init__(self, directory_name):
        self._directory_name = directory_name
        self._directory_files = []

    def add_file(self, file):
        self._directory_files.append(file)

    def open_file(self):
        for file in self._directory_files:
            print(file)

    def __repr__(self):
        info_cartella = f'{self._directory_name}:\n'
        for file in self._directory_files:
            info_cartella += f'    {file.get_info()}\n'
        return info_cartella

def main():
    file1 = File("txt_1 esercizio 2")
    file2 = TextFile("txt_2 esercizio 2")
    tab = [[2,25,102],[200, 15, 55], [0, 255, 78]]
    file3 = BitMap("txt_3 esercizio 3", tab)

    cartella = Directory("cartella1")
    cartella.add_file(file1)
    cartella.add_file(file2)
    cartella.add_file(file3)
    cartella.open_file()
    print(cartella)

main()