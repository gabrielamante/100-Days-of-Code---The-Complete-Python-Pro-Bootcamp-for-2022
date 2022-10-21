from turtle import Turtle, Screen
import random

colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white']

tw = Turtle()
tw.shape('circle')

# for _ in range(4):
#     tw.forward(200)
#     tw.left(90)

# for _ in range(10):
#     tw.forward(10)
#     tw.penup()
#     tw.forward(10)
#     tw.pendown()


def _draw_shape(l):
    angle = 360/l
    for _ in range(l):
        tw.forward(50)
        tw.right(angle)


def _select_color():
    color = random.choice(colors)
    return color


for shape in range(3,11):
    tw.color(_select_color())
    _draw_shape(shape)

screen = Screen()
screen.exitonclick()