from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        for _ in range(20):
            self.add_car()

        self.car_speed = 0.1

    def increase_speed(self):
        self.car_speed = self.car_speed * 0.9

    def move(self):
        for car_number in range(len(self.cars)):
            new_xcor = self.cars[car_number].xcor() - MOVE_INCREMENT
            new_ycor = self.cars[car_number].ycor()
            if new_xcor < -301:
                new_xcor = random.randrange(300, 315)
                new_ycor = random.randrange(-25, 26) * 10
            self.cars[car_number].goto(new_xcor, new_ycor)

    def add_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        rand_y = random.randrange(-25, 26) * 10
        rand_x = random.randrange(-26, 27) * 10
        new_car.goto(rand_x, rand_y)
        new_car.car_speed = MOVE_INCREMENT
        self.cars.append(new_car)
