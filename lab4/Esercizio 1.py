from tkinter import *
from tkinter import ttk

def addLine(event):
    canvas.create_line((root.winfo_screenwidth())/2, 0, event.x, event.y, fill="purple")

root = Tk()
root.title("Esercizio1")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), background="yellow")
canvas.bind("<B1-Motion>", addLine)
canvas.grid(column=0, row=0, sticky="nswe")

root.mainloop()