import csv
file = csv.reader(open(" Names.csv"))
tmp = []
for row in file:
    tmp.append(row)

print(tmp)
