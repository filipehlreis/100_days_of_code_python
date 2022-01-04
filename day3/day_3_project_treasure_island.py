print('''
 _                                           _                 _
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 
''')

print('Welcome to Treasure Island!')
print('Your mission is to find the treasure.')
first_choise = input(
    '\nYou\'re at a cross road. Where do you want to go? Type "left" '
    'or "right".\n')\
    .lower()

if first_choise == 'left':
    second_choise = input(
        '\nYou come to a lake. There is an island in the middle of the lake.'
        '\nType "wait" to wait for a boat.\nType "swim" to swim across.\n')\
        .lower()

    if second_choise == 'wait':
        third_choise = input(
            '\nYou arrive at the island unharmed.\nThere is a house with 3 '
            'doors.\nOne "red", one "yellow" and one "blue".\nWhich colour do '
            'you choose?\n')\
            .lower()

        if third_choise == 'yellow':
            print('Congratulations!!! You find a big treasure!')
        else:
            print('You entered a room of beasts. Game Over!')
    else:
        print('You don\'t know how to swim and drowned. Game Over!')
else:
    print('You came across a tiger and died. Game Over!')
