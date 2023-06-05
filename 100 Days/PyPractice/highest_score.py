# welcome to the highest score in the list program
student_scores = input("Enter scores of students: ").split()
print(student_scores)
highest_score = 0
for score in range(0, len(student_scores)):

    student_scores[score] = int(student_scores[score])

    if highest_score < student_scores[score]:
        highest_score = student_scores[score]
print("Highest score in the class is:", highest_score)
