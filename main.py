# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1]!= "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

"""Check what kind of data you are working with"""

# data = pandas.read_csv("weather_data.csv")
# print(type(data))

# print(data["temp"])

"""Convert data to a dictionary"""
# data_dict = data.to_dict()
# # print(data_dict)

"""Convert data to a list"""
# temp_list = data["temp"].to_list()
# print(temp_list)

"""Calculate the average temperature"""

# average = sum(temp_list) / len(temp_list))
# print(average)

"""Find the day with the highest temperature"""
# max_temp = data["temp"].max()
# print(max_temp)


"""Find the day with the lowest temperature"""
# print(data.condition)

# print(data[data.day == "Monday"])

# challenge: pull out the row of data where the temperature was the highest

# max_temp = data["temp"].max()

# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# print(monday.condition)

"""Convert weather temp from Celsius to Fahrenheit"""
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = (monday_temp * 9/5) + 32
# print(monday_temp_f)


"""Create a dataframe from scratch"""
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)


"""Export the dataframe to a CSV"""
# data.to_csv("new_data.csv")

"""Export the dataframe to an Excel file"""
# data.to_excel("new_data.xlsx", sheet_name="students")

