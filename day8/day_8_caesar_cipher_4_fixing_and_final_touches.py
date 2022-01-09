from replit import clear
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']


def caesar(text, shift, direction):
    new_text = ''
    shift = shift % 26
    if direction != 'encode':
        shift = - shift

    for letter in text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text
        # is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if letter in alphabet:
            position = alphabet.index(letter)
            new_text += alphabet[position+shift]
        else:
            new_text += letter

    print()
    if direction == 'encode':
        print(f"The encoded text is {new_text}")
    else:
        print(f"The decoded text is {new_text}")


# TODO-1: Import and print the logo from art.py when the program starts.

# TODO-4: Can you figure out a way to ask the user if they want to restart
# the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and
# call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program
# if the user types 'yes'.

anwser_reboot = True

while anwser_reboot:
    clear()

    print(logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    anwser_reboot_input = input('\nType "yes" if you want to go again.\n'
                                'Otherwise, type "no"\n').lower()
    if anwser_reboot_input == 'no':
        print('Goodbye!')
        anwser_reboot = False
