from turtle import Turtle, Screen
import random


def draw_a_spirograph(t):
    t.speed("fastest")
    colors = ["red", "yellow", "pink", "green", "purple", "orange", "blue"]
    heading = t.heading()
    for _ in range(37):
        t.circle(100)
        t.color(random.choice(colors))
        t.setheading(heading)
        heading += 10

turtle = Turtle()
screen = Screen()
draw_a_spirograph(turtle)
screen.exitonclick()

