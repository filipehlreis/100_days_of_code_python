from random import randint
from replit import clear
from art import logo


def print_status():
    print(f"You have {attempts_remaining} attempts "
          f"remaining to guess the number.")


clear()
print(logo)

msg_welcome = "Welcome to the Number Guessing Game!"
msg_introdution = "I'm thinking of a number between 1 and 100."
msg_asking_difficulty = "Choose a difficulty. Type 'easy' or 'hard': "


print(msg_welcome)
print(msg_introdution)
difficulty_level = input(msg_asking_difficulty).lower()
print()

if difficulty_level == 'hard':
    attempts_remaining = 5
else:
    attempts_remaining = 10

number_thinked = randint(1, 100)
guess_number = 0
should_continue_guessing = True

while should_continue_guessing:
    print_status()
    print()
    guess_number = int(input('Make a guess: '))

    if guess_number == number_thinked:
        print('\nCongratulations!!! You won!!!')
        should_continue_guessing = False
    else:
        attempts_remaining -= 1
        if attempts_remaining < 1:
            should_continue_guessing = False
            print('You lost.')
            print(f"The number thinked was {number_thinked}.")
        elif guess_number > number_thinked:
            print('Too high.')
        elif guess_number < number_thinked:
            print('Too low.')
