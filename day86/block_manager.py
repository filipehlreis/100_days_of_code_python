from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class BlockManager:
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.add_block(6)

    def add_block(self, lines):
        y_position = +200
        for line in range(lines):
            y_position -= 20
            x_position = -260
            for collum in range(11):
                new_block = Turtle()
                new_block.shape("square")
                new_block.shapesize(1, 2)
                new_block.penup()
                new_block.color(COLORS[line])
                x_position += 43
                new_block.goto(x_position, y_position)
                # new_block.car_speed = MOVE_INCREblockT
                self.blocks.append(new_block)

        print(len(self.blocks))

    def remove_block(self, block):
        print(block)
        print(len(self.blocks))

        if block == len(self.blocks):
            block -= 1
        self.blocks[block].goto(1000, 1000)
        self.blocks.pop(block)

    def is_there_any_block_left(self):
        if len(self.blocks):
            return True
        return False
