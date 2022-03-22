from turtle import Turtle, Screen

tim = Turtle()
myScreen = Screen()

def git():
    tim.forward(10)


myScreen.listen()
myScreen.onkey(git,"space")
myScreen.textinput(prompt="askdşjfklsdf",title="gel vatandaş gel")

myScreen.exitonclick()