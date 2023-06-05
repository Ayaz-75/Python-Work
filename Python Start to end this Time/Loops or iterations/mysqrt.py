"""

Copy the loop from “Square Roots” on page 79 and encapsulate it in a function called
my-sqrt that takes a as a parameter, chooses a reasonable value of x, and returns an
estimate of the square root of a

"""


def my_sqrt(a):

    x = 3

    y = (x + a / a) / 2
    return y


print(my_sqrt(4))
