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

class BitMap(File):

    def __init__(self, file_name, tab):
        super().__init__(file_name)
        self._tab = tab

    def get_dim(self):
        return len(self._tab), len(self._tab[0])

    def __repr__(self):
        img = ""
        for i in range(len(self._tab)):
            for j in range(len(self._tab)):
                img += f'{hex(self._tab[i][j])} '
        return img

def main():
    file1 = File("txt_1 esercizio 2")
    print(file1.get_name())
    print(file1.get_dim())
    print(file1.get_info())
    print(file1)

    file2 = TextFile("txt_2 esercizio 2")
    file2.add_line("linea1")
    file2.add_line("linea2")
    print(file2.get_name())
    print(file2.get_dim())
    print(file2.get_info())
    print(file2)

    tab = [[2,25,102],[200, 15, 55], [0, 255, 78]]
    file3 = BitMap("img_3 esercizio 3", tab)
    print(file3.get_name())
    print(file3.get_dim())
    print(file3.get_info())
    print(file3)

if __name__ == "__main__":
    main()