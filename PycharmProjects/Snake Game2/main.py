import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
timmy = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 18:
        food.move_food()
        snake.extend_snake()
        scoreboard.update_score()
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_is_on = False
        scoreboard.game_over()
        print("Game Over")

    for tim in snake.all_turtles[1:]:
        if tim == snake.head:
            pass
        elif snake.head.distance(tim) < 15:
            game_is_on = False
            scoreboard.game_over()
            print("Game Over")


screen.exitonclick()
