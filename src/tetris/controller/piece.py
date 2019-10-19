from .block import Block

class Piece:

    def __init__(self):
        self.blocks = []

    @staticmethod
    def factory(num, height, width):
        if num == 0:
            return TBlock(height, width)


class TBlock(Piece):
    def __init__(self, height, width):
        Piece.__init__(self)
        self.blocks.append(Block('purple', height, width / 2))
        self.blocks.append(Block('purple', height - 1, width / 2 - 1))
        self.blocks.append(Block('purple', height - 1, width / 2))
        self.blocks.append(Block('purple', height - 1, width / 2 + 1))


class ZBlock(Piece):
    def __init__(self, height, width):
        Piece.__init__(self)
        self.blocks.append(Block('red', height, width / 2 - 1))
        self.blocks.append(Block('red', height, width / 2))
        self.blocks.append(Block('red', height - 1, width / 2))
        self.blocks.append(Block('red', height - 1, width / 2 + 1))


class SBlock(Piece):
    def __init__(self, height, width):
        Piece.__init__(self)
        self.blocks.append(Block('green', height, width / 2))
        self.blocks.append(Block('green', height, width / 2 + 1))
        self.blocks.append(Block('green', height - 1, width / 2 - 1))
        self.blocks.append(Block('green', height - 1, width / 2))


class LBlock(Piece):
    def __init__(self, height, width):
        Piece.__init__(self)
        self.blocks.append(Block('orange', height, width / 2))
        self.blocks.append(Block('orange', height - 1, width / 2 - 1))
        self.blocks.append(Block('orange', height - 1, width / 2))
        self.blocks.append(Block('orange', height - 1, width / 2 + 1))


class JBlock(Piece):
    def __init__(self, height, width):
        Piece.__init__(self)
        self.blocks.append(Block('blue', height, width / 2 + 1))
        self.blocks.append(Block('blue', height - 1, width / 2 - 1))
        self.blocks.append(Block('blue', height - 1, width / 2))
        self.blocks.append(Block('blue', height - 1, width / 2 + 1))


class IBlock(Piece):
    def __init__(self, height, width):
        Piece.__init__(self)
        self.blocks.append(Block('sky blue', height, width / 2 - 1))
        self.blocks.append(Block('sky blue', height - 1, width / 2 - 1))
        self.blocks.append(Block('sky blue', height - 1, width / 2))
        self.blocks.append(Block('sky blue', height - 1, width / 2 + 1))


class OBlock(Piece):
    def __init__(self, height, width):
        Piece.__init__(self)
        self.blocks.append(Block('yellow', height - 1, width / 2 - 2))
        self.blocks.append(Block('yellow', height - 1, width / 2 - 1))
        self.blocks.append(Block('yellow', height - 1, width / 2))
        self.blocks.append(Block('yellow', height - 1, width / 2 + 1))

