import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
turtle.colormode(255)
timmy.speed('fastest')


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_colo_tuple = (r, g, b)
    return my_colo_tuple


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(change_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)
screen = Screen()
screen.mainloop()
