import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('white')
player = Player()
screen.listen()
screen.onkey(player.move_player, 'Up')

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            turtle.write('Game over!', align='center', font=('courier', 25, 'bold'))

    if player.is_finished():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()
