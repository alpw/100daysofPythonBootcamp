from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.shapesize(1,5)
        self.right(90)
        self.goto(pos)
    
    def up(self):
        if self.ycor() < 370:
            self.goto(self.xcor(), self.ycor() +40)
    def down(self):
        if self.ycor() > -370:
            self.goto(self.xcor(), self.ycor() -40)