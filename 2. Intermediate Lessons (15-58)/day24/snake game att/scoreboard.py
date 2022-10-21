from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Verdana',20,'normal')

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/../../Desktop/data.txt",mode="r") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self._update_scoreboard()


    def _update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}  High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)
        

    def _increase_score(self):
        self.score += 1
        self._update_scoreboard()
    

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)


    def _reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self._update_scoreboard()
