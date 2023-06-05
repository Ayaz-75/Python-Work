import random
from turtle import Turtle, Screen

timmy = Turtle()
colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'violet', 'fuchsia', 'navy', 'cornsilk', 'darkgrey', 'gold',
          'peru']


def draw_shapes(num_of_sides):
    angle = 360 / num_of_sides
    timmy.color(random.choice(colors))
    for _ in range(num_of_sides):
        timmy.fd(70)
        timmy.right(angle)


for shape in range(3, 11):
    draw_shapes(shape)


# for _ in range(3):
#     timmy.color(random.choice(colors))
#     timmy.fd(100)
#     timmy.rt(120)
#
# for _ in range(4):
#     timmy.color(random.choice(colors))
#     timmy.fd(100)
#     timmy.rt(90)
#
# for _ in range(5):
#     timmy.color(random.choice(colors))
#     timmy.fd(100)
#     timmy.rt(72)
#
# for _ in range(6):
#     timmy.color(random.choice(colors))
#     timmy.fd(100)
#     timmy.rt(60)
#
# for _ in range(7):
#     timmy.color(random.choice(colors))
#     timmy.fd(100)
#     timmy.rt(51.42857142857143)
#
# for _ in range(8):
#     timmy.color(random.choice(colors))
#     timmy.fd(100)
#     timmy.rt(45)
#
# for _ in range(9):
#     timmy.color(random.choice(colors))
#     timmy.fd(100)
#     timmy.rt(40)
#
# for _ in range(10):
#     timmy.color(random.choice(colors))
#     timmy.fd(100)
#     timmy.rt(36)

screen = Screen()
screen.mainloop()
print("done")