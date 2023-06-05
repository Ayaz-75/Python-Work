
student_scores = [76, 55, 65, 83, 71, 80]


high_score = student_scores[0]
lowest_score = high_score

for score in student_scores:
    if score > high_score:
        high_score = score
    elif score < lowest_score:
        lowest_score = score


print(f'highest score is: {high_score}\nLowest score is: {lowest_score}')
