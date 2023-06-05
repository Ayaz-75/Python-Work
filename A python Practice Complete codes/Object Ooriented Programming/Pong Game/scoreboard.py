from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 200)
        self.write(self.l_score, align='left', font=('Arial', 35, 'bold'))
        self.goto(150, 200)
        self.write(self.r_score, align='right', font=('Arial', 35, 'bold'))


    def update_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_r_score(self):
        self.r_score += 1
        self.update_scoreboard()