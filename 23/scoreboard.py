from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-250,275)
        self.write(f"Score: {self.score}",False,"center",FONT)
    
    def addScore(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}",False,"center",FONT)

    def gameOver(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER\nScore = {self.score}", False, "center", ("Courier", 24, "normal"))
