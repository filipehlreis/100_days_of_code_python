# file = open("C:\\github\\100_days_of_code_python\\day24\\my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

############
# with open("C:\\github\\100_days_of_code_python\\day24\\my_file.txt") as file:
#     contents = file.read()
# print(contents)

############
file_directory = """
C:\\github\\100_days_of_code_python\\day24\\the_snake_game_improved\\"""

file_directory = "C:\\github\\100_days_of_code_python\\day24\\"

with open(f"{file_directory}new_file.txt", mode="a") as file:
    file.write("\nnew text")
