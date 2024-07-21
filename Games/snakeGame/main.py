import snake
from turtle import Turtle, Screen
import time
import scoreboard
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

score = scoreboard.Score()
p1 = snake.Snake()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=p1.up)
screen.onkey(key="Down", fun=p1.down)
screen.onkey(key="Left", fun=p1.left)
screen.onkey(key="Right", fun=p1.right)

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    p1.move()

    # Detect collision with food
    if p1.body[0].distance(food) < 15:
        score.update()
        food.refresh()

    # Detect collision with wall
    if p1.body[0].xcor() > 280 or p1.body[0].xcor() < - 280 or p1.body[0].ycor() > 280 or p1.body[0].ycor() < - 280:
        score.game_over()
        game_over = True
screen.exitonclick()
