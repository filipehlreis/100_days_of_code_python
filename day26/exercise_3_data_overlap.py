with open("file1.txt") as file1:
    data1 = file1.readlines()

with open("file2.txt") as file2:
    data2 = file2.readlines()


result = [int(data.strip()) for data in data1 if data in data2]

# Write your code above 👆

print(result)
