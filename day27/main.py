import tkinter

window = tkinter.Tk()
window.title("My Frist GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=30)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)


my_label["text"] = "New Text"
my_label.config(text="New text")
my_label.config(padx=20, pady=20)


click = 0
# Button


def button_clicked():
    print("I Got Clicked.")
    global click
    click += 1
    texto = input.get()
    if texto:
        my_label.config(text=texto)
    else:
        my_label["text"] = f"Button got clicked {click} times."


button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)


button2 = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
button2.grid(column=2, row=0)

# Entry

input = tkinter.Entry()
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
