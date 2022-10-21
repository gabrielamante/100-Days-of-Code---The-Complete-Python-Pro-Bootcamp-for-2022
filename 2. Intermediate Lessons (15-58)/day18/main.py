# -- Instalar colorgram: pip install colorgram.py

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color = (r,g,b)
#     rgb_colors.append(color)

import random
import turtle
from turtle import Turtle, Screen, colormode, pendown

turtle.colormode(255)
tw = turtle.Turtle()
tw.speed("fastest")
tw.penup()
tw.hideturtle()

colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

# ------- Cores randômicas -------


def _select_color():
    color = random.choice(colors)
    return color


# ------- Ajuste da posição inicial -------

tw.setheading(210)
tw.forward(300)
tw.setheading(0)
number_of_dots = 100

# ------- Repetição da marcação dos pontos -------

for dot_count in range(1, number_of_dots + 1):
    tw.dot(20, _select_color())
    tw.forward(50)

    if dot_count % 10 == 0:
        tw.setheading(90)
        tw.forward(50)
        tw.setheading(180)
        tw.forward(500)
        tw.setheading(0)

screen = Screen()
screen.exitonclick()