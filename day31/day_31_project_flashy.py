
import random
from tkinter import messagebox
import pandas
import tkinter
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")


# ---------------- Reading the file --------------------------------------*
try:
    file_french_words_direct = "day31\\data\\words_to_learn.csv"
    file_french_words = pandas.read_csv(file_french_words_direct)
except FileNotFoundError:
    file_french_words_direct = "day31\\data\\french_words.csv"
    file_french_words = pandas.read_csv(file_french_words_direct)
finally:
    to_learn = file_french_words.to_dict(orient="records")


current_card = {}


# ---------------- Functions -------------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    try:
        current_card = random.choice(to_learn)
        canvas.itemconfig(canvas_image_card, image=image_card_front)
        canvas.itemconfig(canvas_text_language, text="French", fill="black")
        canvas.itemconfig(
            canvas_text_word,
            text=current_card["French"],
            fill="black",)
    except IndexError:
        canvas.itemconfig(canvas_image_card, image=image_card_front)
        canvas.itemconfig(canvas_text_language, text="French", fill="black")
        canvas.itemconfig(
            canvas_text_word,
            text="No more words.",
            fill="black",)
        messagebox.showinfo(
            title="Oopps", message="There is no word to learn!")

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_text_language, text="English", fill="white")
    canvas.itemconfig(
        canvas_text_word,
        text=current_card["English"],
        fill="white",)
    canvas.itemconfig(canvas_image_card, image=image_card_back)


def got_it():
    try:
        to_learn.remove(current_card)
        data = pandas.DataFrame(to_learn)
        data.to_csv("day31\\data\\words_to_learn.csv", index=False)
    except ValueError:
        messagebox.showinfo(
            title="Oopps", message="There is no word to learn!")

    next_card()


# ---------------- Interface --------------------------------------*
window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

canvas = tkinter.Canvas(width=800, height=526,
                        bg=BACKGROUND_COLOR, highlightthickness=0)
image_card_front = tkinter.PhotoImage(file="day31\\images\\card_front.png")
image_card_back = tkinter.PhotoImage(file="day31\\images\\card_back.png")
canvas_image_card = canvas.create_image(400, 263, image=image_card_front)
canvas.grid(row=0, column=0, columnspan=2)

canvas_text_language = canvas.create_text(
    400, 150, text="", font=FONT_LANGUAGE, fill="black")
canvas_text_word = canvas.create_text(
    400, 263, text="", font=FONT_WORD, fill="black")


image_button_wrong = tkinter.PhotoImage(file="day31\\images\\wrong.png")
image_button_right = tkinter.PhotoImage(file="day31\\images\\right.png")
button_wrong = tkinter.Button(
    padx=50,
    highlightthickness=0,
    activebackground=BACKGROUND_COLOR,
    borderwidth=0,
    image=image_button_wrong,
    command=next_card,
)
button_wrong.grid(row=1, column=0)

button_right = tkinter.Button(
    padx=50,
    highlightthickness=0,
    activebackground=BACKGROUND_COLOR,
    borderwidth=0,
    image=image_button_right,
    command=got_it,
)
button_right.grid(row=1, column=1)


next_card()


window.mainloop()
