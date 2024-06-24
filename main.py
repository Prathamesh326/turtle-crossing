import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

player.move_turtle()

screen.listen()
screen.onkey(player.move_turtle, 'w')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.generate_car()
    cars.move_car()

    for car in cars.all_cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.if_collide()

    if player.finish():
        scoreboard.calculate_level()
        cars.increase_speed()

screen.exitonclick()
