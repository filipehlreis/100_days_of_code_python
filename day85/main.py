from __future__ import annotations
from tkinter import END, StringVar
import tkinter
import pandas
import random
import datetime as dt

# ---------------------------- DEBUG MODE -------------------------------- #
run_debug = False
open_tkinter = True


# ---------------------------- DEFINE GLOBAL VAR ------------------------- #
timer = 0
count_words_per_min = 0
count_correct_words = 0
count_incorrect_words = 0
countdown_time = 60
current_word = 0
some_words = []
time_now = 0
time_start = 0
time_stop = 0
time_set = False
time_sum: dt.datetime = dt.datetime.now()
time_stop_previous = 0


# ---------------------------- TIMER MECHANISM --------------------------- #
def start_timer():
    global countdown_time
    count_down(countdown_time)


# ---------------------------- COUNTDOWN MECHANISM ----------------------- #
def count_down(count):
    global countdown_time
    minutes = int(count / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = int((count-1) % 60)
    if seconds < 10:
        seconds = f"{seconds}"
    countdown_time = seconds
    label_time_remaining_var.config(text=f"{countdown_time}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- LOAD MOST COMMON WORDS -------------------- #
file_dir = "day85\\assets\\words_to_type_most_common.csv"
words_to_type = pandas.read_csv(file_dir)
words_to_type_list = [word for word in words_to_type['a']]
random.shuffle(words_to_type_list)

if run_debug:
    print(words_to_type_list)


# ---------------------------- START ACTION BUTTON ------------- #
def start_button():
    global time_start, time_now, time_stop, countdown_time, time_set
    global time_stop_previous

    time_start = dt.datetime.now()
    time_stop_previous = time_start

    time_start = time_stop_previous
    time_stop = dt.datetime.now()

    if not time_set and countdown_time == 60:
        # countdown_time = 60
        start_timer()
        get_random_list()
        time_set = True
    elif not time_set:
        start_timer()
        time_set = True


# ---------------------------- STOP ACTION BUTTON ------------- #
def stop_button():
    global time_start, time_now, time_stop, time_set, time_sum
    global time_stop_previous

    if time_set:
        window.after_cancel(timer)

    time_start = time_stop_previous
    time_stop = dt.datetime.now()
    time_between = time_stop - time_start

    time_sum += time_between
    print(time_sum)

    # time_start = time_stop_previous
    # time_stop = dt.datetime.now()
    # print(time_between)

    atualiza_status()
    time_set = False


# ---------------------------- RESET ACTION BUTTON ------------- #
def reset_button():
    global count_words_per_min, count_correct_words, count_incorrect_words
    global countdown_time, current_word, some_words
    global time_start, time_now, time_stop, time_set, time_sum

    if time_set:
        window.after_cancel(timer)

    time_set = False
    time_start = 0
    time_now = 0
    time_stop = 0
    time_sum = 0

    count_words_per_min = 0
    count_correct_words = 0
    count_incorrect_words = 0
    countdown_time = 60
    current_word = 0
    some_words = []
    atualiza_status()
    atualiza_timer()
    # get_random_list()


# ---------------------------- GET RANDOM LIST OF WORDS ------------------ #
def get_random_list():
    global some_words
    random.shuffle(words_to_type_list)
    some_words = [word for word in words_to_type_list[:50]]
    label_words.config(text=some_words[:-1])


# ---------------------------- ATUALIZA LABEL TIMER  ------------- #
def atualiza_timer():
    global countdown_time

    label_time_remaining_var.config(text=countdown_time)


# ---------------------------- ATUALIZA STATUS ------------- #
def atualiza_status():
    global current_word, count_correct_words, count_incorrect_words
    global count_words_per_min, time_sum, time_now

    time_start = time_stop_previous
    time_stop = dt.datetime.now()
    time_between = time_stop - time_start
    # print(time_between)

    time_sum = time_sum + time_between
    print(time_sum)
    if time_sum.second != 0:
        count_words_per_min = round((current_word / time_sum.second) * 60, 2)

    label_wpm_var.config(text=f'{count_words_per_min}')
    label_correct_wpm_var.config(text=f'{count_correct_words} words.')
    label_incorrect_wpm_var.config(text=f'{count_incorrect_words} words')
    prop_ratio = round((count_correct_words/(current_word+1) * 100), 2)
    label_prop_correct_wpm_var.config(
        text=f'{prop_ratio} %')


# ---------------------------- PEGA VARIACAO NO CAMPO DE PALAVRA --------- #
def callback(sv):
    global some_words
    global current_word, count_correct_words, count_incorrect_words

    texto = entry_typing_box.get()

    if texto[-1:] == ' ':
        if run_debug:
            print(some_words[current_word])
            print('detectado espaco')

        texto_alter = texto.replace(' ', '')
        if some_words[current_word] == texto_alter:
            if run_debug:
                print("Detectado palavra igual.")
            count_correct_words += 1
            atualiza_status()

        elif len(texto_alter) == 0:
            if run_debug:
                print('somente espacos')
            atualiza_status()
        else:
            count_incorrect_words += 1
            atualiza_status()

        entry_typing_box.delete(0, END)
        current_word += 1

        if run_debug:
            print(f"'{texto_alter}'")


if open_tkinter:
    # ------------------------ UI SETUP ---------------------------------- #
    window = tkinter.Tk()
    window.title("Typing Speed Test")
    window.config(padx=50, pady=50)

    # canvas = tkinter.Canvas(width=600, height=400)
    # image_file = tkinter.PhotoImage(file="day84\\assets\\no-image.png")
    # canvas.create_image(300, 200, image=image_file)
    # canvas.grid(row=0, column=0, columnspan=3)

    # labels
    label_words = tkinter.Message(width=600)
    label_words.grid(row=0, column=0, columnspan=12, rowspan=5)
    label_words.config(text='Some words here.', pady=20)

    label_wpm = tkinter.Label()
    label_wpm.grid(row=6, column=0, columnspan=3)
    label_wpm.config(text='WPM:')

    label_wpm_var = tkinter.Label()
    label_wpm_var.grid(row=6, column=3, columnspan=3)
    label_wpm_var.config(text=f'{count_words_per_min}')

    label_time_remaining = tkinter.Label()
    label_time_remaining.grid(row=6, column=6, columnspan=3)
    label_time_remaining.config(text='Remaining Time:')

    label_time_remaining_var = tkinter.Label()
    label_time_remaining_var.grid(row=6, column=9, columnspan=3)
    label_time_remaining_var.config(text=f'{countdown_time}')

    label_correct_wpm = tkinter.Label()
    label_correct_wpm.grid(row=9, column=0, columnspan=2)
    label_correct_wpm.config(text='Correct Words')

    label_correct_wpm_var = tkinter.Label()
    label_correct_wpm_var.grid(row=9, column=2, columnspan=2)
    label_correct_wpm_var.config(text=f'{count_correct_words} words.')

    label_incorrect_wpm = tkinter.Label()
    label_incorrect_wpm.grid(row=9, column=4, columnspan=2)
    label_incorrect_wpm.config(text='Inorrect Words')

    label_incorrect_wpm_var = tkinter.Label()
    label_incorrect_wpm_var.grid(row=9, column=6, columnspan=2)
    label_incorrect_wpm_var.config(text=f'{count_correct_words} words.')

    label_prop_correct_wpm = tkinter.Label()
    label_prop_correct_wpm.grid(row=9, column=8, columnspan=2)
    label_prop_correct_wpm.config(text='Ratio:')

    label_prop_correct_wpm_var = tkinter.Label()
    label_prop_correct_wpm_var.grid(row=9, column=10, columnspan=2)
    label_prop_correct_wpm_var.config(
        text=f'{count_correct_words/(current_word+1) * 100} %')

    # Entries
    sv = StringVar()
    sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
    entry_typing_box = tkinter.Entry(window, textvariable=sv, width=100)
    entry_typing_box.grid(row=8, column=0, columnspan=12)
    entry_typing_box.config(justify='center')
    entry_typing_box.focus()

    # buttons
    button_start = tkinter.Button(
        text="Start", command=start_button, width=28)
    button_start.grid(row=7, column=0, columnspan=4)

    button_stop = tkinter.Button(
        text="Stop", command=stop_button, width=28)
    button_stop.grid(row=7, column=4, columnspan=4)

    button_reset = tkinter.Button(
        text="Reset", command=reset_button, width=28)
    button_reset.grid(row=7, column=8, columnspan=4)

    window.mainloop()
