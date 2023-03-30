import turtle
from turtle import Turtle

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']

class Blocks:
    def __init__(self):
        self.blocks = []
        self.create_blocks()

    def create_blocks(self):
        x = -350
        y = 300
        rows = 0
        color = 0
        while rows < 6:
            for position in range(11):
                self.add_block((x, y), COLORS[color])
                x += 70
            x = -350
            y -= 30
            rows += 1
            color += 1

    def add_block(self, position, color):
        new_block = Turtle('square')
        new_block.color(color)
        new_block.up()
        new_block.shapesize(stretch_len=3, stretch_wid=1)
        new_block.goto(position)
        self.blocks.append(new_block)

    def reset_blocks(self):
        self.blocks = []
        turtle.clear()
        self.create_blocks()

