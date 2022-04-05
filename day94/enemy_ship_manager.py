from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class EnemyShipManager:
    def __init__(self):
        super().__init__()
        self.ships = []
        self.add_random_ship(5)
        self.ship_to_remove = []

    def add_random_ship(self, number):
        for _ in range(number):
            new_ship = Turtle()
            new_ship.shape("triangle")
            new_ship.left(30)
            new_ship.shapesize(stretch_wid=2, stretch_len=2)
            new_ship.penup()
            new_ship.color(random.choice(COLORS))
            rand_y = random.randrange(5, 20) * 20
            rand_x = random.randrange(-10, 10) * 20
            new_ship.goto(rand_x, rand_y)
            self.ships.append(new_ship)

    def add_ship(self):
        y_position = 400
        x_position = random.randrange(-8, 9) * 25

        new_ship = Turtle()
        new_ship.shape("triangle")
        new_ship.left(30)
        new_ship.shapesize(stretch_wid=2, stretch_len=2)
        new_ship.penup()
        new_ship.color(random.choice(COLORS))
        new_ship.goto(x_position, y_position)
        self.ships.append(new_ship)

    def remove_ship(self, ship_to_remove):
        self.ship_to_remove.append(ship_to_remove)

    def remove_ships_all(self):
        if self.ship_to_remove:
            for ship in self.ship_to_remove:
                index = self.ships.index(ship)
                self.ships[index].goto(1000, 1000)
                self.ships.remove(ship)
        # print(len(self.ships))
        self.ship_to_remove = []

    def move(self):
        for ship_number in range(len(self.ships)):
            new_xcor = self.ships[ship_number].xcor()
            new_ycor = self.ships[ship_number].ycor() - MOVE_INCREMENT
            self.ships[ship_number].goto(new_xcor, new_ycor)
