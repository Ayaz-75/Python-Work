import math
import tkinter
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if work_sec % 8 == 0:
        count_down(long_break_sec)
        text_label.config(text='Long Break', fg=RED)

    elif work_sec % 2 == 0:
        count_down(short_break_sec)
        text_label.config(text='Short Break', fg=PINK)

    else:
        count_down(work_sec)
        text_label.config(text='Work Time', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        window.after(1000, count_down, count - 1)

    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(width=500, height=500)
window.config(padx=150, pady=80, bg=YELLOW)

# Setting the canvas
canvas = Canvas(width=210, height=224)
img = PhotoImage(file='tomato.png')
canvas.create_image(110, 112, image=img)
canvas.config(bg=YELLOW, highlightthickness=0)

# Creating
timer_text = canvas.create_text(112, 130, text='00:00', fill='White', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=2, column=2)
# count_down(5)

# Adding the other components
text_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN, highlightthickness=0)
text_label.grid(row=0, column=2)

# Tick mark labels
tick_label = Label(text='✔', font=(FONT_NAME, 15), bg=YELLOW, fg=GREEN, highlightthickness=0)
tick_label.grid(row=4, column=2)

# Adding start buttons
start_button = Button(text='Start', command=start_timer)
start_button.grid(row=3, column=1)

# Adding reset button
reset_button = Button(text='Reset')
reset_button.grid(row=3, column=3)

window.mainloop()
