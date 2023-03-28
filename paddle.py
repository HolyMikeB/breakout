from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, start_loc):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.up()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed('fastest')
        self.goto(start_loc)

    def move_left(self):
        current_x = self.xcor()
        self.setx(current_x - MOVE_DISTANCE)

    def move_right(self):
        current_x = self.xcor()
        self.setx(current_x + MOVE_DISTANCE)
