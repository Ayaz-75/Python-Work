import random
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def square():
    for i in range(4):
        timmy.right(90)
        timmy.fd(100)

def dashes():
    timmy.fd(10)
    timmy.penup()
    timmy.fd(10)
    timmy.pendown()

def triangle():
    for i in range(3):
        timmy.fd(100)
        timmy.right(120)

# triangle()

colors = ['red', 'blue', 'pink', 'green', 'orange', 'purple']
def multi_angle(num_sides):
    angle = 360 / num_sides
    timmy.color(random.choice(colors))
    for i in range(num_sides):
        timmy.fd(100)
        timmy.right(angle)

for shapes in range(3, 11):
    multi_angle(shapes)



screen.exitonclick()
