from turtle import Turtle

BLOCK_POSITIONS = [(-350, 300), (-280, 300), (-210, 300), (-140, 300), (-70, 300), (0, 300), (70, 300),
                   (140, 300), (210, 300), (280, 300), (350, 300)]

class Blocks:
    def __init__(self):
        self.blocks = []
        self.create_blocks()

    def create_blocks(self):
        for position in range(11):
            self.add_block(BLOCK_POSITIONS[position], 'white')

    def add_block(self, position, color):
        new_block = Turtle('square')
        new_block.color(color)
        new_block.up()
        new_block.shapesize(stretch_len=3, stretch_wid=1)
        new_block.goto(position)
        self.blocks.append(new_block)

