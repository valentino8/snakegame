from turtle import Screen
from turtle import Turtle
from snake import Snake
from food import Food
from score import Score

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_on = True
while game_on:
    screen.update()

    snake.move()
    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.scorecount()
        snake.extend()


    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.gameOver()

    for segment in snake.segments[1::]:

        if snake.head.distance(segment) < 10:
            score.gameOver()
            game_on = False
            



screen.exitonclick()
