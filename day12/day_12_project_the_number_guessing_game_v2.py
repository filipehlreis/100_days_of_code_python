from art import logo
from replit import clear
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    # Function to check user's guess against actual answer.
    if guess > answer:
        print('Too  high.')
        return turns - 1
    elif guess < answer:
        print('Too low')
        return turns - 1
    else:
        print(f'You got it! The answer was {answer}.')
    return turns


def set_difficulty():
    # Make function to set difficulty.
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'hard':
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS


def game():
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Choosing a random number between 1 and 100
    answer = randint(1, 100)

    # Debug
    # print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.\n")

        # Let the user guess a number
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns < 1:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
