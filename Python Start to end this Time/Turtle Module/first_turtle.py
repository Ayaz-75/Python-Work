import turtle
from turtle import Turtle
import math

timmy = Turtle()  # timmy is object of Turtle() class
#
# print(timmy)
# for i in range(4):
#     timmy.fd(100)
#     timmy.rt(90)
#

'''
1. Write a function called square that takes a parameter named t, which is a turtle.
It should use the turtle to draw a square.
Write a function call that passes bob as an argument to square, and then run the
program again
'''

# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.rt(90)
#
#
# square(timmy)
'''
2. Add another parameter, named length, to square. Modify the body so length of
the sides is length, and then modify the function call to provide a second argument.
Run the program again. Test your program with a range of values for
length
'''

# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.rt(90)
#
#
# square(t=timmy, length=200)
#
# turtle.mainloop()

'''
3. Make a copy of square and change the name to polygon. Add another parameter
named n and modify the body so it draws an n-sided regular polygon.
Hint: The exterior angles of an n-sided regular polygon are 360/n degrees
'''

# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.rt(360 / n)
#
#
# polygon(t=timmy, length=100, n=5)
# turtle.mainloop()

'''
4. Write a function called circle that takes a turtle, t, and radius, r, as parameters
and that draws an approximate circle by calling polygon with an appropriate
length and number of sides. Test your function with a range of values of r.
Hint: figure out the circumference of the circle and make sure that length * n =
circumference.
'''

# def circle(t, r):
#     for i in range(r):
#         t.fd(15)
#         t.rt(360/r)
#
#
# circle(timmy, 50)
#
#
# turtle.mainloop()

'''
5. Make a more general version of circle called arc that takes an additional
parameter angle, which determines what fraction of a circle to draw. angle is in
units of degrees, so when angle=360, arc should draw a complete circle.
'''


# def arc(t, r, angle):
#     for i in range(r):
#         t.fd(15)
#         t.rt(360/angle)
#
#
# arc(timmy, 50, 50)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.rt(angle)


# polygon(timmy, 7, 70)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n

    polygon(t, 90, length)


circle(timmy, 80)

turtle.mainloop()
