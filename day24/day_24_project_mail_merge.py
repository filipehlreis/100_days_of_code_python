"""
TODO: Create a letter using starting_letter.docx
for each name in invited_names.txt
Replace the [name] placeholder with the actual name.
Save the letters in the folder "ReadyToSend".

Hint1: This method will help you:
https://www.w3schools.com/python/ref_file_readlines.asp
    Hint2: This method will also help you.
    https://www.w3schools.com/python/ref_string_replace.asp
        Hint3: This method will also help you.
        https://www.w3schools.com/python/ref_string_strip.asp
"""
file_directory_starting_letter = "day24\\Input\\Letters\\starting_letter.txt"
file_directory_invited_names = "day24\\Input\\Names\\invited_names.txt"
folder_ready = "day24\\Output\\ReadyToSend"

with open(file_directory_invited_names) as file:
    list_names = file.readlines()

with open(file_directory_starting_letter) as file:
    texto = file.read()

for name in list_names:
    name = name.strip()
    with open(f"{folder_ready}\\letter_for_{name}.txt", mode="w") as file:
        file.write(texto.replace("[name]", name))
