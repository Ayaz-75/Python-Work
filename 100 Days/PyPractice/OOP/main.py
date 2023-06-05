
from Question_model import Question
from data import question_data
from Quiz_Brain import QuizBrain
question_bank = []
for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("you have completed the quiz")
print(f"your total score is: {quiz.score}/{len(question_bank)}")
