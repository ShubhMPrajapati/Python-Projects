from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox

THEME_COLOR = "#375362"
FONT =("Arial", 20, "italic")

class QuizInterFace:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(height=500, width=600, bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.text = self.canvas.create_text(150, 125, font=FONT, text="Questions Here", width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        wrong_image = PhotoImage(file="images/false.png")
        right_image = PhotoImage(file="images/true.png")

        self.button1 = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed)
        self.button1.grid(row=2, column=1, padx=5, pady=5)

        self.button2 = Button(image=right_image, highlightthickness=0, command=self.true_pressed)
        self.button2.grid(row=2, column=0, padx=5, pady=5)

        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR,pady=5)
        self.label.grid(row=0, column=1,)
        self.new_question()
        self.window.mainloop()

    def new_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=next_question)
            self.canvas.config(bg="white")  # Reset the background color after each question
        else:
            self.canvas.itemconfig(self.text, text="Quiz is Over")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def true_pressed(self):
        self.check(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.check(self.quiz.check_answer('False'))

    def increase_score(self):
        var = self.quiz.score
        self.label.config(text=f"Score: {var}", fg="white", bg=THEME_COLOR)

    def check(self, is_feedback):
        if is_feedback:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.increase_score()  # Update score after checking
        self.window.after(1000, self.new_question)  # Corrected to delay the next question without calling immediately
