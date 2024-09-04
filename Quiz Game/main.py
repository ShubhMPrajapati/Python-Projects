from data import question_data
from question_model import Question
from quiz_brain import quiz_brain

score = 0

question_bank = []
for question in question_data:
    question_text = question["text"]
    answer_text = question["answer"]
    new_question = Question(question_text,answer_text)
    question_bank.append(new_question)


quiz = quiz_brain(question_bank)

answer = quiz.next_question()







