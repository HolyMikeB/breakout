from turtle import Turtle
ALIGNMENT = 'right'
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.lives = 3
        self.score = 0
        self.color('white')
        self.goto(300, 350)
        self.write(f'Score: {self.score} Lives: {self.lives}', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score} Lives: {self.lives}', align=ALIGNMENT, font=FONT)

    def reset_game(self):
        self.clear()
        self.score = 0
        self.write(f'Score: {self.score} Lives: {self.lives}', align=ALIGNMENT, font=FONT)

    def lose_life(self):
        self.lives -= 1
        self.clear()
        self.write(f'Score: {self.score} Lives: {self.lives}', align=ALIGNMENT, font=FONT)
