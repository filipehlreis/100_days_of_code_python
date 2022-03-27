from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from block_manager import BlockManager

screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=860)
screen.title("Breakout")
screen.tracer(0)


paddle = Paddle((0, -360))
ball = Ball()
scoreboard = Scoreboard()
blocks = BlockManager()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with wall x
    if ball.xcor() > 230 or ball.xcor() < -230:
        # needs to bounce
        ball.bounce_x()

    # Detect collision with wall y
    if ball.ycor() > 410:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 61 and ball.ycor() < -335:
        ball.bounce_y()

    # Detect paddle misses
    if ball.ycor() < -410:
        ball.reset_position()
        time.sleep(0.2)
        # scoreboard.r_point()
        game_is_on = False

    # Detect when ball collides with block
    i = 0
    for block in blocks.blocks:
        i += 1
        if ball.distance(block) < 45 and \
                (
                    (ball.ycor() > (block.ycor() - 19)) and
                    (ball.ycor() < (block.ycor() + 19))
        ):
            try:
                blocks.remove_block(i)
            except Exception as e:
                print(e)
            ball.bounce_y()
            screen.update()
            scoreboard.r_point()
            game_is_on = blocks.is_there_any_block_left()
            # scoreboard.game_over()


screen.exitonclick()
