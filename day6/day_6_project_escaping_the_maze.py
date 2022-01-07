def turn_right():
    turn_left()
    turn_left()
    turn_left()


def wall_on_left():
    turn_right()
    if wall_on_right():
        turn_right()
        move()
    else:
        turn_right()


if front_is_clear():
    move()
    if right_is_clear():
        wall_on_left()

while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        move()
