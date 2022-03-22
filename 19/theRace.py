from turtle import Turtle, Screen
import random

colors = ["red", "orange","yellow","green","blue","purple"]


myScreen = Screen()
bet = myScreen.textinput("color?","gir")
turtles = []

for i in  range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.speed= "Fastest"
    tim.penup()
    tim.color(colors[i])
    tim.goto(-400,-250+i*80)
    turtles.append(tim)

def winner():
    for i in turtles:
        if i.xcor() > 400:
            return i.color()[0]

while not any(x.xcor() > 400 for x in turtles):
    for tr in turtles:
        tr.forward(random.randint(5,25))

print(winner())


if winner() == bet:
    print("alasıopdfjas KABLUMBAA YARIŞINI KAZNAFIN")
else:
    print("YARRRAK")




myScreen.exitonclick()