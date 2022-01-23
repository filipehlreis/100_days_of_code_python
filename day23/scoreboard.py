from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score_level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(
            f"Level: {self.score_level}",
            align="left",
            font=FONT)
        self.goto(0, -280)
        self.write(
            '----------------------------------------------------',
            align="center",
            font=FONT
        )
        self.goto(0, 240)
        self.write(
            '----------------------------------------------------',
            align="center",
            font=FONT
        )

    def increase_level(self):
        self.score_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align="center",
            font=FONT)
