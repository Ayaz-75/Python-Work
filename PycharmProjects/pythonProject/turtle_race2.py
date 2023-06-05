import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(500, 400)
user_guess = screen.textinput(title="Turtle Race Guess", prompt="Who is going to win, Choose your color")
colors = ["red", "green", "violet", "indigo", "blue", "yellow", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_game_on = False
for turtle_index in range(0, 6):
    turtle_c = Turtle(shape="turtle")
    turtle_c.penup()
    turtle_c.color(colors[turtle_index])
    turtle_c.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(turtle_c)

if user_guess:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"you won!: winning color is: {winning_color} ")
            else:
                print(f"you lost! winning color is {winning_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()
