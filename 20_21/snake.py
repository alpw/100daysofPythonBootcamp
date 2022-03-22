from turtle import Turtle


startingPosition = [(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.tails = []
        self.createSnake()
    
    def add(self, pos):
        newTr = Turtle("square")
        newTr.color("white")
        newTr.penup()
        newTr.goto(pos)
        self.tails.append(newTr)
    
    def createSnake(self):
        for pos in startingPosition:
            self.add(pos)

    def forward(self):
        for index in range((len(self.tails)-1),0,-1):
            self.tails[index].goto(self.tails[index-1].xcor(),self.tails[index-1].ycor())
        self.tails[0].forward(20)
    
    def up(self):
        if self.tails[0].heading() != 270:
            self.tails[0].setheading(90)

    def down(self):
        if self.tails[0].heading() != 90:
            self.tails[0].setheading(270)

    def left(self):
        if self.tails[0].heading() != 0:
            self.tails[0].setheading(180)
        
    def right(self):
        if self.tails[0].heading() != 180:
            self.tails[0].setheading(0)
    
    def reset(self):
        for i in range(len(self.tails)):
            self.tails[i].goto(1000,0)
        self.tails = []
        self.createSnake()
