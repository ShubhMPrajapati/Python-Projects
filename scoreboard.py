from turtle import Turtle


FONT = ("Courier", 25 ,"normal" )
ALINGMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.write(arg=f"Score: {self.score}",move=False, align=ALINGMENT, font=FONT)
        self.color("white")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER! Final Score is:{self.score}",move=False, align=ALINGMENT, font=FONT)


    def increase(self):
        self.score +=1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALINGMENT, font=FONT)

