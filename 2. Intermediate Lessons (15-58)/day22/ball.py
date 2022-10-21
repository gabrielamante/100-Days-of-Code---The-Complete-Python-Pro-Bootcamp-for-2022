from turtle import Turtle

INITIAL_POSITION = (0,0)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color('white')
        self.speed('fastest')
        self.x_move = 10
        self.y_move = 10
        self.movespeed = 0.1



    def _move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    

    def _bounce_ball(self):
        self.y_move *= -1
        self.movespeed *= 0.9
    

    def _bounce_paddle(self):
        self.x_move *= -1
        self.movespeed *= 0.9
    

    def _reset_position (self):
        self.goto(0, 0)
        self.movespeed = 0.1
        self._bounce_paddle()