student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for names in student_scores:
    score = student_scores[names]
    if 90 < score < 100:
        student_grades[names] = "outstanding"

    elif 80 < score < 90:
        student_grades[names] = "exceeds expectations"

    elif 70 < score < 80:
        student_grades[names] = "acceptable"

    elif 60 < score < 70:
        student_grades[names] = "fail"

# 🚨 Don't change the code below 👇
print(student_grades)
