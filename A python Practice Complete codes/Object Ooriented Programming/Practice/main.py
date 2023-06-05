from turtle import Turtle, Screen
from prettytable import PrettyTable
timmy = Turtle()
timmy.color("red")
screen = Screen()

pt = PrettyTable()
for i in range(5):
    print(pt)


# def rotate_it():
#     timmy.fd(10)
#     timmy.right(20)
#
#
#
# for i in range(20):
#     rotate_it()

#
screen.exitonclick()
