import random
from turtle import Turtle as t, Screen


tim = t()
screen = Screen()
def draw_square():
    for _ in range(4):
        tim.right(90)
        tim.fd(100)


def draw_dashed_line():
    for i in range(10):
        tim.fd(10)
        tim.penup()
        tim.fd(10)
        tim.pendown()


colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

def draw_shapes(sides):
    angle = 360/sides
    for _ in range(sides):
        tim.fd(50)
        tim.right(angle)


# for i in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shapes(i)


def random_walk():
    heading = [90, 180, 270, 360]
    tim.width(10)
    tim.speed("fastest")
    tim.right(random.choice(heading))
    tim.fd(30)


tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for i in range(360//size_of_gap):
        tim.color(random.choice(colors))
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)



draw_spirograph(10)


# for i in range(120):
#     tim.color(random.choice(colors))
#     random_walk()

# draw_dashed_line()
# draw_square()
screen.mainloop()



# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
#

# def make_square():
#     tim.shape('turtle')
#     tim.fd(100)
#     tim.right(72)
#     tim.fd(100)
#     tim.right(72)
#
#
# make_square()
# make_square()
# tim.fd(100)
