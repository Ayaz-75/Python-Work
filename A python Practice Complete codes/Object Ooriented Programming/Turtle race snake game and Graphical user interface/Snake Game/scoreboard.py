from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update_score_board()

    def update_score_board(self):
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)


    def is_game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()
