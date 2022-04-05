from turtle import Turtle


class Ship(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("triangle")
        self.color("white")
        self.left(210)
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def go_left(self):
        new_x = self.xcor() - 20
        if new_x < -200:
            new_x = self.xcor()
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        if new_x > 200:
            new_x = self.xcor()
        self.goto(new_x, self.ycor())
