from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier",60,"normal")

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self._update_scoreboard()
    

    def _update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align='left',font=FONT)
        self.goto(100,200)
        self.write(self.r_score, align='right',font=FONT)


    def _increase_l_score(self):
        self.l_score += 1
        self._update_scoreboard()

    
    def _increase_r_score(self):
        self.r_score += 1
        self._update_scoreboard()


    def _game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)