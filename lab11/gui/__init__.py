from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from diet.food import Food

class View(Tk):

    def __init__(self, model, controller):
        super().__init__()
        self.model = model
        self.controller = controller

        self.title("Food")
        self.minsize(500, 300)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        b1 = ttk.Button(self, text="Add raw ingredient", command=self.controller.show_add_raw_ingredient_window)
        b2 = ttk.Button(self, text="Get raw ingredient", command=self.controller.show_get_raw_ingredient_window)
        b1.grid(column=0, row=0, sticky=(N, S, W, E))
        b2.grid(column=0, row=1, sticky=(N, S, W, E))

    def show_add_raw_ingredient_window(self):
        win = Toplevel(self)
        win.title('Add raw ingredient')
        win.minsize(500, 100)

        win.columnconfigure(0, weight=1)
        win.columnconfigure(1, weight=1)
        win.rowconfigure(0, weight=1)
        win.rowconfigure(1, weight=1)
        win.rowconfigure(2, weight=1)
        win.rowconfigure(3, weight=1)
        win.rowconfigure(4, weight=1)
        win.rowconfigure(5, weight=1)

        l1 = ttk.Label(win, text="Name: ")
        l2 = ttk.Label(win, text="Calories: ")
        l3 = ttk.Label(win, text="Proteins: ")
        l4 = ttk.Label(win, text="Carbs: ")
        l5 = ttk.Label(win, text="Fats: ")
        l1.grid(column=0, row=0, sticky=(N, S, W, E))
        l2.grid(column=0, row=1, sticky=(N, S, W, E))
        l3.grid(column=0, row=2, sticky=(N, S, W, E))
        l4.grid(column=0, row=3, sticky=(N, S, W, E))
        l5.grid(column=0, row=4, sticky=(N, S, W, E))

        name = StringVar()
        calories = StringVar()
        proteins = StringVar()
        carbs = StringVar()
        fats = StringVar()
        name_entry = ttk.Entry(win, textvariable=name)
        calories_entry = ttk.Entry(win, textvariable=calories)
        proteins_entry = ttk.Entry(win, textvariable=proteins)
        carbs_entry = ttk.Entry(win, textvariable=carbs)
        fats_entry = ttk.Entry(win, textvariable=fats)
        name_entry.grid(column=1, row=0, sticky=(N, S, W, E))
        calories_entry.grid(column=1, row=1, sticky=(N, S, W, E))
        proteins_entry.grid(column=1, row=2, sticky=(N, S, W, E))
        carbs_entry.grid(column=1, row=3, sticky=(N, S, W, E))
        fats_entry.grid(column=1, row=4, sticky=(N, S, W, E))

        b = ttk.Button(win, text="Aggiungi", command=lambda: self.controller.add_raw_ingredient(win, name.get(), calories.get(), proteins.get(), carbs.get(), fats.get()))
        b.grid(column=0, row=5, columnspan=2, sticky=(N, S, W, E))

    def error_message(self, win, name):
        messagebox.showinfo(title="Existing raw material!", message=f"{name} is alredy included in the list of raw materials")
        win.destroy()

    def show_get_raw_ingredient_window(self):
        elm_str = "\n".join([f'{elm.name}' for elm in self.model.food.raw_materials])
        messagebox.showinfo(title="Raw ingredients", message=elm_str)


class Model:

    def __init__(self):
        self._food = Food()

    def add_raw_ingredient(self, name, calories, proteins, carbs, fats):
        raw_ingredient = self._food.define_raw_material(name, float(calories), float(proteins), float(carbs), float(fats))

    @property
    def food(self):
        return self._food


class Controller:

    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        self.view = view

    def show_add_raw_ingredient_window(self):
        self.view.show_add_raw_ingredient_window()

    def add_raw_ingredient(self, win, name, calories, proteins, carbs, fats):
        try:
            self.model.add_raw_ingredient(name, calories, proteins, carbs, fats)
        except ValueError:
            self.view.error_message(win, name)

    def show_get_raw_ingredient_window(self):
        self.view.show_get_raw_ingredient_window()


m = Model()
c = Controller(m)
v = View(m, c)
c.set_view(v)
v.mainloop()

