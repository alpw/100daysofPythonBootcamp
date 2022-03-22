from turtle import Turtle
from time import sleep

font = ("Verdana","18","bold")


class Board(Turtle):
    def __init__(self):
        super().__init__()
        with open("HighScore.txt") as file:
            self.highscore = int(file.readline())
        print(self.highscore)
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,370)
        self.hideturtle()
        self.write(f"Score: {self.score}  High Score: {self.highscore}",False,"center",font)
    
    def onCollision(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}",False,"center",font)

    def gameOver(self):
        self.clear()
        self.goto(0,0)
        self.write(f" . . . : : : GAME OVER : : : . . . \n\n Your Score: {self.score}\nHigh Score: {self.highscore}",False,"center",("Arial", 24, "bold"))
        self.reset()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("HighScore.txt","w") as data:
                data.write(str(self.highscore))
        self.score = 0
        sleep(3)
        self.clear()
        self.goto(0,370)
        self.write(f"Score: {self.score}  High Score: {self.highscore}",False,"center",font)
