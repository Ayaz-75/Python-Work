import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.speed('fastest')

turtle.colormode(255)

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    random_c = (r, g, b)
    return random_c


angles = [90, 180, 360]
def random_walk():
    timmy.pensize(10)
    for i in range(100):
        timmy.color(random_color())
        random_angle = random.choice(angles)
        timmy.fd(20)
        timmy.right(random_angle)


random_walk()

screen.exitonclick()
