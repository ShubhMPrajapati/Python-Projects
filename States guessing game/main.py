from turtle import Turtle, Screen
from set_state import Set_State
import turtle as td
import pandas as pd

turtle = Turtle()
screen = Screen()
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

df = pd.read_csv("50_states.csv")

states = df.state.to_list()
xcor = df.x.to_list()
ycor = df.y.to_list()

total_state = len(states)
guessed_state = 0
turns = 50
guessed_state_name = []


game_is_on = True
while game_is_on:
    answer_state = screen.textinput(f"Correct {guessed_state}/{total_state} | Turns: {turns}",
                                    "What is another State's name? ").title()
    if answer_state in states:
        guessed_state_name.append(answer_state)
        ind = states.index(answer_state)
        guessed_state += 1
        print(xcor[ind])
        print(ycor[ind])
        write = Set_State()
        write.set_text(answer_state, xcor[ind], ycor[ind])

    elif answer_state in ["Exit", "Close"]:
        missing_states_name = []
        for stat in states:
            if stat in guessed_state_name:
                pass
            else:
                missing_states_name.append(stat)
                dfs = pd.DataFrame(missing_states_name)
                dfs.to_csv("Remaining_States_to_Learn.csv")
                write = Set_State()
                write.set_text("GAME OVER", 0, 0)
                game_is_on = False
    else:
        turns -= 1
        if turns == 0:
            write = Set_State()
            write.set_text("GAME OVER", 0, 0)
            game_is_on = False

td.mainloop()