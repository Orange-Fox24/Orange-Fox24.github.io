#Палитра

import tkinter as tk
from tkinter import colorchooser


def choose_color():
    color = colorchooser.askcolor(title="Какой?")
    if color[1]:
        label.config(text=color[1], fg=color[1])


root = tk.Tk()
label = tk.Label(root, text="Выбери какой хочешь цвет)")
label.pack()
button = tk.Button(root, text="тык", command=choose_color)
button.pack()

root.mainloop()
