from question_model import Question
from data import question_data
from quiz_brain import *
Go = True
question_bank = []
#PASAMOS LAS PREGUNTAS Y RESPUESTA AL ARREGLO
for questions in question_data:
    txt = questions["text"]
    ans = questions["answer"]
    new_question = Question(txt, ans)
    question_bank.append(new_question)

Quiz = QuizBrain(question_bank)
while Quiz.still_has_questions():
    Quiz.next_question()

print("")
print("You have completed the quiz!!!")
print(f"Your final score is: {Quiz.a_correct}/{Quiz.question_number}")
