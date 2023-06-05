import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(500, 400)
user_guess = screen.textinput(title="Guess your choice", prompt="Guess who is going to winn, Choose your color")
colors = ["red", "green", "violet", "indigo", "blue", "yellow", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"you have won the winning color is {winning_color}")
            else:
                print(f"you have lost the winning color is {winning_color}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


# print(user_guess)
screen.exitonclick()
