import turtle
from turtle import Turtle

positions = [(-20, 0), (0, 0), (20, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.direction = "right"

        for position in positions:
            segment = Turtle()
            segment.penup()
            segment.color("white")
            segment.shape("square")
            segment.goto(position)
            self.segments.append(segment)

        self.head = self.segments[2]

    # controls of our snake
    def up(self):
        if self.direction == "right":
            self.head.left(90)
            self.direction = "up"
        elif self.direction == "left":
            self.head.right(90)
            self.direction = "up"

    def down(self):
        if self.direction == "right":
            self.head.right(90)
            self.direction = "down"
        elif self.direction == "left":
            self.head.left(90)
            self.direction = "down"

    def left(self):
        if self.direction == "up":
            self.head.left(90)
            self.direction = "left"
        elif self.direction == "down":
            self.head.right(90)
            self.direction = "left"

    def right(self):
        if self.direction == "up":
            self.head.right(90)
            self.direction = "right"
        elif self.direction == "down":
            self.head.left(90)
            self.direction = "right"

    def move(self):
        for i in range(len(self.segments)):
            if i == len(self.segments) - 1:
                self.segments[i].forward(10)
                self.head.goto(round(self.head.xcor()), round(self.head.ycor()))
            else:
                self.segments[i].goto(self.segments[i + 1].xcor(), self.segments[i + 1].ycor())

    def stretch(self):
        segment = Turtle()
        segment.penup()
        segment.color("white")
        segment.shape("square")
        segment.goto(self.segments[0].xcor(), self.segments[0].xcor())
        self.segments.insert(0, segment)

    def get_pos(self):
        return self.head.xcor(), self.head.ycor()
