from __future__ import annotations
from replit import clear
from random import choice

from art import vs, logo
from game_data import data


def pick_a_data(data, history):
    choosed = choice(data)
    while choosed in history:
        choosed = choice(data)
    return choosed


def check_answer(history):
    awnser_guess = input(
        "Who has more followers? Type 'A' or 'B': ").lower()

    if history[-2]['follower_count'] > history[-1]['follower_count']:
        awnser_correct = 'a'
    else:
        awnser_correct = 'b'

    if awnser_correct != awnser_guess:
        print('You lost.')
        return False
    return True


def game():
    history = []
    should_continue = True

    while should_continue:
        clear()
        print(logo)

        history.append(pick_a_data(data, history))
        history.append(pick_a_data(data, history))

        print(f"Compare A: "
              f"{history[-2]['name']}, "
              f"a {history[-2]['description']}, "
              f"from {history[-2]['country']}.")
        print(vs)
        print(f"Against B: "
              f"{history[-1]['name']}, "
              f"a {history[-1]['description']}, "
              f"from {history[-1]['country']}.")

        a = history[-2]['follower_count']
        b = history[-1]['follower_count']
        print(f"{a} > {b}")

        should_continue = check_answer(history)
    return


game()
