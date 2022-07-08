from abc import ABC, abstractmethod
from math import sqrt

class Shape(ABC):

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Triangle(Shape):

    def __init__(self, name, base_length, *side_length):
        super().__init__(name)
        self._base_length = base_length
        self._side_length = side_length

    def get_area(self):
        area = 0
        if len(self._side_length) == 0:
            area = (self._base_length*self._base_length)/2
        if len(self._side_length) == 1:
            p = (self._base_length + self._side_length[0] + self._side_length[0])/2
            area = sqrt(p*(p-self._base_length)*(p-self._side_length[0])*(p-self._side_length[0]))
        if len(self._side_length) == 2:
            p = (self._base_length + self._side_length[0] + self._side_length[1])/2
            area = sqrt(p*(p-self._base_length)*(p-self._side_length[0])*(p-self._side_length[1]))
        return area

    def get_perimeter(self):
        perimeter = 0
        if len(self._side_length) == 0:
            perimeter = self._base_length*3
        if len(self._side_length) == 1:
            perimeter = self._base_length + self._side_length[0]*2
        if len(self._side_length) == 2:
            perimeter = self._base_length + self._side_length[0] + self._side_length[1]
        return perimeter

class Square(Shape):

    def __init__(self, name, side_length):
        super().__init__(name)
        self._side_length = side_length

    def get_area(self):
        return self._side_length * self._side_length

    def get_perimeter(self):
        return self._side_length * 4

# def main():
#     triangolo = Triangle("triangolo1",5, 6, 7)
#     print(triangolo.get_area())
#     print(triangolo.get_perimeter())
#
#     quadrato = Square("quadrato1", 5)
#     print(quadrato.get_area())
#     print(quadrato.get_perimeter())

def main():
    # controllo che classe astratta non sia istanziabile
    try:
        s = Shape()
    except TypeError as e:
        print("Error: {}".format(e))

    # creo triangolo e testo override
    t = Triangle("Triangolo Scaleno", 2, 3, 4)
    print(t.get_name())
    print("\t - Perimetro: {:.3f}".format(t.get_perimeter()))
    print("\t - Area: {:.3f}".format(t.get_area()))

    # creo triangolo e testo override
    t = Triangle("Triangolo Isoscele", 2, 3)
    print(t.get_name())
    print("\t - Perimetro: {:.3f}".format(t.get_perimeter()))
    print("\t - Area: {:.3f}".format(t.get_area()))

    # creo triangolo e testo override
    t = Triangle("Triangolo Equilatero", 3)
    print(t.get_name())
    print("\t - Perimetro: {:.3f}".format(t.get_perimeter()))
    print("\t - Area: {:.3f}".format(t.get_area()))

    # creo rettangolo e testo override
    s = Square("Un Quadrato", 5)
    print(s.get_name())
    print("\t - Perimetro: {:.3f}".format(s.get_perimeter()))
    print("\t - Area: {:.3f}".format(s.get_area()))

main()