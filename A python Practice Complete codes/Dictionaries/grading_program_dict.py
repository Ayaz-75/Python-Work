
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

# student_grades["Harry"] = student_scores["Harry"]
# student_grades["Ron"] = student_scores["Ron"]
# student_grades["Hermione"] = student_scores["Hermione"]
# student_grades["Draco"] = student_scores["Draco"]
# student_grades["Neville"] = student_scores["Neville"]    


for grade in student_scores:
    # student_score = student_grades[grade]
    score = student_scores[grade]
    if score > 91 and score <= 100:
        student_grades[grade] = "Outstanding"
    
    elif score > 81 and score <= 91:
        student_grades[grade] = "Exceeds expectations"

    elif score > 71 and score <= 81:
        student_grades[grade] = "Acceptable"

    else:
        student_grades[grade] = "Fail"



# 🚨 Don't change the code below 👇
print(student_grades)
