import pandas

data = pandas.read_csv("day30\\NATO\\nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


while True:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)
        break
