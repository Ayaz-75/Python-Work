from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for position in POSITION:
            self.create_body(position)

    def create_body(self, position):
        timmy = Turtle("square")
        timmy.penup()
        timmy.color("white")
        timmy.goto(position)
        self.all_turtles.append(timmy)

    def extend_snake(self):
        self.create_body(self.all_turtles[-1].position())

    def move_snake(self):
        for tur in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[tur - 1].xcor()
            new_y = self.all_turtles[tur - 1].ycor()
            self.all_turtles[tur].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
