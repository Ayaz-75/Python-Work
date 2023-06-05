import pandas as pd
data = pd.read_csv('weather_data.csv')
data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()

# print(data['temp'].mean())
add = 0
avg = 0
for item in temp_list:
    add += item
    avg = add/len(temp_list)

# print(avg)
# print(data['temp'].max())
#
# print(temp_list)
max_temp = data['temp'].max()
to_f = max_temp * 1.8000 + 32.00

monday = data[data.day == 'Monday']
maximum_temperature = data[data.temp == max_temp]
print(to_f)

# print(maximum_temperature)