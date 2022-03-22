from food import Food
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreBoard import Board

myScreen = Screen()
myScreen.setup(width=800,height=800)
myScreen.bgcolor("black")
myScreen.title("TheSnakeGame")
myScreen.tracer(0)

mySnake = Snake()
myFood = Food()
myBoard = Board()

myScreen.listen()
myScreen.onkeypress(mySnake.up, "Up")
myScreen.onkeypress(mySnake.down, "Down")
myScreen.onkeypress(mySnake.right, "Right")
myScreen.onkeypress(mySnake.left, "Left")


while True:
    time.sleep(0.1)
    myScreen.update()
    mySnake.forward()

    #detect eating
    if mySnake.tails[0].distance(myFood) < 15:
        myFood.refresh()
        myBoard.onCollision()
        pos = (mySnake.tails[-1].xcor(), mySnake.tails[-1].ycor())
        mySnake.add(pos)
        print("ham aq")
    
    #detect collisions
    if mySnake.tails[0].xcor() < -390 or mySnake.tails[0].xcor() > 390 or mySnake.tails[0].ycor() < -390 or mySnake.tails[0].ycor() > 390:
        myBoard.gameOver()
        mySnake.reset()


    #detect tail collisions
    for tail in mySnake.tails[1::]:
        if mySnake.tails[0].distance(tail) < 15:
            isON = False
            myBoard.gameOver()
            mySnake.reset()




myScreen.exitonclick()