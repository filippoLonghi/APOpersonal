from university import *
from university.uni import University

from tkinter import *
from tkinter import ttk

uni = University("PoliTo")
matricola_studente = 10000
students = {}

def insert_student():
    global matricola_studente
    students[matricola_studente] = uni.add_student(name.get(), surname.get())
    matricola_studente += 1
    name.set("")
    surname.set("")

def info_student():
    informazioni_text.delete(1.0,12.0)
    informazioni_text.insert(END,uni.get_student_info(int(matricola.get())))
    matricola.set("")

root = Tk()
root.title("lab7")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

frame1 = ttk.Frame(root, borderwidth=5, relief="ridge")
frame1.grid(column=0, row=0, sticky="nswe")
frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)
frame1.columnconfigure(2, weight=1)
frame1.rowconfigure(0, weight=1)
frame1.rowconfigure(1, weight=1)

name = StringVar()
surname = StringVar()

student_name_entry = Entry(frame1, textvariable=name)
student_name_entry.grid(column=1, row=0, sticky="nswe")

student_surname_entry = Entry(frame1, textvariable=surname)
student_surname_entry.grid(column=1, row=1, sticky="nswe")

name_label = ttk.Label(frame1, text="Name: ")
name_label.grid(column=0, row=0, sticky="nswe")

surname_label = ttk.Label(frame1, text="Surname: ")
surname_label.grid(column=0, row=1, sticky="nswe")

insert_button = ttk.Button(frame1, text="Aggiungi studente", command=insert_student)
insert_button.grid(column=2, row=0, rowspan=2, sticky="nswe")

frame2 = ttk.Frame(root, borderwidth=5, relief="ridge")
frame2.grid(column=0, row=1, sticky="nswe")
frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(0, weight=1)
frame2.columnconfigure(1, weight=1)
frame2.rowconfigure(1, weight=1)

matricola = StringVar()

matricola_entry = Entry(frame2, textvariable=matricola)
matricola_entry.grid(column=1, row=0, sticky="nswe")

matricola_label = ttk.Label(frame2, text="Matricola: ")
matricola_label.grid(column=0, row=0, sticky="nswe")

informazioni_text = Text(frame2, height=1, width=1)
informazioni_text.grid(column=0, row=1, columnspan=3, sticky="nswe")

matricola_button = ttk.Button(frame2, text="Richiedi informazioni\nsullo studente", command=info_student)
matricola_button.grid(column=2, row=0, rowspan=2, sticky="nswe")

root.mainloop()