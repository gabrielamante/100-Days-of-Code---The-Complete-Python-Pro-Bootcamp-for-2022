from turtle import colormode,Turtle,Screen
import random
import turtle

turtle.colormode(255)
tw = Turtle()
tw.shape('circle')
is_on = True


def _select_color():
    # color = random.choice(colors)
    # return color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def _spirograph(pace):
    for _ in range(int(360/pace)):
        tw.speed('fastest')
        tw.circle(100)
        tw.color(_select_color())
        tw.setheading(tw.heading() + pace)

_spirograph(10)

screen = Screen()
screen.exitonclick()