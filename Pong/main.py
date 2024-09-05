import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scorbaord import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

right_paddle = Paddle()
right_paddle.go_to((350, 0))

left_paddle = Paddle()
left_paddle.go_to((-350, 0))

screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)

screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)
screen.update()

ball = Ball()
ball.setheading(45)

left_scoreboard = Scoreboard(-200, 240)
right_scoreboard = Scoreboard(200, 240)


screens = Turtle()
screens.pencolor("white")
screens.penup()
screens.goto(0, -300)
screens.pendown()
screens.setheading(90)
screens.goto(0, 320)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    left_scoreboard.show()
    right_scoreboard.show()
    screens.goto(0, 350)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 335 or ball.distance(left_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()

    elif ball.xcor() > 370 or ball.xcor() < -370:

        if ball.xcor() > 370:
            left_scoreboard.increase()
        elif ball.xcor() < -370:
            right_scoreboard.increase()
        ball.rst()

screen.exitonclick()
