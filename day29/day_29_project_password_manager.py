import pyperclip
from random import randint, choice, shuffle
import tkinter
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR -------------------------- #


def generate_password():
    # Password Generator Project
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = ''.join(password_list)

    entry_password.delete(0, tkinter.END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if not website or not username or not password:
        messagebox.showinfo(title="Oops",
                            message="Please don't leave any fields empty!")
    else:
        data = f"{website} | {username} | {password}\n"

        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\n"
            f"\nEmail/Username: {username}\nPassword: {password}\n\n"
            f"Is it ok to save?")

        if is_ok:
            with open("day29\\passwords.txt", mode="a") as file:
                file.write(data)

            entry_website.delete(0, tkinter.END)
            entry_username.delete(0, tkinter.END)
            entry_username.insert(0, "filipe@email.com.br")
            entry_password.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------------ #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
image_file = tkinter.PhotoImage(file="day29\\logo.png")
canvas.create_image(100, 100, image=image_file)
canvas.grid(row=0, column=1)

# labels
label_website = tkinter.Label(text="Website:")
label_website.grid(row=1, column=0)

label_username = tkinter.Label(text="Email/Username:")
label_username.grid(row=2, column=0)

label_password = tkinter.Label(text="Password:")
label_password.grid(row=3, column=0)

# Entries
entry_website = tkinter.Entry(width=50)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_username = tkinter.Entry(width=50)
entry_username.grid(row=2, column=1, columnspan=2)
entry_username.insert(0, "filipe@email.com.br")

entry_password = tkinter.Entry(width=32)
entry_password.grid(row=3, column=1)

# buttons
button_generate_password = tkinter.Button(
    text="Generate Password", command=generate_password)
button_generate_password.grid(row=3, column=2)

button_add = tkinter.Button(text="Add", width=42, command=save)
button_add.grid(row=4, column=1, columnspan=2)


window.mainloop()
