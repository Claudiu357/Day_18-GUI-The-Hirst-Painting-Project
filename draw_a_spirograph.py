from turtle import Turtle, Screen
import random

trutle = Turtle()
trutle.speed("fastest")
screen = Screen()
colors = ["red", "yellow", "pink", "green", "purple", "orange", "blue"]
heading = trutle.heading()
for _ in range(37):
    trutle.circle(100)
    trutle.color(random.choice(colors))
    trutle.setheading(heading)
    heading += 10
screen.exitonclick()
