import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


""" PROJECT DAY 26 """
# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_alphabet = pandas.read_csv("day26\\nato_phonetic_alphabet.csv")
# print(nato_alphamet)

nato_dict = {row.letter: row.code for (_, row) in nato_alphabet.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user
# inputs.
while True:
    string = input("\nEnter a word: ").upper()
    if string == 'EXIT':
        break
    word_nato = [nato_dict[letter] for letter in string]
    print(word_nato)
