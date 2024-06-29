import colorgram
import turtle as turtle_module


def return_rgb():
    colors = colorgram.extract("ppaint.jpg", 100)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb = (r, g, b)
        rgb_colors.append(rgb)
    return rgb_colors


turtle_module.colormode(255)
turtle = turtle_module.Turtle()
turtle.penup()
screen = turtle_module.Screen()
colors = return_rgb()
x = -350
y = -150
turtle.goto(x, y)
dot = 0
for color in colors:
    if dot > 6:
        dot = 0
        y = y + 50
        turtle.goto(x, y)
    turtle.dot(30, color)
    turtle.forward(50)
    dot += 1
turtle.hideturtle()
screen.exitonclick()