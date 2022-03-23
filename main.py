from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

EDGE = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_on = True
while is_on:
    screen.update()
    time.sleep(0.08)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > EDGE or snake.head.xcor() < -EDGE or snake.head.ycor() > EDGE or snake.head.ycor() < -EDGE:
        is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_on = False
            scoreboard.game_over()


screen.exitonclick()
