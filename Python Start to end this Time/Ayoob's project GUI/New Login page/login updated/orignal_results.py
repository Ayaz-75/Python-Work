from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

class OriginalResults:

    window = Tk()
    window.title('Bug fixing Time Estimation')
    window.config(padx=80, pady=40, bg=YELLOW)
    title_label = Label(text="Bug fixing Time Estimation", fg='#0F3460', bg=YELLOW, font=(FONT_NAME, 20))
    title_label.grid(column=1, row=0)


    canvas = Canvas(width=300, height=270, bg=YELLOW, highlightthickness=0)


    resolution_entry = Entry(width=35)
    resolution_entry.grid(row=8, column=1, columnspan=3)


    # Buttons
    submit_button = Button(text="Result")
    submit_button.grid(row=11, column=1)


    window.mainloop()


