import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    pass
    # print(value)


student_data_frama = pandas.DataFrame(student_dict)
# print(student_data_frama)

# Looping through a data frame
for (key, value) in student_data_frama.items():
    # print(value)
    ...


# loop through rows of a data frame
for (index, row) in student_data_frama.iterrows():
    if row.student == "Angela":
        print(row.score)
