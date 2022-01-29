import tkinter

# ---------------------------- CONSTANTS --------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2  # 25
SHORT_BREAK_MIN = 0.1  # 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label "timer"
    label_timer.config(text="Timer", fg=GREEN)
    # reset check_marks
    label_check.config(text="")

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM --------------------------- #


def start_timer_button():
    global reps
    if reps < 1:
        start_timer()


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if its the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)
        # if its the 1st/3rd/5th/7th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
    # if its 2nd/4th/6th rep:
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ----------------------- #


def count_down(count):

    minutes = int(count / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = int(count % 60)
    if seconds < 10:
        seconds = f"0{seconds}"

    text_count = f"{minutes}:{seconds}"

    canvas.itemconfig(timer_text, text=text_count)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = int(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        label_check.config(text=marks)


# ---------------------------- UI SETUP ---------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="day28\\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130,
    text="00:00", fill="white",
    font=(FONT_NAME, 28, "bold")
)
canvas.grid(row=1, column=1)


label_timer = tkinter.Label(
    text="Timer", fg=GREEN, bg=YELLOW,
    font=(FONT_NAME, 40, "bold"))
label_timer.grid(row=0, column=1)

button_start = tkinter.Button(
    text="Start", highlightthickness=0, command=start_timer_button)
button_start.grid(row=2, column=0)

button_reset = tkinter.Button(
    text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)

label_check = tkinter.Label(
    text="", fg=GREEN, bg=YELLOW,
    font=(FONT_NAME, 25, "bold"))
label_check.grid(row=3, column=1)


window.mainloop()
