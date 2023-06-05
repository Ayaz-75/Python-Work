from turtle import Turtle
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        # self.update_score()
        self.refresh_score()

    def refresh_score(self):
        self.write(f"SCORE: {self.score}", align="center", font=("arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=("Arial", 20, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.refresh_score()
