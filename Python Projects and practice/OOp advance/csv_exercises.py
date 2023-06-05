import csv

# Python program to read each row from a given csv file and print a list of strings
'''with open("data.csv") as file:
    reader = csv.reader(file)
    data_list = list(reader)
print(data_list)'''

# Python program to read a given CSV file having tab delimiter and list
'''with open('new_data.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter='\t')
    for row in data:
        print(', '.join(row))
    data_list = list(data)

print(data_list)'''

# Python program to read a given CSV file as a dictionary
with open('new_data.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile, delimiter='\t')
    for row in data:
        print(row)

