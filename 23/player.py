from car_manager import STARTING_MOVE_DISTANCE
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def goUp(self):
        self.forward(10)

    def startAgain(self):
        self.goto(STARTING_POSITION)
    
    def atTheFinish(self):
        if self.ycor() > 275:
            return True
        else:
            return False