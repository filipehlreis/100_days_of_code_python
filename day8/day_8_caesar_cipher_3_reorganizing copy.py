alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function
# called caesar().


def caesar(text, shift, direction):
    new_text = ''
    shift = shift % 26
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)

            if direction == 'encode':
                if (position + shift) > 26:
                    position = (position + shift) % 26
                new_text += alphabet[position+shift]
            else:
                if (position - shift) < 0:
                    position = (position - shift) % 26
                new_text += alphabet[position-shift]
        else:
            new_text += letter

    if direction == 'encode':
        print(f"The encoded text is {new_text}")
    else:
        print(f"The decoded text is {new_text}")


caesar(text, shift, direction)
