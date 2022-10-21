import random
from turtle import Turtle, Screen
import turtle

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-150, -90, -30, 30, 90, 150]
turtles = []


for turtle_index in range(0,6):
    tw = Turtle(shape='turtle')
    tw.color(colors[turtle_index])
    tw.penup()
    tw.goto(-230, y_pos[turtle_index])
    turtles.append(tw)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won! The winning turtle is {winning_color}.")
            else:
                 print("You've lost. The winning turtle is {winning_color}.")
        turtle.forward(random.randint(0,10))


screen.exitonclick()