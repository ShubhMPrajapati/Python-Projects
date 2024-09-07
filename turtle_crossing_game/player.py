from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def moved(self):
        self.forward(MOVE_DISTANCE)

    def raced_finished(self):
        if self.ycor()>=280:
            print("Race Finished")
            return True

    def reset(self):
        self.goto(STARTING_POSITION)





