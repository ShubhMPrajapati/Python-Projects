# from turtle import Turtle, Screen
#
# jim = Turtle()
# scr = Screen()
#
# jim.shape("turtle")
# jim.color("orange")
# jim.forward(100)
# jim.sety(100)
# jim.back(100)
# jim.down()
#
# scr.exitonclick()

from prettytable import PrettyTable


table = PrettyTable()
table.align = "c"

table.add_column("Pokemon Name",["Pikachu", "Squirrel", "Charmender"])
table.add_column("Type",["Electric", "Water", "Fire"])

print(table)