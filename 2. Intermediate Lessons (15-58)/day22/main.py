from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Screen Object

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Play Pong!")
screen.tracer(0)

# Paddle Objects

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))

screen.listen()
screen.onkeypress(paddle_right._move_up, "Up")
screen.onkeypress(paddle_right._move_down, "Down")
screen.onkeypress(paddle_left._move_up, "w")
screen.onkeypress(paddle_left._move_down, "s")

# Ball Object

ball = Ball()

# Scoreboard Object

scoreboard = Scoreboard()

# Pont Game

game_is_on = True

while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball._move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball._bounce_ball()

    if ball.distance(paddle_right) < 60 and ball.xcor() > 320 or ball.distance(paddle_left) < 60 and ball.xcor() < -320:
        ball._bounce_paddle()
        
    
    if ball.xcor() > 370:
        ball._reset_position()
        scoreboard._increase_l_score()
    elif ball.xcor() < -370:
        ball._reset_position()
        scoreboard._increase_r_score()
    

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_is_on = False
        scoreboard._game_over()

screen.exitonclick()