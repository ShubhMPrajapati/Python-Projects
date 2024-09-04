import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("purple")
scr.title(f'Snake Game')

scr.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

scr.listen()
scr.onkey(key="Up", fun=snake.up)
scr.onkey(key="Down", fun=snake.down)
scr.onkey(key="Left", fun=snake.left)
scr.onkey(key="Right", fun=snake.right)


game_is_on = True


while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()

    if snake.segments[0].xcor()>290 or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()>290 or snake.segments[0].ycor()<-290:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[2:]:
        if snake.segments[0].distance(segment) <10:
            game_is_on = False
            score.game_over()

    # if snake.segments[0]























scr.exitonclick()