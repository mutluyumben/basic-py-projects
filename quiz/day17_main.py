from day17_question_model import Question
from day17_quiz_data import question_data
from day17_quiz_brain import quizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = quizBrain(question_bank)

while quiz.still_cont():
    quiz.question_queue()


print("You've completed the quiz")
print(f"Your final score was : {quiz.score} / {quiz.question_number} ")

