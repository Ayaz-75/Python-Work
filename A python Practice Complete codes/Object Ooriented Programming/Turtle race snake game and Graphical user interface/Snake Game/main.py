import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)
screen.bgcolor("black")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.is_game_over()
        is_game_on = False
        print(f"Game is over and your Score was: {scoreboard.score}")

    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            scoreboard.is_game_over()
            is_game_on = False
            print(f"Game is over and your Score was: {scoreboard.score}")

screen.mainloop()






# x_positions = 0
# y_positions = 0
#
#
# for turtle in range(3):
#     timmy = Turtle()
#     timmy.shape('square')
#     timmy.color('white')
#     timmy.penup()
#     timmy.goto(x=x_positions, y=y_positions)
#     x_positions -= 20
