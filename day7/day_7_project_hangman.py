import random
from hangman_words import msg_already_guessed, msg_status, msg_wrong_guess
from hangman_words import word_list
from hangman_art import logo
from replit import clear


chosen_word = random.choice(word_list)
word_len = len(chosen_word)
lives = 6

# Create blanks
display = []
already_guessed = []
for _ in range(word_len):
    display.append('_')

clear()
print(logo)
print('\n')
msg_status(lives, display)


while "_" in display and lives:
    print(chosen_word)

    guess = input('\nAdivinhe uma letra: ').lower()
    clear()

    print(logo)

    if guess not in chosen_word:
        lives -= 1
        msg_wrong_guess(guess)
    else:
        if guess not in already_guessed:
            # Check guessed letter
            for position in range(word_len):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
            already_guessed.append(guess)
            print('\n')
        else:
            msg_already_guessed(guess)

    msg_status(lives, display)
else:
    if lives:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
