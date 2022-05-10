from Esercizio_2 import *

class Directory(File):

    def __init__(self, directory_name):
        super().__init__(directory_name)
        self._directory_name = directory_name
        self._directory_files = []
        self._info_cartella = ""

    def add_file(self, file):
        self._directory_files.append(file)

    def open_file(self):
        for file in self._directory_files:
            print(file)

    def __repr__(self):
        return self.get_info()

    def get_dim(self):
        return len(self._directory_files)

    def get_info(self):
        self._info_cartella = f'{self._directory_name}:\n'
        for file in self._directory_files:
            self._info_cartella += f'    {file.get_info()}\n'
        return self._info_cartella


def main():
    file1 = File("txt_1 esercizio 2")
    file2 = TextFile("txt_2 esercizio 2")
    tab = [[2,25,102],[200, 15, 55], [0, 255, 78]]
    file3 = BitMap("img_3 esercizio 3", tab)

    cartella1 = Directory("cartella1")
    cartella1.add_file(file1)
    cartella1.add_file(file2)
    cartella1.add_file(file3)
    # print(cartella1.get_info())
    # print(cartella1.get_dim())
    # cartella1.open_file()
    # print(cartella1)

    cartella2 = Directory("cartella 2")
    cartella2.add_file(file1)
    cartella1.add_file(cartella2)

    print(cartella1)

main()