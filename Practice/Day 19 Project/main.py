from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "blue", "green", "purple"]
y_axis = -100
is_race_on = False
turtles = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, y_axis)
    turtles.append(new_turtle)
    y_axis += 40


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        distance = randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
