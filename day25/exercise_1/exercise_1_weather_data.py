

# # import csv
# import pandas
# weather_data_directory = "day25\\weather_data.csv"
# # with open(weather_data_directory) as weather_data:
# #     weather_data_list = weather_data.readlines()

# # for indice in range(len(weather_data_list)):
# #     weather_data_list[indice] = weather_data_list[indice].strip()

# # print(weather_data_list)

# # ########################################################################
# # with open(weather_data_directory) as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))

# #     print(temperatures)

# # ########################################################################


# data = pandas.read_csv(weather_data_directory)
# # # print(data["temp"])
# # data_dict = data.to_dict()
# # print(data_dict)

# # temp_list = data["temp"].to_list()
# # print(temp_list)

# # average = round(sum(temp_list) / len(temp_list), 2)
# # average = sum(temp_list) / len(temp_list)
# # print(average)

# # average2 = data["temp"].mean()
# # print(average2)

# # max = data["temp"].max()
# # print(max)

# # #  Get Data in Columns
# # print(data["condition"])
# # print(data.condition)


# # print('\n\n')
# # #  Get Data in Rows
# # print(data[data.day == "Monday"])

# # # Get data where temperatures is the max
# # print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# print(monday.condition)
# # (0 °C × 9/5) + 32 = 32 °F
# monday_temp_F = (monday.temp * 9 / 5) + 32
# print(monday_temp_F)


# # Create a dataframe from scracth

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "score": [76, 56, 65],
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("day25\\new_data.csv")


# ###################################################

import pandas

file_squirrel = "day25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

data = pandas.read_csv(file_squirrel)
data_color = data["Primary Fur Color"]

# print(data_color)
data_color_pandas = data_color.value_counts()
# print(data_color_pandas)

data_color_pandas.to_csv("day25\\count_squirrel.csv")


# ###############
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("day25\\count_squirrel_teache.csv")
