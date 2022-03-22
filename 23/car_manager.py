from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def createCar(self):
        if random.randint(1,100) < 20:
            newCar = Turtle(shape="square")
            newCar.shapesize(1,2)
            newCar.penup()
            newCar.color(random.choice(COLORS))
            newCar.goto(300,random.randint(-250,250))
            newCar.setheading(180)
            self.allCars.append(newCar)
    
    def moveThatAll(self):
        for index in range(len(self.allCars)-1):
            self.allCars[index].forward(self.carSpeed)
    
    def levelUp(self):
        self.carSpeed += MOVE_INCREMENT