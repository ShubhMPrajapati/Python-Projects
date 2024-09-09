from turtle import Turtle, Screen


class Set_State(Turtle):

    def __init__(self ):
        super().__init__()
        self.penup()
        self.hideturtle()

    def set_text(self, state, x, y):
        self.goto(x, y)
        if state == "GAME OVER":
            self.pensize(1000)
        self.write(state,True, align="center")




