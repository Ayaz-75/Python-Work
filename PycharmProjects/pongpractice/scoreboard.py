from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("green")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center", font=("Arial", 50, "normal"))

        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Arial", 50, "normal"))

    def refresh_l_score(self):
        self.l_score += 10
        self.update_scoreboard()

    def refresh_r_score(self):
        self.r_score += 10
        self.update_scoreboard()
