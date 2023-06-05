# with open('weather_data.csv') as file:
#     data = file.readlines()
#
# print(data)
# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for each_row in data:
#         if each_row[1] != 'temp':
#             temps = each_row[1]
#             temperatures.append(temps)
#
# print(temperatures)

import pandas as pd
data = pd.read_csv('weather_data.csv')
data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()

print(data['temp'].mean())
add = 0
avg = 0
for item in temp_list:
    add += item
    avg = add/len(temp_list)

print(avg)
print(data['temp'].max())

print(temp_list)
