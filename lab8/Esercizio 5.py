from Esercizio_2 import *

class Directory(File):

    def __init__(self, directory_name):
        super().__init__(directory_name)
        self._directory_name = directory_name
        self._directory_files = []

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
        info_cartella = f'{self._directory_name}:\n'
        for file in self._directory_files:
                info_cartella += f'\t{file.get_info()}\n'
        return info_cartella


# def main():
#     file1 = File("txt_1 esercizio 2")
#     file2 = TextFile("txt_2 esercizio 2")
#     tab = [[2,25,102],[200, 15, 55], [0, 255, 78]]
#     file3 = BitMap("img_3 esercizio 3", tab)
#
#     cartella1 = Directory("cartella1")
#     cartella1.add_file(file1)
#     cartella1.add_file(file2)
#     cartella1.add_file(file3)
#     # print(cartella1.get_info())
#     # print(cartella1.get_dim())
#     # cartella1.open_file()
#     # print(cartella1)
#
#     cartella2 = Directory("cartella 2")
#     cartella2.add_file(file1)
#     cartella1.add_file(cartella2)
#
#     print(cartella1)

def main():
    # creo file semplice
    empty = File("empty.info")
    img = BitMap("myimage.bmp", [[1, 2, 3], [4, 255, 6]])
    txt = TextFile("mytext.txt")
    txt.add_line("ciao")
    txt.add_line("come")
    txt.add_line("va")

    # creo cartella
    folder = Directory("my_folder")

    # aggiungo file
    folder.add_file(empty)
    folder.add_file(img)
    folder.add_file(txt)

    # stampo contenuto cartella
    print(folder)

    # stampo contenuto file in cartella
    folder.open_file()

    # creo altra cartella e aggiungo file
    sub_folder = Directory("my_sub_folder")
    sub_folder.add_file(txt)
    sub_folder.add_file(img)
    folder.add_file(sub_folder)
    print(folder)

    # aggiungo se stessa e controllo che non venga stampata
    folder.add_file(folder)

main()