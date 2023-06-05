"""
Create a dictionary of student and their grades.
Store 10-15 records.

1 - Find the top 2 highest scorer student
2 - Find all those students who have failed to pass the course.
3 - Display the average marks secured by students
4 - If students fail to pass the course, then print the margin by which they missed passing the exam.

Assign the margin marks to failed students.
e.g:  student marks = 45, margin marks = 5
      => student marks = 50

Note: The failing students marks should not exceed the 50 after giving margin mark
Passing marks = 50
Marks < 50 => FAIL

"""

students = {
    "Turab": 95,
    "Aaqib": 87,
    "Ayaz": 45,
    "Ayoob": 97,
    "Danish": 86,
    "Zahoor": 79,
    "Ramesh": 93,
    "Shahzaib": 85,
    "Naresh": 78,
    "Ehsan": 33,
    "Muzamil": 81,
    "Aman": 77
}
failed = {}
margin = {}
first_highest_marks = 0
second_highest_marks = 0
addition = 0
average = 0
for item in students:
    marks = students[item]
    addition += marks
    if marks > first_highest_marks:
        second_highest_marks = first_highest_marks
        first_highest_marks = marks

    if second_highest_marks < marks < first_highest_marks:
        second_highest_marks += marks

    elif marks < 50:
        failed[item] = marks
        margin[item] = 50 - marks


average += addition/len(students)
# print(students)
print(f"Highest marks are: {first_highest_marks} and {second_highest_marks} \nAverage marks: {average}")
print(f"{failed} has failed with margin: {margin}")


# are_there_other_students = True
# while are_there_other_students:
#     name_input = input("Student's name: : ")
#     marks_input = float(input("Their marks: "))
#     students[name_input] = marks_input
#     other = input("is there any other student: ")
#     if other == 'no':
#         are_there_other_students = False
