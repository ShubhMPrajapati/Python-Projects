from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")


# colors = ["purple", "black", "red", "blue", "yellow", "orange","violet", "green"]

# for i in range(3,9):
#     a = 360/i
#     b = random.choice(colors)
#     timmy.color(b)
#     print(b)
#     for j in range(0,i):
#         timmy.forward(100)
#         timmy.right(a)




# directions = [90,180,270,360]
# i = 0
# timmy.pensize(15)
# timmy.speed("fastest")
#
#
# def randon_color():
#     import random
#     r = random.randint(0, 255) / 255
#     g = random.randint(0, 255) / 255
#     b = random.randint(0, 255) / 255
#     return (r, g, b)
#
# while i != 300:
#     timmy.color(randon_color())
#     timmy.forward(20)
#
#     timmy.setheading(random.choice(directions))
#     # timmy.setheading(random.randint(0,360))
#
#     i+=1




# def randon_color():
#     import random
#     r = random.randint(0, 255) / 255
#     g = random.randint(0, 255) / 255
#     b = random.randint(0, 255) / 255
#     return (r, g, b)
#
# timmy.speed("fastest")
#
# for i in range(0,360,5):
#     print(i)
#     timmy.color(randon_color())
#     timmy.circle(100)
#     i+=1
#     timmy.setheading(i)



import colorgram
import turtle as turtle_module
turtle_module.colormode(255)
colors = colorgram.extract('20_001.jpg', 25)
all_color = []
timmy.speed("fastest")
timmy.hideturtle()

for color in colors:
    col1 = color.rgb.r
    col2 = color.rgb.g
    col3 = color.rgb.b
    rgb = (col1,col2,col3)
    all_color.append(rgb)


timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

def move_timmy():
    for i in range(0,10):
        timmy.dot(20, random.choice(all_color))
        timmy.forward(50)

for i in range(1,11):
    move_timmy()

    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)


screen = Screen()
screen.exitonclick()








import time
from turtle import Turtle, Screen
import snake

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("purple")
scr.title('Snake Game')
x_postion = 0
segments =[]
scr.tracer(0)


for i in range (0,3):
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x_postion,0)
    x_postion -= 20
    segments.append(new_turtle)

game_is_on = True

while game_is_on:
    scr.update()
    time.sleep(0.1)

    for turtl in range (len(segments)-1, 0, -1):
        new_x = segments[turtl - 1].xcor()
        new_y = segments[turtl - 1].ycor()
        segments[turtl].goto(new_x,new_y)
    segments[0].forward(12)


scr.exitonclick()










