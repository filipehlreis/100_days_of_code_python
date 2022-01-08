import random
# Step 4
stages = ["""
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      / \\
 |
_|___
""", """
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      /
 |
_|___
""", """
  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      
 |
_|___
""", """
  _______
 |/      |
 |      (_)
 |      \|
 |       |
 |      
 |
_|___
""", """
  _______
 |/      |
 |      (_)
 |       |
 |       |
 |      
 |
_|___
""", """
  _______
 |/      |
 |      (_)
 |      
 |       
 |      
 |
_|___

""", """
  _______
 |/      |
 |      
 |      
 |       
 |      
 |
_|___

"""
          ]

word_list = ['camelo', 'dentista', 'sorvete', 'papagaio', 'televisao', 'bola']
chosen_word = random.choice(word_list)
word_len = len(chosen_word)

# TODO - Create a variable called 'lives' to keep track of the number of lives
#        left. Set 'lives' to equal 6.
lives = 6
print(f'stages + {len(stages)}')
# Testing code
print(f'Chosen_word: {chosen_word}')

# Create blanks
display = []
for _ in range(word_len):
    display.append('_')
print(display)

print(f'\nVidas restantes: {lives}{stages[lives]}')

while "_" in display and lives:
    guess = input('Adivinhe uma letra: ').lower()

    # Check guessed letter
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # TODO - If guess is not a letter in the chosen_word, then reduce 'lives'
    #        by 1. If lives goes down to 0 then the game should stop and it
    #        should print "You lose."

    if guess not in chosen_word:
        lives -= 1

    # TODO - print the ASCII art from 'stages' that corresponds to the current
    #        number of 'lives' the user has remaning.

    print(f'\nVidas restantes: {lives}{stages[lives]}')
    # Join all the elements in the list and turn it into a String.

    print(f'{" ".join(display)}')
else:
    if lives:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
