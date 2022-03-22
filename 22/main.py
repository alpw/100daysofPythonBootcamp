from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreBoard import Score

myScreen = Screen()

myScreen.bgcolor("black")
myScreen.setup(1500, 900, 0,0)
myScreen.title("PONG")
myScreen.tracer(0)

R_paddle = Paddle((700,0))
L_paddle = Paddle((-700,0))

myScreen.listen()
myBall = Ball()
myScore = Score()

ballSpeed = 6
maxY = 430
maxX = 690
lenBounce = 120
ballSpeedIncrease = 1
defBallSpeed = ballSpeed

def missR():
    global ballSpeed
    ballSpeed =defBallSpeed
    print("R missed")
    myBall.bounceX()
    myBall.resetPos()
    myScore.scoreL()

def missL():
    global ballSpeed
    ballSpeed =defBallSpeed
    print("L missed")
    myBall.bounceX()
    myBall.bounceY()
    myBall.resetPos()
    myScore.scoreR()


while True:
    myScreen.update()
    sleep(0.0001)
    myBall.move(ballSpeed)

    if myBall.ycor() > maxY or myBall.ycor() < -maxY: #top-bottom bpunce
        myBall.bounceY()

    if myBall.xcor() > maxX or myBall.xcor() < -maxX :
        if R_paddle.distance(myBall) <= lenBounce/2: #playerR paddle bounce
            myBall.bounceX()
            myBall.move(ballSpeed)
            ballSpeed += ballSpeedIncrease
        elif  myBall.xcor() > 0:
            missR()

        if L_paddle.distance(myBall) <= lenBounce/2: #playerL paddle bounce
            myBall.bounceX()
            myBall.move(ballSpeed)
            ballSpeed += ballSpeedIncrease
        elif myBall.xcor() < 0:
            missL()
    

    myScreen.onkeypress(R_paddle.up, "Up")
    myScreen.onkeypress(R_paddle.down, "Down")
    myScreen.onkeypress(L_paddle.up, "w")
    myScreen.onkeypress(L_paddle.down, "s")



myScreen.exitonclick()