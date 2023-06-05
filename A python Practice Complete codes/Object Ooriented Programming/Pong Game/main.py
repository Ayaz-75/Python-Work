import time
from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard


R_PADDLES_POSITION = (350, 0)
L_PADDLES_POSITION = (-350, 0)

screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.bgcolor('black')

r_paddle = Paddle(R_PADDLES_POSITION)
l_paddle = Paddle(L_PADDLES_POSITION)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.move_right_paddle_up, 'Up')
screen.onkey(r_paddle.move_right_paddle_down, 'Down')

screen.onkey(l_paddle.move_right_paddle_up, 'w')
screen.onkey(l_paddle.move_right_paddle_down, 's')


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 330:
        ball.reset_ball_position()
        scoreboard.update_l_score()

    if ball.xcor() < -330:
        ball.reset_ball_position()
        scoreboard.update_r_score()


screen.mainloop()
