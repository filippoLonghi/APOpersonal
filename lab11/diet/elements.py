from diet.nutritional import NutritionalElement

def _call_ingredients_data(data, obj):
    if data == "calories":
        return obj.calories
    if data == "proteins":
        return obj.proteins
    if data == "carbs":
        return obj.carbs
    if data == "fats":
        return obj.fats

def _proportions_per100g(data, diz):
    tot_quantity = 0
    for elm in diz:
        tot_quantity += diz[elm]
    per100g = (100 * _proportions_perxg(data, diz)) / tot_quantity
    return per100g

def _proportions_perxg(data, diz):
    perxg = 0
    for elm in diz:
        perxg += (diz[elm] * _call_ingredients_data(data, elm)) / 100
    return perxg

def _products_data(data, list):
    tot = 0
    for elm in list:
        tot += _call_ingredients_data(data, elm[0])
    return tot

class Recipe(NutritionalElement):

    def __init__(self, name, food_obj):
        self._ingredients = {} #{RawMaterial: quantity}
        self._name = name
        self._food_obj = food_obj

    def add_ingredient(self, raw_material_name: str, quantity: float) -> "Recipe":
        self._ingredients[self._food_obj.get_raw_material(raw_material_name)] = quantity
        return self

    @property
    def name(self) -> str:
        return self._name

    @property
    def calories(self) -> float:
        return _proportions_per100g("calories", self._ingredients)

    @property
    def proteins(self) -> float:
        return _proportions_per100g("proteins", self._ingredients)

    @property
    def carbs(self) -> float:
        return _proportions_per100g("carbs", self._ingredients)

    @property
    def fats(self) -> float:
        return _proportions_per100g("fats", self._ingredients)

    @property
    def per100g(self) -> bool:
        return True

    def __repr__(self) -> str:
        recipe = [f'{elm.name} {self._ingredients[elm]:.1f}' for elm in self._ingredients]
        return "\n".join(recipe)



class Menu(NutritionalElement):

    def __init__(self, name, food_obj):
        self._name = name
        self._food_obj = food_obj
        self._recipes = {}
        self._products = []

    def add_recipe(self, recipe_name: str, quantity: float) -> "Menu":
        self._recipes[self._food_obj.get_recipe(recipe_name)] = quantity
        return self

    def add_product(self, product_name: str) -> "Menu":
        self._products.append([self._food_obj.get_product(product_name)])
        return self

    @property
    def name(self) -> str:
        return self._name

    @property
    def calories(self) -> float:
        return _proportions_perxg("calories", self._recipes) + _products_data("calories", self._products)

    @property
    def proteins(self) -> float:
        return _proportions_perxg("proteins", self._recipes) + _products_data("proteins", self._products)

    @property
    def carbs(self) -> float:
        return _proportions_perxg("carbs", self._recipes) + _products_data("carbs", self._products)

    @property
    def fats(self) -> float:
        return _proportions_perxg("fats", self._recipes) + _products_data("fats", self._products)

    @property
    def per100g(self) -> bool:
        return False
