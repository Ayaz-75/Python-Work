from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
import turtle
from scoreboard import Scoreboard
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_v()

    # Detect Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_points()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_points()

    if scoreboard.l_score >= 10:
        scoreboard.write('Left Player wins!', align='left', font=('Arial', 20, 'normal'))
        game_is_on = False
    elif scoreboard.r_score >= 10:
        scoreboard.write('Right Player wins!', align='right', font=('Arial', 20, 'normal'))
        game_is_on = False

screen.exitonclick()
