ENCODE_MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    ' ': '   ',
    '\n': '   ',
}


DECODE_MORSE_CODE = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V', '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '--..--': ', ',
    '.-.-.-': '.', '..--..': '?',
    '-..-.': '/',
    '-....-': '-',
    '-.--.': '(',
    '-.--.-': ')',
}


def encodeMorse(text: str):
    text = text.upper()
    print(text)
    morse_code = ''
    for letter in text:
        morse_code += ENCODE_MORSE_CODE[letter]
        morse_code += ' '
    print(f'{morse_code[:-1]}')
    return f'{morse_code[:-1]}'


def decodeMorse(morse_code: str):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    morse_code_words = morse_code.split('  ')
    morse_code_words = [x for x in morse_code_words if x != '']
    word = ''
    for words in morse_code_words:
        morse_code_words_dec = ''.join(words).split()
        for letter in morse_code_words_dec:
            word += DECODE_MORSE_CODE[letter]
        word += ' '
    return f'{word[:-1]}'


texto = """
This is a place to journal your experience of completing this project. This will help you figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve for the next project? What was your biggest learning from today? What would you do differently if you were to tackle this project again?
"""


if __name__ == "__main__":
    print(decodeMorse(encodeMorse(texto)))
