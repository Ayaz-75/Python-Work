from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.speed('fastest')
        self.penup()
        self.color('white')
        self.setheading(90)
        self.shapesize(stretch_wid=0.75, stretch_len=5)
        self.goto(position)


    def move_right_paddle_up(self):
        self.fd(20)

    def move_right_paddle_down(self):
        self.bk(20)
