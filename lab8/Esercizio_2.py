class File:

    def __init__(self, file_name):
        self._file_name = file_name

    def get_name(self):
        return self._file_name

    def get_dim(self):
        return 0

    def get_info(self):
        return f'{self.get_name()}: {self.get_dim()}'

    def __repr__(self):
        return ""


class TextFile(File):

    def __init__(self, file_name):
        super().__init__(file_name)
        self._lines = []

    def add_line(self, line):
        self._lines.append(line)

    def get_dim(self):
        return len(self._lines)

    def __repr__(self):
        text = ""
        for line in self._lines:
            text += line + "\n"
        return text
#       return "\n".join(self.lines)

class BitMap(File):

    def __init__(self, file_name, tab):
        super().__init__(file_name)
        self._tab = tab

    def get_dim(self):
        return len(self._tab[0]), len(self._tab)

    def __repr__(self):
        img = ""
        for i in range(len(self._tab)):
            for j in range(len(self._tab[0])):
                img += f'{hex(self._tab[i][j])} '
            img += "\n"
        return img

# def main():
#     file1 = File("txt_1 esercizio 2")
#     print(file1.get_name())
#     print(file1.get_dim())
#     print(file1.get_info())
#     print(file1)
#
#     file2 = TextFile("txt_2 esercizio 2")
#     file2.add_line("linea1")
#     file2.add_line("linea2")
#     print(file2.get_name())
#     print(file2.get_dim())
#     print(file2.get_info())
#     print(file2)
#
#     tab = [[2,25,102],[200, 15, 55], [0, 255, 78]]
#     file3 = BitMap("img_3 esercizio 3", tab)
#     print(file3.get_name())
#     print(file3.get_dim())
#     print(file3.get_info())
#     print(file3)

def main():
    print("-----------------")
    # creo file semplice
    empty = File("empty.info")
    # testo metodi
    print(empty.get_name())
    print(empty.get_dim())
    print(empty.get_info())
    print(empty)

    print("-----------------")
    # creo file di testo
    txt = TextFile("mytext")
    # popolo file
    txt.add_line("ciao")
    txt.add_line("come")
    txt.add_line("va")
    # metodi ereditati
    print(txt.get_name())
    # metodi overridden
    print(txt.get_dim())
    print(txt)
    # metodo ereditato che usa metodo overridden (dim)
    print(txt.get_info())

    print("----------------")
    # creo file immagine
    table = [
        [201, 198, 56],
        [102, 32, 28]
    ]
    img = BitMap("myimage", table)
    # metodi ereditati
    print(img.get_name())
    # metodi overridden
    print(img.get_dim())
    print(img)
    # metodo ereditato che usa metodo overridden (dim)
    print(img.get_info())

if __name__ == "__main__":
    main()