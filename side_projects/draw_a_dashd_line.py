from turtle import Turtle, Screen


def draw_a_dashed_line(t):
    for _ in range(15):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()

turtle = Turtle()
screen = Screen()

draw_a_dashed_line(turtle)
screen.exitonclick()
