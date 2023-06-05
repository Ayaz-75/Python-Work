class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"({self.x},{self.y})")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 2)
other_p = Point(1, 2)

print(point == other_p)
# if you will not apply eq magic method it will return false

combined = (point + other_p)
print(combined.x, combined.y)
# this will give us addition of x and y components of both objects
