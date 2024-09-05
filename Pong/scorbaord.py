from turtle import Turtle

FONT = ("Courier", 25 ,"normal" )
ALINGMENT = "center"

class Scoreboard(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(arg=f"Score: {self.score}",move=False, align=ALINGMENT, font=FONT)
        self.color("white")

    def increase(self):
        self.score +=1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALINGMENT, font=FONT)

    def show(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALINGMENT, font=FONT)
        pass




