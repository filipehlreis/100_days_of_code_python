import random
# Step 2
word_list = ['camelo', 'dentista', 'sorvete', 'papagaio', 'televisao', 'bola']
chosen_word = random.choice(word_list)

# Testing code
print(f'Chosen_word: {chosen_word}')

# TODO - Create an empty List called display.
#        For each letter in the chosen_word, add a "_" to 'display'.
#        So if the chosen_word was "apple", display should be
#        ['_','_','_','_','_'] with 5 "_" representing each letter to guess.
word_len = len(chosen_word)

display = []
for _ in range(word_len):
    display.append('_')
print(display)

guess = input('Adivinhe uma letra: ').lower()

# TODO - Loop through each position in the chosen_word;
#        If the letter at that position matches 'guess' then reveal that letter
#        in the display at that position.
#        e.g. If the user guessed "p" and the chosen_word was "apple", then
#        display should be ['_','p','p','_','_'].
for position in range(word_len):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter


# TODO - Print 'display' and you should see the guessed letter in the correct
#        position and every other letter replace with "_".
#        HINT - Don't worry about getting the user to guess the next letter.
#               We'll tackle that in step 3.
print(display)
