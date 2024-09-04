import random
from turtle import Turtle, Screen

# timmy = Turtle()
# scr = Screen()
#
#
# def move_forward():
#     timmy.forward(10)
#
# def move_right():
#     timmy.right(8)
#
# def move_backwords():
#     timmy.back(10)
#
# def move_left():
#     timmy.left(8)
#
# def clr_scr():
#     timmy.clear()
#
# scr.listen()
# scr.onkey(key="w", fun=move_forward)
# scr.onkey(key="d", fun=move_right)
# scr.onkey(key="s", fun=move_backwords)
# scr.onkey(key="a", fun=move_left)
# scr.onkey(key="c",fun=clr_scr)
#
# scr.exitonclick()




is_race_on = False
scr = Screen()
scr.setup(width=600,height=500)
user_input = scr.textinput("Make your bet", "Which turtle is gonna win? ")
print(user_input)
color = ["red","blue","yellow","green"]
y_coordinates =[-60, -20, 20, 60]
all_turtles = []
for i in range(0,4):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_coordinates[i])
    new_turtle.color(color[i])
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:

    for turtles in all_turtles:
        if turtles.xcor() >235:
            print(turtles.pencolor(), "Turtle Won")
            is_race_on = False

        turtles = random.choice(all_turtles)
        turtles.forward(random.randint(0, 10))











    
scr.exitonclick()