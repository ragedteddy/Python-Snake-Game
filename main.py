import time, turtle
from snake import Snake
from food import Food
from turtle import Turtle, Screen
from scoreboard import Scorecount

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Scorecount()
score.update()

turtle.onkey(snake.up, "Up")
turtle.onkey(snake.down, "Down")
turtle.onkey(snake.left, "Left")
turtle.onkey(snake.right, "Right")


def dist(first, second):
    return ((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2) ** .5

def check():
    for i in range(len(snake.segments)-1):
        if dist(snake.get_pos(), (snake.segments[i].xcor(), snake.segments[i].ycor())) < 10:
            return True
    return False


while True:
    screen.update()
    time.sleep(.1)

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 or check():
        print("Game Over")
        break

    if dist(snake.get_pos(), food.get_pos()) < 15:
        score.update()
        food.kill()
        snake.stretch()

    snake.move()

screen.exitonclick()
