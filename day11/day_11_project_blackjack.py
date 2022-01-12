from __future__ import annotations
from random import choice
from art import logo
from replit import clear

# ############## Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############## Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

# #################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


def print_status(score_user, cards_user, score_computer, cards_computer,
                 play_user):
    print(f'you      - score: {score_user:2}   cards: {cards_user}')
    if play_user:
        print(f"computer - score:  x   cards: "
              f"[{cards_computer[0]}, 'x']\n ")
    else:
        print(f'computer - score: {score_computer:2}   cards: '
              f'{cards_computer}\n ')


msg_computer_wins = "You lose because computer has 21."
msg_user_wins = "You wins because you have 21."
msg_game_draw = "It's a draw. Nobody wins!"
msg_user_lose_over_21 = "You lose because you have more than 21."
msg_computer_lose_over_21 = "You win because computer have more than 21."
msg_user_higher = "You win because you have more than computer."
msg_computer_higher = "You lose because you have less than computer."

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

should_game_continue = 1

while should_game_continue:
    clear()
    print(logo)

    cards_user = []
    cards_computer = []

    score_user = 0
    score_computer = 0

    cards_user.append(choice(cards))
    cards_user.append(choice(cards))
    cards_computer.append(choice(cards))
    cards_computer.append(choice(cards))

    score_computer = sum(cards_computer)
    score_user = sum(cards_user)
    play_user = 1

    print_status(score_user, cards_user, score_computer,
                 cards_computer, play_user)

    should_user_continue = 1

    if score_computer == 21:
        print(msg_computer_wins)
    elif score_user == 21:
        print(msg_user_wins)
    else:
        while should_user_continue:
            score_user = sum(cards_user)
            if score_user > 21:
                if 11 in cards_user:
                    index_ace = cards_user.index(11)
                    cards_user[index_ace] = 1
                    score_user = sum(cards_user)
                    print(f'you      - score: {score_user:2}   cards: '
                          f'{cards_user} - ACE changed')
                else:
                    should_user_continue = 0
            else:
                draw_another_card = input("\nDo you want do draw another card?"
                                          " Type 'yes' or 'no' ").lower()
                print()
                if draw_another_card == 'yes':
                    cards_user.append(choice(cards))
                    score_user = sum(cards_user)

                    print_status(score_user, cards_user,
                                 score_computer, cards_computer, play_user)

                    if score_user == 21:
                        print(msg_user_wins)

                else:
                    should_user_continue = 0

        play_user = 0
        if score_user > 21:
            print(msg_user_lose_over_21)
        else:
            print_status(score_user, cards_user,
                         score_computer, cards_computer, play_user)
            while score_computer < 17:
                cards_computer.append(choice(cards))
                score_computer = sum(cards_computer)

                if score_computer > 21:
                    if 11 in cards_computer:
                        index_ace = cards_computer.index(11)
                        cards_computer[index_ace] = 1
                        score_computer = sum(cards_computer)
                        print(f'computer - score: {score_computer:2}   '
                              f'cards: {cards_computer} - ACE changed')
                        score_computer = sum(cards_computer)

                print_status(score_user, cards_user,
                             score_computer, cards_computer, play_user)

            if score_computer == 21:
                print(msg_computer_wins)
            elif score_computer > 21:
                print(msg_computer_lose_over_21)
            elif score_computer == score_user:
                print(msg_game_draw)
            elif score_computer > score_user:
                print(msg_computer_higher)
            elif score_computer < score_user:
                print(msg_user_higher)

    answer_game_continue = input("\n\nType 'n' to exit the game. ").lower()
    if answer_game_continue == 'n':
        should_game_continue = 0
