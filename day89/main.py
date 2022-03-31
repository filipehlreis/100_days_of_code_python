from __future__ import annotations
from tkinter import END, StringVar
import tkinter


# ---------------------------- DEBUG MODE -------------------------------- #
run_debug = False
open_tkinter = True


# ---------------------------- DEFINE GLOBAL VAR ------------------------- #
timer = 0
countdown_time = 6
time_set = False


# ---------------------------- TIMER MECHANISM --------------------------- #
def start_timer():
    global countdown_time, time_set
    time_set = True
    count_down(countdown_time)


# ---------------------------- COUNTDOWN MECHANISM ----------------------- #
def count_down(count):
    global countdown_time

    countdown_time -= 1
    atualiza_timer()

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        entry_typing_box.delete(0, END)
        window.after_cancel(timer)


# ---------------------------- ATUALIZA LABEL TIMER  ------------- #
def atualiza_timer():
    global countdown_time
    text_to_uptade = f"{countdown_time} seconds"
    label_time_remaining_var.config(text=text_to_uptade)


# ---------------------------- PEGA VARIACAO NO CAMPO DE PALAVRA --------- #
def callback(sv):
    global time_set, timer, countdown_time

    if time_set:
        window.after_cancel(timer)
        countdown_time = 6

    texto = entry_typing_box.get()
    print(texto[-1:])

    if run_debug:
        entry_typing_box.delete(0, END)

    start_timer()


if open_tkinter:
    # ------------------------ UI SETUP ---------------------------------- #
    window = tkinter.Tk()
    window.title("Typing Speed Test")
    window.config(padx=50, pady=50)

    # labels
    label_title = tkinter.Message(width=300)
    label_title.grid(row=0, column=0, columnspan=4, rowspan=3)
    label_title.config(
        text="Type as much words as you can, otherwise, after 5 seconds, your"
        "words are going to after life!", pady=20, justify='center')

    label_time_remaining = tkinter.Label()
    label_time_remaining.grid(row=6, column=0, columnspan=2)
    label_time_remaining.config(text='Remaining Time:')

    label_time_remaining_var = tkinter.Label()
    label_time_remaining_var.grid(row=6, column=2, columnspan=2)
    label_time_remaining_var.config(text=f'{countdown_time}')
    atualiza_timer()

    # Entries
    sv = StringVar()
    sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
    entry_typing_box = tkinter.Entry(
        window, textvariable=sv, width=50)
    entry_typing_box.grid(row=8, column=0, columnspan=4)
    entry_typing_box.config(justify='center')
    entry_typing_box.focus()

    window.mainloop()
