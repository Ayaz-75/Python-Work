import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

fur_color = data['Primary Fur Color']

gray_counts = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_counts = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_counts = len(data[data['Primary Fur Color'] == 'Black'])

# print(black_counts)
# print(gray_counts)
# print(cinnamon_counts)

squirrel_counts_dictionary = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'count': [gray_counts, cinnamon_counts, black_counts]
}


df = pd.DataFrame(squirrel_counts_dictionary)

df.to_csv('updated_squirrel_counts.csv', index=False)




# black = []
# gray = []
# cinnamon = []
#
# for color in fur_color:
#     if color == 'Black':
#         black.append(color)
#
#     elif color == 'Gray':
#         gray.append(color)
#
#     else:
#         cinnamon.append(color)
#
#
# black_counts = len(black)
# gray_counts = len(gray)
# cinnamon_counts = len(cinnamon)
#
# squirrel_dict = {
#     "Black_counts": [black_counts],
#     "Gray_counts": [gray_counts],
#     "Cinnamon_counts": [cinnamon_counts],
# }
#
# data_frame = pd.DataFrame(squirrel_dict)
# data_frame.to_csv('squirrel_counts')
#
