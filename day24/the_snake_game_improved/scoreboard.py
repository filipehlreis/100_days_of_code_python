from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.file_directory_save = "C:\\github\\100_days_of_code_python\\"
        self.file_directory_save += "day24\\the_snake_game_improved\\"
        self.read_high_score_to_data()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.uptade_scoreboard()
        self.hideturtle()

    def uptade_scoreboard(self):
        self.clear()
        self.write(
            f" Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT
        )

    def increase_score(self):
        self.score += 1
        self.uptade_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score_to_data()
        self.score = 0
        self.uptade_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def write_high_score_to_data(self):
        with open(f"{self.file_directory_save}data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def read_high_score_to_data(self):
        with open(f"{self.file_directory_save}data.txt") as file:
            self.high_score = int(file.read())
