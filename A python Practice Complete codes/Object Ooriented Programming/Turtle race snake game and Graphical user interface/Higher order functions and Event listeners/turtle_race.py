import random
from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race: ")


x_position = -230
y_position = 100
colors = ['red', 'blue', 'green', 'indigo', 'violet', 'yellow', 'orange']
random_walk = random.randint(5, 15)

all_turtles = []

for i in range(7):
    tim = Turtle()
    tim.color(colors[i])
    tim.penup()
    tim.shape('turtle')
    tim.goto(x=x_position, y=y_position)
    y_position -= 30
    all_turtles.append(tim)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for tur in all_turtles:
        if tur.xcor() > 230:
            winning_color = tur.pencolor()
            if winning_color == user_bet:
                print(f"You won! winning color is: {winning_color}")
                is_race_on = False

            else:
                print(f"You lost! winning color is {winning_color}")
                is_race_on = False
        random_walk = random.randint(5, 15)
        tur.fd(random_walk)


screen.mainloop()
