from turtle import Turtle
from random import randint


class Food:
    def __init__(self):
        self.tim = Turtle()
        self.tim.penup()
        self.tim.color("blue")
        self.tim.shape("circle")
        self.tim.goto(randint(-28, 28) * 10, randint(-28, 28) * 10)
        self.tim.shapesize(stretch_len=.5, stretch_wid=.5)

    def kill(self):
        self.tim.goto(randint(-30, 30) * 10, randint(-30, 30) * 10)

    def get_pos(self):
        return self.tim.xcor(), self.tim.ycor()
