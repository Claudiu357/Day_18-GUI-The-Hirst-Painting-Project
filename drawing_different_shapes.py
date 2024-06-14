from turtle import Turtle, Screen
import random

colors = ["red", "yellow", "pink", "green", "purple", "orange", "blue"]
turtle = Turtle()
screen = Screen()
for _ in range(3, 10):
    angle = 360 / _
    turtle.pencolor(random.choice(colors))
    for i in range(_):
        turtle.forward(100)
        turtle.right(angle)
screen.exitonclick()