from turtle import Screen
from ship import Ship
from shoot_manager import Shoot
import time
from scoreboard import Scoreboard
from enemy_ship_manager import EnemyShipManager

screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=860)
screen.title("Space Invader")
screen.tracer(0)


ship = Ship((0, -370))
shoot_manager = Shoot()
scoreboard = Scoreboard()
ship_enemy = EnemyShipManager()


def fire_shoot():
    posicao = ship.xcor()
    shoot_manager.add_shoot(posicao)
    # print(f'Shoot at {posicao}')


time_refresh = 20
screen.listen()
screen.onkey(ship.go_right, "Right")
screen.onkey(ship.go_left, "Left")
screen.onkey(fire_shoot, "Up")

enemy_refresh = 0
enemy_add = 0
game_is_on = True
while game_is_on:
    time.sleep(0.3/time_refresh)

    if enemy_refresh < time_refresh:
        enemy_refresh += 1
    elif enemy_add > 1:
        ship_enemy.add_ship()
        enemy_add = 0
    else:
        enemy_refresh = 0
        enemy_add += 1
        ship_enemy.move()

    shoot_manager.move()
    screen.update()

    try:
        # # Detect when shoot collides with enemy ship
        for shoot in shoot_manager.shoots:
            for enemy in ship_enemy.ships:
                if shoot.distance(enemy) < 25 and \
                        ((shoot.xcor() > (enemy.xcor() - 21)) and
                         (shoot.xcor() < (enemy.xcor() + 21))):
                    shoot_manager.remove_shoot(shoot)
                    ship_enemy.remove_ship(enemy)
                    scoreboard.r_point()

        # # Detect when enemy shipe reach you
        for enemy in ship_enemy.ships:
            if enemy.ycor() < -340:
                game_is_on = False
                scoreboard.game_over()
                screen.update()

    except Exception as e:
        msg_error = e
        print(msg_error)

    shoot_manager.remove_shoot_all()
    ship_enemy.remove_ships_all()

screen.exitonclick()
