
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)
        print()


    def check_answer(self, u_answer, original_answer):
        if u_answer == original_answer.lower():
            self.score += 1
            print(f"You got it! \ncurrent score is: {self.question_number}/{self.score}")
        else:
            print(f"That's wrong!")
            print(f"current score is: {self.question_number}/{self.score}")

        print(f"The correct answer was: {original_answer}")

