student_score = {
    'Turab': 81,
    'Danish': 78,
    'Aaqib': 99,
    'Zahoor': 74,
    'Ayaz': 62
}
new_dictionary = student_score

for student in student_score:
    score = student_score[student]
    if 90 < score < 100:
        student_score[student] = "Excellent"
    elif 70 < score < 90:
        student_score[student] = 'Good'
    elif 50 < score < 70:
        student_score[student] = 'Acceptable'
    elif score < 50:
        student_score[student] = 'Fail'
    else:
        print('Invalid score')


print(student_score)
