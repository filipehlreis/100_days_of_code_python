alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    text_encrypted = ''
    shift = shift % 25
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if (position + shift) > 25:
                position = (position + shift) % 25 - 2
            text_encrypted += alphabet[position+shift]
        else:
            text_encrypted += letter
    print(f"The encoded text is {text_encrypted}")


def decrypt(text, shift):
    text_encrypted = ''
    shift = shift % 25
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if (position - shift) < 0:
                position = (position - shift) % 25 + 2
            text_encrypted += alphabet[position-shift]
        else:
            text_encrypted += letter
    print(f"The decoded text is {text_encrypted}")


# TODO-1: Create a different function called 'decrypt' that takes the 'text'
#  and 'shift' as inputs.

#    TODO-2: Inside the 'decrypt' function, shift each letter of the 'text'
#            *backwards* in the alphabet by the shift amount and print the
#            decrypted text.
#    e.g.
#    cipher_text = "mjqqt"
#    shift = 5
#    plain_text = "hello"
#    print output: "The decoded text is hello"

# TODO-3: Check if the user wanted to encrypt or decrypt the message by
#         checking the 'direction' variable. Then call the correct function
#         based on that 'drection' variable. You should be able to test the
#         code to encrypt *AND* decrypt a message.
if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)
