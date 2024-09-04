from turtle import Turtle

class Snake:
    def __init__(self):
        x_postion = 0
        self.segments =[]
        for i in range (0,3):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)
            new_turtle.goto(x_postion,0)
            x_postion -= 20
            self.segments.append(new_turtle)

    def extend(self):
        x_postion = 0
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)
        new_turtle.goto(x_postion, 0)
        x_postion -= 20
        self.segments.append(new_turtle)


    def move(self):
        for turtl in range (len(self.segments)-1, 0, -1):
            new_x = self.segments[turtl - 1].xcor()
            new_y = self.segments[turtl - 1].ycor()
            self.segments[turtl].goto(new_x, new_y)
        self.segments[0].forward(10)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
