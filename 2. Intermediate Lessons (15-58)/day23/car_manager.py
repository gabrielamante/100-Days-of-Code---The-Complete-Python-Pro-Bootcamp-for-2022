from operator import length_hint
from re import T
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    

    def _create_car(self):
        frequency = random.randint(1,5)
        if frequency == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300,random.randint(-260,260))
            new_car.setheading(180)
            global all_cars
            self.all_cars.append(new_car)


    def _move_car(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
    
    
    def _move_increment(self):
        self.car_speed += MOVE_INCREMENT