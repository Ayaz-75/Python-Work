from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.listen()
steps = 10


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.back(10)


def move_counter_clock():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def move_clock_wise():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clear_drawing():
    screen.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


# def game():
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_counter_clock, "d")
screen.onkey(move_clock_wise, "a")
screen.onkey(clear_drawing, "c")

screen.exitonclick()
