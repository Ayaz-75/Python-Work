from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']

    # new_q = Question(question['text'], question['answer']) # this works the same!

    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()


