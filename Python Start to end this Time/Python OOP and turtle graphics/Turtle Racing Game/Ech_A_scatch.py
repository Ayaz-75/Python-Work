from turtle import Turtle, Screen

timmy = Turtle()
timmy.color('red')
timmy.pencolor('green')
screen = Screen()

screen.listen()


def move_forward():
    timmy.fd(10)


def move_backwards():
    timmy.bk(10)


def move_up():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def move_down():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clear():
    timmy.home()
    timmy.clear()


screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=move_up)
screen.onkey(key='d', fun=move_down)
screen.onkey(key='c', fun=clear)

screen.mainloop()
