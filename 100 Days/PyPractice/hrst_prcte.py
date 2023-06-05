from turtle import Screen
import turtle as turtle_module
import random

timmy = turtle_module.Turtle()
turtle_module.colormode(255)
color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68),
              (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12),
              (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165),
              (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211),
              (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232),
              (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167),
              (77, 234, 202), (52, 234, 243), (3, 67, 40)]
timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100
for color in range(1, number_of_dots + 1):
    timmy.dot(10, random.choice(color_list))
    timmy.forward(50)

    if color % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()
