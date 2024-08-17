from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(x_coordinate, y_coordinate)

    def move_up(self):
        y_axis = self.ycor() + 20
        self.goto(self.xcor(), y_axis)

    def move_down(self):
        y_axis = self.ycor() - 20
        self.goto(self.xcor(), y_axis)
