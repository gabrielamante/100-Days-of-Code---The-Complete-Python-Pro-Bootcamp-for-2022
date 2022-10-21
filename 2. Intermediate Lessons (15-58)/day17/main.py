from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

q_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_q = Question(q_text, q_answer)
    q_bank.append(new_q)

quiz = QuizBrain(q_bank)
while quiz._still_has_questions(q_bank):
    quiz._next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")