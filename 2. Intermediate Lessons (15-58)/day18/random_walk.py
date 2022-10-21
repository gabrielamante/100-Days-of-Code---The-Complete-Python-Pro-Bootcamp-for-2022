from turtle import colormode,Turtle,Screen
import random
import turtle

colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']

angles = [0,90,180,270]
turtle.colormode(255)
tw = Turtle()
tw.shape('circle')
is_on = True


# def _draw_shape(l):
#     angle = 360/l
#     for _ in range(l):
#         tw.forward(50)
#         tw.right(angle)


def _select_color():
    # color = random.choice(colors)
    # return color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color



def _select_direction():
    angle = random.choice(angles)
    return angle


def _random_walk():
    tw.pensize(10)
    tw.speed('fastest')
    tw.color(_select_color())
    tw.forward(50)
    tw.right(_select_direction())


while is_on:
    _random_walk()


screen = Screen()
screen.exitonclick()