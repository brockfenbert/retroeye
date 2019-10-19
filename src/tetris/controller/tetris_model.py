# Model for a game of Tetris
"""
NO DOCUMENTATION NEEDED BOIS
"""
import random
from .piece import Piece

class TetrisModel:

    # Constructor for Tetris that takes in the width and height to use
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = self.make_board()
        self.next_pieces = self.random_pieces()
        self.shift = None
        self.canShift = True
        # TODO: change this to a new random piece
        self.falling = self.get_random_piece()
        self.score = 0

    # make a blank board of Tetris
    def make_board(self):
        board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(None)
            board.append(row)

        return board

    # return this width of this game of Tetris
    def get_width(self):
        return self.width

    # return the height of this game of Tetris
    def get_height(self):
        return self.height

    # get the block at the given location
    def get_block_at(self, col, row):
        return self.board[col][row]

    # get the shift piece, set the ability to shift to false
    def get_shift(self):
        return self.shift

    # swap the shift and falling piece
    def swap_shift(self):
        if self.canShift:
            temp = self.shift
            self.shift = self.falling
            self.falling = temp
            self.canShift = False

    # rotate the piece that is currently falling
    def rotate_falling(self):
        if self.falling is not None:
            self.rotate_piece()

    # rotate a piece given that the piece is not None
    def rotate_piece(self):
        new_piece = self.falling.rotate()
        if self.is_valid_move(new_piece):
            self.falling = new_piece

    # get the list of the next pieces
    def get_next_pieces(self):
        return self.next_pieces

    # move the piece horizontally
    def move_horizontal(self, dirc):
        new_piece = self.falling.shift(dirc)
        if self.is_valid_move(new_piece):
            self.falling = new_piece

    # determine if the given piece is a valid location
    def is_valid_move(self, new_piece):
        for block in new_piece.get_blocks():
            loc = block.get_location()
            x = loc.get_x()
            y = loc.get_y()
            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                return False
            if self.board[x][y] is not None:
                return False
        return True

    # get how many lines have been cleared
    def get_score(self):
        return self.score

    # apply gravity to the current piece on the board
    def apply_gravity(self):
        new_piece = self.falling.move_down()
        if self.is_valid_move(new_piece):
            self.falling = new_piece
        else:
            self.add_piece_to_board()
            self.clear_lines()

    # clear all lines and shift down the rest of the lines in the game
    def clear_lines(self):
        i = 0
        while i < self.height:
            row = self.board[i]
            full = True
            for block in row:
                if block is None:
                    i += 1
                    full = False
                    break
            if full:
                self.board.pop(i)
                self.board.append(self.blank_row())

    # get a blank row of blocks
    def blank_row(self):
        row = []
        for i in range(self.width()):
            row.append(None)
        return row

    # get a random piece of Tetris
    def get_random_piece(self):
        num = random.randint(0, 6)
        return Piece.factory(num, self.height, self.width)

    # get a list of the next possible pieces
    def random_pieces(self):
        pieces = []
        for i in range(3):
            pieces.append(self.get_random_piece())
        return pieces

    # send the currently falling piece to the bottom of the board
    def send_piece(self):
        new_piece = self.falling.move_down()
        if self.is_valid_move(new_piece):
            self.falling = new_piece
            self.send_piece()
        else:
            self.add_piece_to_board()
            self.clear_lines()

    # add the currently falling piece to the board and replace it with a new falling piece
    def add_piece_to_board(self):
        for block in self.falling.get_blocks():
            loc = block.get_location()
            self.board[loc.get_x()].pop(loc.get_y())
            self.board[loc.get_x()].insert(loc.get_y(), block)
        self.falling = self.next_pieces[0]
        self.next_pieces.append(self.get_random_piece())

    # check if the game is over
    def is_game_over(self):
        return not self.is_valid_move(self.falling)
