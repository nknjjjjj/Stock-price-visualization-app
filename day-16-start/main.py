# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan2")
# timmy.forward(1000)
# timmy.backward(1000)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Su"])
table.add_column("Type", ["Elet", "water"])

table.align = "l"

print(table)
