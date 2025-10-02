# import turtle
# jimmy = turtle.Turtle()
# lesson 1
# from turtle import Turtle, Screen
#
# jimmy = Turtle()
# print(jimmy)
# jimmy.shape("turtle")
# jimmy.color("teal")
# jimmy.forward(100)
# jimmy.right(200)
# jimmy.forward(300)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# lesson 2
from prettytable import PrettyTable

table = PrettyTable()
table.field_names=["Pokemon name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "l"
print(table)
