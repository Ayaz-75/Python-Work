import pandas as pd

# import csv
#
# with open('weather-data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


# data = pd.read_csv('weather-data.csv')

# print(data['temp'])
# data_dict = data.to_dict()

# temp_list = data['temp'].to_list()

# print(data_dict)
# print(temp_list)
# total = 0
# avg = 0
# for item in temp_list:
#     total += item
#     avg = total/len(temp_list)
#
# print(avg)

# print(data['temp'].mean())
# print(data['temp'].max())
# print(data[data['day'] == 'Monday'])
#
# print(data[data['temp'] == data.temp.max()])

# new_dict = {
#     'students': ['ayaz', 'aaqib', 'turab'],
#     'scores': [75, 85, 95]
# }
#
# data_f = pd.DataFrame(new_dict)
# data_f.to_csv('new_csv_file.csv')
#
#
#
# new_dict2 = [
#     {'name': 'Ayaz', 'roll_no': 75, 'marks': 75},
#     {'name': 'Aaqib', 'roll_no': 1, 'marks': 85},
#     {'name': 'Turab', 'roll_no': 45, 'marks': 95}
# ]
#
# data_f2 = pd.DataFrame(new_dict2)
# data_f2.to_csv('new_data_f2.csv')
# print(data_f2)
#
# print(data_f)


data = pd.read_csv('2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')

gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])

print(gray_count)
print(cinnamon_count)
print(black_count)

data_dict = {
    'Fur_color': ['Gray', 'Cinnamon', 'Black'],
    'count': [gray_count, cinnamon_count, black_count]
}

new_df = pd.DataFrame(data_dict)
print(new_df)
new_df.to_csv('squirrel_count.csv')
