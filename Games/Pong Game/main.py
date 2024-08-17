from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import time


# TODO: Create the screen(Window)
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

score = Scoreboard()
player1 = Paddle(-350, 0)
player2 = Paddle(350, 0)
dot = Ball()

screen.listen()

screen.onkey(player1.move_up, "Up")
screen.onkey(player1.move_down, "Down")
screen.onkey(player2.move_up, "w")
screen.onkey(player2.move_down, "s")
game_over = False
while not game_over:
    time.sleep(0.1)
    dot.move()
    screen.update()

# TODO Create and move a paddle

# TODO Create another paddle

# TODO Create the ball and make it move

# TODO Detect collision with wall and bounce

# TODO Detect collision with paddle

# TODO Detect when paddle misses

# TODO Keep score
