from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_farwards():
    timmy.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_farwards)
screen.exitonclick()
