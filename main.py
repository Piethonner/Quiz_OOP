from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

all_questions = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer) # positional parameters
    all_questions.append(new_question)

quiz = QuizBrain(all_questions)

while quiz.questions_left():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your final score was: {quiz.score}/{len(all_questions)}")
