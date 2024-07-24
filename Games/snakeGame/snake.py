from turtle import Turtle

LOCATIONS = [(-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.body = []

        for location in LOCATIONS:
            self.add_body(location)

    def move(self):
        for item in range(len(self.body) - 1, 0, -1):
            new_x = self.body[item - 1].xcor()
            new_y = self.body[item - 1].ycor()
            self.body[item].goto(new_x, new_y)
        self.body[0].forward(MOVE_DISTANCE)

    def add_body(self, position):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.body.append(new_snake)


    def extend(self):
        self.add_body(self.body[-1].position())

    def up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)
