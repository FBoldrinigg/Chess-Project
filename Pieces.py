from Constants import ChessConstants


class Piece:

    pos = ""
    timesMoved = 0
    color = ""
    moveSet = []


class Pawn(Piece):

    def __init__(self, color, pos):
        self.color = color
        if self.color == ChessConstants.COLOR[0]:
            self.moveSet = [(0, 1), (0, 2)]
        else:
            self.moveSet = [(0, -1), (0, -2)]
        self.pos = pos


class Knight(Piece):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-2,-1), (-2,1), (-1, 2), (1, 2), (2,1), (2,-1), (1,-2), (-1,-2)]
        self.pos = pos


class Bishop(Piece):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-1,-1), (-1,1), (1,1), (1,-1)]
        self.pos = pos


class Rook(Piece):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-1,0), (0,1), (1,0), (0,-1)]
        self.pos = pos


class Queen(Piece):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        self.pos = pos


class King(Piece):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        self.pos = pos
