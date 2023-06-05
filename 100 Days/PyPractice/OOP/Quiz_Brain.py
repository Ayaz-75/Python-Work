class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.q_list = question_list
        self.score = 0


    def still_has_questions(self):
        return self.question_number < len(self.q_list)

    #   if self.question_number == len(self.q_list): this is same as above expression is
    #           return True
    #       else:
    #           return False

    def check_answer(self, user_answer, correct_answer):
        self.user_answer = user_answer
        self.correct_answer = correct_answer

        if user_answer == correct_answer:
            print("you answer is correct")
            self.score += 1
            # print(f"your score is {self.score}")
        else:
            print("Wrong answer")
        print(f"right answer is {correct_answer}")
        print(f"your score is {self.score}/{self.question_number}")
        print("\n")

    def next_question(self, ):
        correct_answer = current_question = self.q_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text}(True/False): ")
        self.check_answer(user_answer, current_question.answer)
