from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(arg=f"Score: {self.points}", align="center", font=("Arial", 16, "normal"))

    def update(self):
        self.points += 1
        self.clear()
        self.write(arg=f"Score: {self.points}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 24, "normal"))
