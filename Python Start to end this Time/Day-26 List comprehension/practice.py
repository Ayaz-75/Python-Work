
# dictionary = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}
#
# new_dict = {key: (value**2) for (key, value) in dictionary.items()}
# print(new_dict)


import pandas as pd
new_dictionary = {
    'students': ['Ayaz', 'Naresh', 'Ayoob', 'Aaqib'],
    'scores': [95, 85, 75, 73]
}


data_f = pd.DataFrame(new_dictionary)

for (index, row) in data_f.iterrows():
    if row.students == 'Naresh':
        print(row.scores)

# print(data_f)
