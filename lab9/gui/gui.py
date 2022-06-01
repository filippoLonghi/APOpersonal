from hydraulics.hsystem import HSystem
from hydraulics.elements import Source, Tap, Sink, Split
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def show_add_hydraulic_element_window():
    win = Toplevel(root)
    win.title('Add hydraulic element')
    win.minsize(500, 100)
    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)
    l1 = ttk.Label(win, text="Name: ")
    l2 = ttk.Label(win, text="Type: ")
    l1.grid(column=0, row=0, sticky=(N, S, W, E))
    l2.grid(column=0, row=1, sticky=(N, S, W, E))
    name = StringVar()
    type = StringVar()
    name_entry = ttk.Entry(win, textvariable=name)
    surname_entry = ttk.Entry(win, textvariable=type)
    name_entry.grid(column=1, row=0, sticky=(N, S, W, E))
    surname_entry.grid(column=1, row=1, sticky=(N, S, W, E))
    b = ttk.Button(win, text="Add", command=lambda: add_hydraulic_element(win, name.get(), type.get()))
    b.grid(column=0, row=2, columnspan=2, sticky=(N, S, W, E))

def add_hydraulic_element(win, name, type):
    if name != "" and type != "":
        if type == "Source" or type == "source":
            new_elm = h_sys.add_element(Source(name))
            messagebox.showinfo(title="Success!", message="Hydraulic element {} added".format(name))
        if type == "Tap" or type == "tap":
            new_elm = h_sys.add_element(Tap(name))
            messagebox.showinfo(title="Success!", message="Hydraulic element {} added".format(name))
        if type == "Split" or type == "split":
            new_elm = h_sys.add_element(Split(name))
            messagebox.showinfo(title="Success!", message="Hydraulic element {} added".format(name))
        if type == "Sink" or type == "sink":
            new_elm = h_sys.add_element(Sink(name))
            messagebox.showinfo(title="Success!", message="Hydraulic element {} added".format(name))
        else:
            messagebox.showinfo(title="Error!", message="Type {} does not exist".format(type))
        win.destroy()

def get_hydraulic_elements_window():
    messagebox.showinfo(title="Get hydraulic elements", message=f'Elements in the hydraulic system: {[e.get_name() for e in h_sys.get_elements()]}')


h_sys = HSystem()

root = Tk()
root.title("HSystem")
root.minsize(500, 300)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

b1 = ttk.Button(root, text="Add hydraulic element", command=show_add_hydraulic_element_window)
b2 = ttk.Button(root, text="Get hydraulic elements", command=get_hydraulic_elements_window)
b1.grid(column=0, row=0, sticky=(N, S, W, E))
b2.grid(column=0, row=1, sticky=(N, S, W, E))

root.mainloop()
