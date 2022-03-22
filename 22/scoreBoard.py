from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.goto(0,340)
        self.scoreCounterL = 0
        self.scoreCounterR = 0
        self.write(str(self.scoreCounterL) +" - "+ str(self.scoreCounterR),False, "center", ("Verdana", 46,"bold"))
    
    def scoreL(self):
        self.scoreCounterL += 1
        self.clear()
        self.write(str(self.scoreCounterL) +" - "+ str(self.scoreCounterR),False, "center", ("Verdana", 46,"bold"))
    
    def scoreR(self):
        self.scoreCounterR += 1
        self.clear()
        self.write(str(self.scoreCounterL) +" - "+ str(self.scoreCounterR),False, "center", ("Verdana", 46,"bold"))
