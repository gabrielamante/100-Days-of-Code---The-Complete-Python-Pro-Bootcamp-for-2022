from turtle import Turtle, Screen

SNAKE_START = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:


    def __init__(self):
        self.snake_group = []
        self._create_snake()
        self.head = self.snake_group[0]


    def _create_snake(self):
        for position in SNAKE_START:
            self.add_segment(position)


    def _move(self):
        for snake_num in range (len(self.snake_group)-1, 0, -1):
            new_x = self.snake_group[snake_num-1].xcor()
            new_y = self.snake_group[snake_num-1].ycor()
            self.snake_group[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    

    def _move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def _move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def _move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def _move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    

    def extend(self):
        self.add_segment(self.snake_group[-1].position())
    

    def add_segment(self, position):
        snake = Turtle(shape='square')
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_group.append(snake)
    

    def _reset_snake(self):
        for seg in self.snake_group:
            seg.goto(1000,1000)
        self.snake_group.clear()
        self._create_snake()
        self.head = self.snake_group[0]