class Block:
    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_color(self):
        return self.color
