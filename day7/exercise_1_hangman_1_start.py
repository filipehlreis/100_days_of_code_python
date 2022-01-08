import random
# Step 1
word_list = ['camelo', 'dentista', 'sorvete', 'papagaio', 'televisao', 'bola']

# TODO - Randomly choose a word from the word_list and assign it to a variable
#        called chosen_word

chosen_word = random.choice(word_list)
print(f'Chosen_word: {chosen_word}')

# TODO - Ask the user to guess a letter and assign their answer to a variable
#        called guess. Make guess lowercase.
# guess = str.lower(input('Adivinhe uma letra: '))
guess = input('Adivinhe uma letra: ').lower()

# TODO - Check if the letter the user guessed (guess) is one of the letters
#        in the chosen_word.

for letter in chosen_word:
    print(letter)
    if letter == guess:
        print('Certo.')
    else:
        print('Errado.')
