from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.my_score = 0
        self.cpu_score = 0
        self.goto(0, 250)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write(arg= f"{self.my_score} | {self.cpu_score}", align= "center", font=("Arial", 24, "normal"))

    def increasemyscore(self):
        self.my_score += 1

    def increaseplayerscore(self):
        self.cpu_score += 1
