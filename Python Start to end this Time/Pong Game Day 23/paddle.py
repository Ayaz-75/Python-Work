from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        PADDLE_WIDTH = 4
        PADDLE_LENGTH = 0.75

        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.color('white')
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
