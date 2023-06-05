scores = [61, 82, 35, 74, 58 ]

highest_score = scores[0]
for score in scores:
    if highest_score < score:
        highest_score = score

print(f"{highest_score} is the highest score in the class")
