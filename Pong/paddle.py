from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_to(self, tup):
        self.goto(tup)

    def move_up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)
