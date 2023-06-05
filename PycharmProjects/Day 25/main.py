'''import csv

with open("weather_data.csv") as data:
    # data_list = data.readlines()
    # print(data_list)
    data_list = csv.reader(data) # csv reader is used to read to list individually
    temperatures = []
    for row in data_list:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
'''

'''data_dic = data.to_dict()
print(data_dic)
temp_list = data["temp"].to_list()
# sum = 0
# for temp in temp_list:
#     sum += temp
# print(sum/len(temp_list))

avg = sum(temp_list) / len(temp_list)
print(avg)
print(data["temp"].mean())
print(data["temp"].max())

print(data["condition"])
print(data.condition)
print(data.day)
'''

# print(data[data.temp == data.temp.max()])
# print(data.max())
# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5)+32)

'''import pandas
data = pandas.read_csv("weather_data.csv")
data_dict = {
    "students": ["Ayaz", "Anwar", "Aaqib"],
    "score": [75, 80, 85]
}

data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("new_data.csv")
'''
'''import pandas
data = pandas.read_csv("cps.csv")
count_gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
count_cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
count_black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
#
# print(count_gray_squirrel)
# print(count_cinnamon_squirrel)
# print(count_black_squirrel)
data_dictionary = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [count_gray_squirrel, count_cinnamon_squirrel, count_black_squirrel]
}
df = (pandas.DataFrame(data_dictionary))
df.to_csv("squirrel color.csv")

print(df.to_csv())'''

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_l = data["temp"].to_list()

# maximum temperature in a row
# max = data[data.temp == data.temp.max()]
# print(max)

# print(data.temp.max())
# mon = data[data.day == "Monday"]
# print(mon)

# print(data)

# data_dic = data.to_dict()

# print(data_dic)
#
# avg = sum(data_l) / len(data_l)
# print(avg)
'''monday = data[data.day == "Monday"]
print((monday.temp * 9/5) + 32)

data_dic = {
    "name": ["Ayaz", "Aaqib", "Anwar"],
    "score": [80, 85, 90]
}

df = pandas.DataFrame(data_dic)
df_d = df.to_csv("Squirrel.csv")
print(df)'''


data = pandas.read_csv("cps.csv")
# print(data)
gray_count_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count_squirrel = len(data[data["Primary Fur Color"] == "Black"])

data_dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Color_count": [gray_count_squirrel, cinnamon_count_squirrel, black_count_squirrel]
}

df = (pandas.DataFrame(data_dic))
print(df.to_csv("colors squirrel.csv"))
