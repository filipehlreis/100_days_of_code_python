import random
# Step 3

word_list = ['camelo', 'dentista', 'sorvete', 'papagaio', 'televisao', 'bola']
chosen_word = random.choice(word_list)
word_len = len(chosen_word)

# Testing code
print(f'Chosen_word: {chosen_word}')

# Create blanks
display = []
for _ in range(word_len):
    display.append('_')
print(display)

# TODO - Use a while loop to let the user guess again. The loop should only
#        once the user has guessed all the letters in the chosen_word and
#        'display' has no more blanks ('_'). Then you can tell the user they've
#        won.
while "_" in display:
    guess = input('Adivinhe uma letra: ').lower()

    # Check guessed letter
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

else:
    print('You won!')
