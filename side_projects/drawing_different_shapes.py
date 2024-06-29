from turtle import Turtle, Screen
import random


def draw_shapes(t):
    colors = ["red", "yellow", "pink", "green", "purple", "orange", "blue"]
    for _ in range(3, 10):
        angle = 360 / _
        t.pencolor(random.choice(colors))
        for i in range(_):
            t.forward(100)
            t.right(angle)

turtle = Turtle()
screen = Screen()
draw_shapes(turtle)
screen.exitonclick()
