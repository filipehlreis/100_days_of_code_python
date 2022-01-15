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


def check_answer(history, score):
    awnser_guess = input(
        "\nWho has more followers? Type 'A' or 'B': ").lower()

    if history[-2]['follower_count'] > history[-1]['follower_count']:
        awnser_correct = 'a'
    else:
        awnser_correct = 'b'

    if awnser_correct != awnser_guess:
        clear()
        print(logo)
        print(f"\nSorry, that's wrong. Final score: {score}")
        return False
    return True


def print_compare(history):
    print(f"Compare A: "
          f"{history[-2]['name']}, "
          f"a {history[-2]['description']}, "
          f"from {history[-2]['country']}.")
    print(vs)
    print(f"Against B: "
          f"{history[-1]['name']}, "
          f"a {history[-1]['description']}, "
          f"from {history[-1]['country']}.")
    return


def game():
    history = []
    should_continue = True
    score = 0
    max_score = len(data)
    history.append(pick_a_data(data, history))

    while should_continue and (score < max_score):
        clear()
        print(logo)

        history.append(pick_a_data(data, history))

        if score > 0:
            print(f"\nYou're right! Your current score is: {score}\n")
        else:
            print('\n\n')

        print_compare(history)

        should_continue = check_answer(history, score)
        score += 1

    return


game()
