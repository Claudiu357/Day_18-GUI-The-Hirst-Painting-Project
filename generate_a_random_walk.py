from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()
angles = [0, 90, 180, -90, -180]
colors = ["red", "yellow", "pink", "green", "purple", "orange", "blue"]
moving = True

turtle.pensize(10)

while moving:
    turtle.pencolor(random.choice(colors))
    turtle.forward(50)
    turtle.left(random.choice(angles))
screen.exitonclick()