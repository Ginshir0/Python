from turtle import Turtle, Screen, colormode
import random

color_list = [(199, 117, 175), (124, 24, 36), (210, 213, 221), (168, 57, 106), (222, 227, 224), (186, 53, 158), (6, 83, 57), (109, 85, 67), (113, 175, 161), (22, 174, 122), (64, 138, 153), (39, 36, 36), (76, 48, 40), (9, 47, 67), (90, 53, 141), (181, 79, 96), (132, 42, 40), (210, 151, 200), (141, 155, 171), (179, 186, 201), (172, 159, 153), (212, 177, 183), (176, 203, 198)]

painter = Turtle()
screen = Screen()
colormode(255)
x_axis = -200
y_axis = -200

for row in range(10):
    for dot in range(10):
        painter.teleport(x_axis + (50 * dot), y_axis)
        painter.dot(20, random.choice(color_list))
    y_axis += 50

screen.exitonclick()
