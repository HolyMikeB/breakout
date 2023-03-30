import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 800)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle((0, -300))
ball = Ball()

blocks = Blocks()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.move_right, 'Right')
screen.onkeypress(paddle.move_left, 'Left')


while len(blocks.blocks) > 0 and scoreboard.lives > 0:
    screen.update()
    time.sleep(ball.move_speed)

    ball.ball_move()

    if not -380 < ball.xcor() < 380:
        ball.wall_bounce()
    if ball.ycor() > 390:
        ball.ceiling_bounce()
    if ball.ycor() < -380:
        ball.reset_ball()
        scoreboard.lose_life()
    if ball.distance(paddle) < 50 and ball.ycor() < -270:
        ball.paddle_bounce()
    for block in blocks.blocks:
        if ball.distance(block) < 50:
            ball.ceiling_bounce()
            block.hideturtle()
            blocks.blocks.remove(block)
            scoreboard.add_score()


if scoreboard.lives == 0:
    scoreboard.score = 0
    scoreboard.lives = 3
    blocks.reset_blocks()
    ball.reset_ball()
    scoreboard.reset_game()
else:
    blocks.reset_blocks()
    ball.reset_ball()

screen.exitonclick()
