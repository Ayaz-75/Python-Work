"""Practice the oop programs with instance methods"""


class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point: ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
print(isinstance(point, Point))
# isinstance tells either the given object is instance of given class or not


another = Point(3, 4)
another.draw()
print(isinstance(another, Point))
# isinstance tells either the given object is instance of given class or not


Point.default_color = "blue"
print(f"point object accessing class attribute: {point.default_color}")
print(f"Point class accessing class attribute: {Point.default_color}")
print(another.default_color)
