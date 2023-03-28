import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(800, 1000)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle((0, -400))
ball = Ball()

screen.listen()
screen.onkeypress(paddle.move_right, 'Right')
screen.onkeypress(paddle.move_left, 'Left')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.ball_move()

    if not -380 < ball.xcor() < 380:
        ball.wall_bounce()
    if ball.ycor() > 490:
        ball.ceiling_bounce()
    if ball.ycor() < -480:
        ball.reset_ball()
    if ball.distance(paddle) < 50 and ball.ycor() < -370:
        ball.paddle_bounce()

screen.exitonclick()
