import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

me = Player()

screen.listen()
screen.onkeypress(me.goUp,"Up")

carManager = CarManager()

myBoard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.createCar()
    carManager.moveThatAll()

    #detect collision
    for car in carManager.allCars:
        if car.distance(me) < 20:
            game_is_on = False
    
    if me.atTheFinish():
        me.startAgain()
        carManager.levelUp()
        myBoard.addScore()

myBoard.gameOver()
screen.exitonclick()