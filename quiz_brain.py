class quiz_brain:
    def __init__(self, list):
        self.question_number = 0
        self.questions_list = list

    def still_has_questions(self):
        i

    def next_question(self):
        score = 0
        is_on = True
        while is_on:
            current_question_number = self.questions_list[self.question_number]
            self.question_number += 1
            answer = input(f"Q.{self.question_number}: {current_question_number.text} ")
            if answer == current_question_number.answer:
                score +=1
                print(score)
            else:
                score -=1
                print(score)


