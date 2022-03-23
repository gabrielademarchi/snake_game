from turtle import Turtle
import random

EDGE = 280


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 10x10 circle
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-EDGE, EDGE)
        random_y = random.randint(-EDGE, EDGE)
        self.goto(random_x, random_y)
