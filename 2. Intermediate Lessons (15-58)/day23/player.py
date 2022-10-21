from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color('black')
        self.speed('fastest')
        self._refresh_run()
        self.setheading(90)


    def _move_player(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
    

    def _successfull_cross(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            False
    

    def _refresh_run(self):
        self.goto(STARTING_POSITION)
