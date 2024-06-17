from turtle import Turtle, Screen


def draw_square(t):
    for _ in range(4):
        t.forward(100)
        t.right(90)

turtle = Turtle()
screen = Screen()
draw_square(turtle)
screen.exitonclick()
