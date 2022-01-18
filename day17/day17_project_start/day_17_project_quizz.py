from data import question_data_trivia_db
from question_model import Question
from quiz_brain import QuizBrain
from replit import clear

question_bank = []
for question in question_data_trivia_db:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
clear()

while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
