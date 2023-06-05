import csv

fil_e = open('D:\Python Start to end this Time\File Handeling\ Names.csv', 'w')

new_item = "Ayaz, 75 \n"

fil_e.write(str(new_item))

fil_e.close()

fil_e = open('D:\Python Start to end this Time\File Handeling\ Names.csv', 'a')
new_item = "Aaqib, 01\nTurab, 45\nZahoor, 61"
fil_e.write(str(new_item))

file = open(' Names.csv', 'a')

name = input("Enter your name: ")
age = input('Enter Age: ')

new_record = name + ", " + age + " \n"


file.write(str(new_record))

file.close()
