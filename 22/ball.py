from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.left(37)
        self.yDirection = 1
        self.xDirection = 1

    def move(self, speed):
        self.goto(self.xcor()+speed*self.xDirection, self.ycor()+self.yDirection*speed)
    
    def bounceY(self):
        self.yDirection *= -1
    def bounceX(self):
        self.xDirection *= -1

    def resetPos(self):
        self.goto(0,0)
        angle = randint(15,165)
        self.right(angle)
        print(angle)

