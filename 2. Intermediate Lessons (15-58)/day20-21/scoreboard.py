from turtle import Turtle
SCORE = 0
ALIGNMENT = 'center'
FONT = ('Verdana',20,'normal')

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = SCORE
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self._update_scoreboard()


    def _update_scoreboard(self):
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)
        

    def _increase_score(self):
        self.score += 1
        self.clear()
        self._update_scoreboard()
    

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)