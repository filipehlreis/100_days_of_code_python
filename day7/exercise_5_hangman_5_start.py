import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear

# Step 5

# TODO - Update the word list to use the 'word_list' from hangman_words.py
#        Delete this line: word_list = ['camelo', 'dentista', 'sorvete',
#        'papagaio', 'televisao', 'bola']

chosen_word = random.choice(word_list)
word_len = len(chosen_word)

# TODO - Import the logo from hangman_art.py and print it at the start of
#        the game.
print(logo)

lives = 6
print(f'stages + {len(stages)}')


# Testing code
print(f'Chosen_word: {chosen_word}')

# Create blanks
display = []
already_guessed = []
for _ in range(word_len):
    display.append('_')
print(display)

print(f'\nVidas restantes: {lives}{stages[lives]}')

while "_" in display and lives:
    guess = input('Adivinhe uma letra: ').lower()
    clear()
    # TODO - If the letter is not in the chosen_word, print out the letter and
    #        let them know it's not in the word.
    if guess not in chosen_word:
        lives -= 1
        print(f'Você tentou "{guess}", que não está na palavra. Você perdeu uma'
              f' vida.')
    else:
        # TODO - If the user has entered a letter they've already guesse, print the
        #        letter and let them know.
        if guess not in already_guessed:
            # Check guessed letter
            for position in range(word_len):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
            already_guessed.append(guess)
        else:
            print(f'Você já adivinhou a letra "{guess}". Tente novamente.')

    # TODO - Import the stages from hangman_art.py and make this error go away.
    print(f'\nVidas restantes: {lives}{stages[lives]}')

    print(f'{" ".join(display)}')
else:
    if lives:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
