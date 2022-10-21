from turtle import Turtle, Screen

tw = Turtle()
pm = Turtle
screen = Screen()


def _move_up():
    tw.forward(10)


def _move_right():
    new_heading = tw.heading() - 10
    tw.setheading(new_heading)


def _move_down():
    tw.backward(10)


def _move_left():
    new_heading = tw.heading() + 10
    tw.setheading(new_heading)


def _clear_sketch():
    tw.clear()
    tw.penup()
    tw.home()
    tw.pendown()


screen.listen()
screen.onkey(key="d", fun=_move_right)
screen.onkey(key="w", fun=_move_up)
screen.onkey(key="a", fun=_move_left)
screen.onkey(key="s", fun=_move_down)
screen.onkey(key="c", fun=_clear_sketch)
screen.exitonclick()