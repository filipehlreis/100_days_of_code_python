from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # self.goto(-100, 320)
        # self.write(
        #     self.l_score,
        #     align="center",
        #     font=("Courier", 60, "normal")
        # )
        self.goto(000, 320)
        self.write(
            self.r_score,
            align="center",
            font=("Courier", 60, "normal")
        )

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 10
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align="center",
            font=FONT)
