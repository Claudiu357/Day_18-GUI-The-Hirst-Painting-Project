from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

for _ in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
screen.exitonclick()
