# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\n\nWelcome to the PyPassword Generator!")
nr_letters_input = int(
    input("How many letters would you like in your password?\n"))
nr_symbols_input = int(input("How many symbols would you like?\n"))
nr_numbers_input = int(input("How many numbers would you like?\n"))
print('')

total_charact = nr_letters_input + nr_numbers_input + nr_symbols_input

# TODO: Needs to make a better randomination

for x in range(1, 31):
    nr_numbers = nr_numbers_input
    nr_symbols = nr_symbols_input
    nr_letters = nr_letters_input
    password = ''
    token = 1

    for charact in range(0, total_charact):
        # rand = random.randint(0, 600) % 3
        rand = int(random.choice(['0', '1', '2']))

        if rand and nr_letters:
            rand_letters = random.randint(0, len(letters))
            password += letters[rand_letters-1]
            nr_letters -= 1

        elif nr_symbols and token:
            rand_symbols = random.randint(0, len(symbols))
            password += symbols[rand_symbols-1]
            nr_symbols -= 1
            token = 0

        elif nr_numbers and token:
            rand_numbers = random.randint(0, len(numbers))
            password += numbers[rand_numbers-1]
            nr_numbers -= 1
            token = 0

        elif nr_numbers:
            rand_numbers = random.randint(0, len(numbers))
            password += numbers[rand_numbers-1]
            nr_numbers -= 1
            token = 1

        elif nr_symbols:
            rand_symbols = random.randint(0, len(symbols))
            password += symbols[rand_symbols-1]
            nr_symbols -= 1
            token = 1

        elif nr_letters:
            rand_letters = random.randint(0, len(letters))
            password += letters[rand_letters-1]
            nr_letters -= 1

    print(f'Password{x:4}:    {password}')
