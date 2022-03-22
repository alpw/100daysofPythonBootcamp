from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("orange")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        self.goto(randint(-19, 19)*20, randint(-19, 19)*20)

