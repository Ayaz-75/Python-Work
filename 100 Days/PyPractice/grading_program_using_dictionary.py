student_score = {
    "ayaz": 81,
    "wassi": 78,
    "Muzi": 99,
    "zahoor": 74,
    "asifil": 62
}

student_grades = {}
for student in student_score:
    score = student_score[student]

    if score >= 90:
        student_grades[student] = "Outstanding"

    elif score > 80:
        student_grades[student] = "Exceeds expectations"

    elif score > 70:
        student_grades[student] = "Acceptable"

    elif score < 70:
        student_grades[student] = "Fail"
print(student_grades)
