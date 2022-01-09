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
        if letter in alphabet:
            position = alphabet.index(letter)
            new_text += alphabet[position+shift]
        else:
            new_text += letter

    print()
    if direction == 'encode':
        print(f"The encoded text is '{new_text}'")
    else:
        print(f"The decoded text is '{new_text}'")


anwser_reboot = True

while anwser_reboot:
    clear()

    print(logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    caesar(text, shift, direction)

    anwser_reboot_input = input('\nType "yes" if you want to go again.\n'
                                'Otherwise, type "no"\n').lower()
    if anwser_reboot_input == 'no':
        print('Goodbye!')
        anwser_reboot = False
