from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05
        self.goto(0, 0)

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.up()
        self.speed("fastest")

    def reset_ball(self):
        self.reset()
        self.move_speed = 0.05
        self.create_ball()

    def wall_bounce(self):
        self.x_move *= -1

    def paddle_bounce(self):
        self.y_move *= -1

    def ceiling_bounce(self):
        self.y_move *= -1

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
