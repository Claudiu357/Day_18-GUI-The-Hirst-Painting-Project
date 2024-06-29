from turtle import Turtle, Screen
import random


def random_walk(t):
    t.pensize(10)
    moving = True
    angles = [0, 90, 180, -90, -180]
    colors = ["red", "yellow", "pink", "green", "purple", "orange", "blue"]
    while moving:
        t.pencolor(random.choice(colors))
        t.forward(50)
        t.left(random.choice(angles))


turtle = Turtle()
screen = Screen()
random_walk(turtle)
screen.exitonclick()
