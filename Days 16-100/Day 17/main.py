from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data_piece in question_data:
    question_bank.append(Question(data_piece["question"], data_piece["correct_answer"]))

qb = QuizBrain(question_bank)
while qb.still_has_questions():
    qb.next_question()

print("Congrats! you have finished the quiz!")
print(f"your final score was: {qb.score}/{qb.quest_num}")

