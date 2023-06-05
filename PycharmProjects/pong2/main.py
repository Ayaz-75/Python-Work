import time
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.tracer(0)

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")

r_paddle = Paddle()
l_paddle = Paddle()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "o")
screen.onkey(l_paddle.move_down, "l")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # r_paddle.move_up()
screen.exitonclick()
