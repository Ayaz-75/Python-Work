import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
turtle.colormode(255)
timmy.pensize(15)
timmy.speed(10)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_colo_tuple = (r, g, b)
    return my_colo_tuple


direction = [0, 90, 180, 270, 360]
for _ in range(200):
    timmy.fd(35)
    timmy.right(random.choice(direction))
    timmy.color(change_color())


screen = Screen()
screen.mainloop()
print('Done')
