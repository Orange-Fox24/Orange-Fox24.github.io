import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()

image = PhotoImage(file="C:\\Users\\admin\\Downloads\\Subtract (1).png")
button = tk.Button(root, text="Click here", image=image, compound="left")
button.pack()

root.mainloop()
