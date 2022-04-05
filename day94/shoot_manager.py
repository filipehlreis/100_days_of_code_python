from turtle import Turtle
import random


MOVE_INCREMENT = 10
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Shoot(Turtle):
    def __init__(self):
        super().__init__()
        self.shoots = []
        self.shoots_to_remove = []

    def move(self):
        try:
            for shoot_number in range(len(self.shoots)):
                if self.shoots[shoot_number].ycor() > 400:
                    self.shoots[shoot_number].goto(1000, 1000)
                    self.shoots.pop(shoot_number)
        except Exception as e:
            msg_error = e

        for shoot_number in range(len(self.shoots)):
            new_xcor = self.shoots[shoot_number].xcor()
            new_ycor = self.shoots[shoot_number].ycor() + MOVE_INCREMENT
            self.shoots[shoot_number].goto(new_xcor, new_ycor)

    def add_shoot(self, ship_position):
        new_shoot = Turtle()
        new_shoot.shape("square")
        new_shoot.shapesize(0.4, 0.2)
        new_shoot.penup()
        new_shoot.color('blue')
        new_shoot.goto(ship_position, -360)
        self.shoots.append(new_shoot)

    def remove_shoot(self, shoot_to_remove):
        self.shoots_to_remove.append(shoot_to_remove)

    def remove_shoot_all(self):
        try:
            if self.shoots_to_remove:
                for shoot in self.shoots_to_remove:
                    index = self.shoots.index(shoot)
                    self.shoots[index].goto(1000, 1000)
                    self.shoots.remove(shoot)
        except Exception as e:
            msg_error = e

        # print(len(self.shoots))
        self.shoots_to_remove = []
