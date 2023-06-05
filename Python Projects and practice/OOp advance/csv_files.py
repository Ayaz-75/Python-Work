import csv

'''with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Id", "Batch"])
    writer.writerow(["Ayaz", "18cs75", 18])
    writer.writerow(["Zahoor", "18cs61", 18])'''

with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
