# Computing the distance through pythagoras theorem
# import math


def pythagoras_theorem(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # does same as math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance


pythagoras_theorem(3, 4, 5, 6)
print(pythagoras_theorem(3, 4, 5, 6))


