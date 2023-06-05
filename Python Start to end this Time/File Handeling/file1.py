"""
105
Write a new file called “Numbers.txt”. Add five numbers to the document
which are stored on the same line and only separated by a comma. Once you
have run the program, look in the location where your program is stored, and you
should see that the file has been created. The easiest way to view the contents
of the new text file on a Windows system is to read it using Notepad.

"""
# fin = open('D:\Python Start to end this Time\File Handeling\ Numbers.txt', 'w')
# fin.write('1, ')
# fin.write('2, ')
# fin.write('3')
#
# fin.close()

# fin = open('D:\Python Start to end this Time\File Handeling\ Numbers.txt', 'r')

# print(fin.read())

'''
106 
Create a new file called “Names.txt”. Add five names to the 
document, which are stored on separate lines. Once you have 
run the program, look in the location where your program is 
stored and check that the file has been created properly. 
'''

# fin1 = open('D:\Python Start to end this Time\File Handeling\ Names.txt', 'w')
# fin1.write('Ayaz, ')
# fin1.write('Zahoor, ')
# fin1.write('Aaqib, ')
#
# fin1.close()

'''
108 
Open the Names.txt file. Ask the user to input a new name. Add this to the end of the file and 
display the entire file. 

'''
# user_input = input('Enter an other name: ')
# fin1 = open('D:\Python Start to end this Time\File Handeling\ Names.txt', 'a')
# fin1.write(user_input)
#
# fin1 = open('D:\Python Start to end this Time\File Handeling\ Names.txt', 'r')
# print(fin1.read())


'''
109 
Display the following menu to the user: 
1) Create a new file
2) Display the file
3) Add a new item to file
Make a selection 1, 2 or 3: 


Ask the user to enter 1, 2 or 3. If they select anything other than 1, 2 or 3 it should display a 
suitable error message. If they select 1, ask the user to enter a school subject and save it to a new file called 
“Subject.txt”. It should overwrite any existing file with a new file. If they select 2, display the contents of the 
“Subject.txt” file. If they select 3, ask the user to enter a new subject and save it to the file and then display 
the entire contents of the file. Run the program several times to test the options.
'''

print(f"1) Create a new file\n2)Display the file\n3)Add a new item to file")
user_input = int(input("Make a selection 1, 2 or 3: "))

if user_input == 1:
    new_file = open('D:\Python Start to end this Time\File Handeling\Subject.txt', 'w')
    new_file.write('Math, ')

    new_file.close()

elif user_input == 2:
    new_file = open('D:\Python Start to end this Time\File Handeling\Subject.txt', 'r')
    print(new_file.read())

elif user_input == 3:
    new_file = open('D:\Python Start to end this Time\File Handeling\Subject.txt', 'a')
    new_file.write('Science')

else:
    print("Invalid input")
