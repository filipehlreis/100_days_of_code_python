import random
from turtle import Screen, Turtle
import turtle

tim = Turtle()
tim.shape("turtle")
tim.color("red")
"""
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
          "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"] """


turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
tim.speed(0)
tim.width(2)

"""
for i in range(3, 11):
    tim.color(colors[i-3])
    for _ in range(i):
        tim.forward(100)
        tim.right(360/i)
"""
directions = [0, 90, 180, 270]


def random_walk_turtle():
    tim.color(random_color())
    walk_angle = random.choice(directions)
    tim.setheading(walk_angle)
    tim.forward(30)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)+1):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


def draw():
    for i in range(51):
        # random_walk_turtle()
        tim.color(random_color())
        tim.circle(120)
        tim.setheading(7.2*i)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()

# print(heroes.gen())







# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# turtle.colormode(255)
# tim.speed(0)
# tim.width(20)


# tim.setheading(270)
# tim.penup()
# tim.forward(250)
# tim.setheading(180)
# tim.forward(250)


# for _ in range(10):
#     for _ in range(10):
#         tim.setheading(0)
#         tim.color(random.choice(colors_list))
#         tim.pendown()
#         tim.circle(1)
#         tim.penup()
#         tim.forward(50)
#     tim.setheading(90)
#     tim.penup()
#     tim.forward(50)
#     tim.setheading(180)
#     tim.forward(500)
