import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

#----------------------------- Generating the flash Cards -------------------------------#
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")

# ------------------------- Next card --------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_word, text=current_card['French'], fill='black')
    canvas.itemconfig(canvas_title, text="French", fill='black')
    canvas.itemconfig(card_background, image=canvas_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_title, text="English")
    canvas.itemconfig(canvas_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=canvas_back_image)
    canvas.itemconfig(canvas_title, fill='white')
    canvas.itemconfig(canvas_word, fill='white')



def generate_word():
    data_dict = data.to_dict()
    new_data = data_dict["French"]
    keys = [new_data[key] for key in new_data]
    random_word = random.choice(keys)
    canvas.itemconfig(canvas_word, text=random_word)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    new_dataframe = pd.DataFrame(to_learn)
    new_dataframe.to_csv("data/words_to_learn.csv", index=False)
    next_card()



# ---------------------------- UI setup ------------------------------ #

# Window
window = Tk()
window.title("Flashy")
window.config(padx=15, pady=15, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas_front_image = PhotoImage(file="images/card_front.png")
canvas_back_image = PhotoImage(file="images/card_back.png")


canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(400, 263, image=canvas_front_image)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, 'italic'))
canvas_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
my_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=my_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

my_image2 = PhotoImage(file="images/right.png")
right_button = Button(image=my_image2, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

# change_item()
next_card()


























window.mainloop()