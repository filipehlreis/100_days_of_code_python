import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
cars = CarManager()
# screen.onkey(player.move, "Up")
screen.onkeypress(player.move, "Up")
car_count = 0

game_is_on = True
while game_is_on:
    time.sleep(cars.car_speed)
    cars.move()

    # Detect when player gets to finish line
    if player.ycor() >= FINISH_LINE_Y:
        player.reset_level()
        # Increase level on scoreboard
        scoreboard.increase_level()
        # Increase car speed
        cars.increase_speed()
    screen.update()

    # Detect when player collides with car
    for car in cars.cars:
        if player.distance(car) < 31 and \
                (
                    (player.ycor() > (car.ycor() - 20)) and
                    (player.ycor() < (car.ycor() + 20))
        ):
            game_is_on = False
            screen.update()
            scoreboard.game_over()

screen.exitonclick()
