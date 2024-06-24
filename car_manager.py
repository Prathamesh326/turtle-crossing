from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def generate_car(self):
        random_choice = 3
        if random_choice == random.randint(1, 8):
            new_car = Turtle('square')
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
