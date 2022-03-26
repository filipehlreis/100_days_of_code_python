import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
# Place this at the end (to avoid any conflicts/errors)
from PIL import Image, ImageTk

window = tk.Tk()
a = Tk()


def openimgfile():
    currdir = os.getcwd()
    name = filedialog.askopenfile(initialdir=currdir, title="Select a Image", filetype=(
        ("PNG", "*.png"), ("JPEG", "*.jpg;.*jpeg"), ("All files", "*.*")))
    print(name.name)


a.title("Pattern Matching")
a.minsize(200, 200)
button1 = Button(text="Open file", width=10,
                 height=10, command=openimgfile).pack()

a.mainloop()
