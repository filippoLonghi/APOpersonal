import operator
from typing import List
from diet.nutritional import NutritionalElement, RawMaterial, Product
from diet.elements import Recipe, Menu
from operator import itemgetter


class Food:

    def __init__(self):
        self._raw_materials = {} #{name: RawMaterial}
        self._products = {}
        self._recipes = {}
        self._menus = {}

    # R1
    def define_raw_material(self, name: str, calories: float, proteins: float, carbs: float, fats: float) -> None:
        if name not in self._raw_materials:
            self._raw_materials[name] = RawMaterial(name, calories, proteins, carbs, fats)
        else:
            raise ValueError("Materia prima già definita")

    @property
    def raw_materials(self) -> List[NutritionalElement]:
        raw_materials = [elm[1] for elm in sorted(self._raw_materials.items(), key=operator.itemgetter(0))]
        return raw_materials

    def get_raw_material(self, name: str) -> NutritionalElement:
        return self._raw_materials[name]

    # R2
    def define_product(self, name: str, calories: float, proteins: float, carbs: float, fats: float) -> None:
        if name not in self._products:
            self._products[name] = Product(name, calories, proteins, carbs, fats)
        else:
            raise ValueError("Materia prima già definita")

    @property
    def products(self) -> List[NutritionalElement]:
        products = [elm[1] for elm in sorted(self._products.items(), key=operator.itemgetter(0))]
        return products

    def get_product(self, name: str) -> NutritionalElement:
        return self._products[name]

    # R3
    def create_recipe(self, name: str) -> Recipe:
        self._recipes[name] = Recipe(name, self)
        return self._recipes[name]

    @property
    def recipes(self) -> List[Recipe]:
        recipes = [elm[1] for elm in sorted(self._recipes.items(), key=operator.itemgetter(0))]
        return recipes

    def get_recipe(self, name: str) -> Recipe:
        return self._recipes[name]

    # R5
    def create_menu(self, name: str) -> Menu:
        self._menus[name] = Menu(name, self)
        return self._menus[name]




