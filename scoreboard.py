from turtle import Turtle


class Scorecount:
    def __init__(self):
        self.count = -1
        self.tim = Turtle()
        self.tim.penup()
        self.tim.color("white")
        self.tim.goto(-60, 260)
        self.tim.hideturtle()

    def update(self):
        self.tim.clear()
        self.count += 1
        self.tim.write(f"Score : {self.count}", font=("Verdana",
                                                      20, "normal"))
