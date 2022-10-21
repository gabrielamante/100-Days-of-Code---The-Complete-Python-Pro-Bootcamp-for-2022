from turtle import Turtle

ALIGNMENT = 'left'
FONT = ("Courier", 24, "normal")
INITIAL_LEVEL = 1


class Scoreboard(Turtle):
    

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = INITIAL_LEVEL
        self._update_scoreboard()

    
    def _update_scoreboard(self):
        self.clear()
        self.goto(-250,250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
    

    def _increase_level(self):
        self.level += 1
        self._update_scoreboard()
    

    def _game_over(self):
        self.goto(-90,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
