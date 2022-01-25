from typing import List
import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "day25\\blank_states_img.gif"
screen.setup(725, 491)
screen.addshape(image)

turtle.shape(image)
"""
# se quiser pegar coordenadas atraves de cliques
def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
"""
csv_file = "day25\\50_states.csv"
data = pandas.read_csv(csv_file)
all_states = data.state.to_list()

guessed_states: List = []

while len(guessed_states) < 50:
    answer_state = str(screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )).title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("day25\\states_learn.csv")
        break

    # if answer_state is one of the states in all the states
    # of the 50_states.csv
    #       if they got it right:
    #           Create a turtle to write the name of the state at the
    #           state's x and y coordate.
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = (data[data.state == answer_state])
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
