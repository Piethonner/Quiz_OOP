class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.all_questions = q_list
        self.score = 0

    def questions_left(self):
        """Returns True if there are any questions left, False if quiz is out of questions."""
        return self.q_number < len(self.all_questions)

    def next_question(self):
        """Counts question number, gathers input T/F."""
        current_question = self.all_questions[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks if answer is correct."""
        if user_answer.lower() == correct_answer.lower():
            print("Correct answer!")
            self.score += 1
        else:
            print("Incorrect!")
        print(f"The correct answer was: {correct_answer}.\nYour current score is {self.score}/{self.q_number}\n")
