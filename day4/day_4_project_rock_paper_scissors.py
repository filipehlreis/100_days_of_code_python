import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
won = '''

██    ██  ██████  ██    ██     ██     ██  ██████  ███    ██ 
 ██  ██  ██    ██ ██    ██     ██     ██ ██    ██ ████   ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██    ██ ██ ██  ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██    ██ ██  ██ ██ 
   ██     ██████   ██████       ███ ███   ██████  ██   ████ 
'''

lost = '''

██    ██  ██████  ██    ██     ██       ██████  ███████ ████████ 
 ██  ██  ██    ██ ██    ██     ██      ██    ██ ██         ██    
  ████   ██    ██ ██    ██     ██      ██    ██ ███████    ██
   ██    ██    ██ ██    ██     ██      ██    ██      ██    ██
   ██     ██████   ██████      ███████  ██████  ███████    ██
'''
tied = '''

██    ██  ██████  ██    ██     ████████ ██ ███████ ██████
 ██  ██  ██    ██ ██    ██        ██    ██ ██      ██   ██ 
  ████   ██    ██ ██    ██        ██    ██ █████   ██   ██ 
   ██    ██    ██ ██    ██        ██    ██ ██      ██   ██ 
   ██     ██████   ██████         ██    ██ ███████ ██████  
'''


hand_signs = [rock, paper, scissors]

user_choise = int(input('\n\nWhat do you choose? Type 0 for Rock, 1 for '
                        'Paper or 2 for Scissors.\n'))
computer_choise = random.randint(0, 2)

if (user_choise >= 3) or (user_choise < 0):
    print(f'You chose an invalid number, so:{lost}')
else:
    result = f'\n\nYou chose:{hand_signs[user_choise]}\nComputer chose:'\
             f'{hand_signs[computer_choise]}\n\nResult:'

    if user_choise == computer_choise:
        print(result + tied)
    elif user_choise == 0 and computer_choise == 1:
        print(result + lost)
    elif user_choise == 1 and computer_choise == 2:
        print(result + lost)
    elif user_choise == 2 and computer_choise == 0:
        print(result + lost)
    else:
        print(result + won)
