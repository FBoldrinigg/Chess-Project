from Constants import ChessConstants


class Pieces:

    pos = ""
    color = ""

    def getPos(self):
        x_value = int(ChessConstants.X.index(self.pos[1]))
        y_value = int(ChessConstants.Y.index(self.pos[0]))
        return x_value, y_value

    def returnPos(self, x, y):
        return ChessConstants.Y[y] + ChessConstants.X[x]


class Pawn(Pieces):

    def __init__(self, color, pos):
        self.color = color
        if self.color == ChessConstants.COLOR[0]:
            self.moveSet = [(0, 1), (0, 2)]
        else:
            self.moveSet = [(0, -1), (0, -2)]
        self.timesMoved = 0
        self.pos = pos

    def calculateMoves(self, board):
        x, y = self.getPos()
        possibleMoves = []
        if self.timesMoved > 0:
            self.moveSet.pop()
        for j in self.moveSet:
            if 0 <= x - j[1] <= 7:
                if board[x - j[1]][y] == "#":
                    possibleMoves.append(self.returnPos(x - j[1], y))
        # Agregar check de piezas del color opuesto en (-1,1) y (1,1)
        return possibleMoves


class Bishop(Pieces):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-1,-1), (-1,1), (1,1), (1,-1)]
        self.pos = pos

class Knight(Pieces):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-2,-1), (-2,1), (-1, 2), (1, 2), (2,1), (2,-1), (1,-2), (-1,-2)]
        self.pos = pos


class Rook(Pieces):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-1,0), (0,1), (1,0), (0,-1)]
        self.timesMoved = 0
        self.pos = pos

class Queen(Pieces):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        self.pos = pos


class King(Pieces):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        self.timesMoved = 0
        self.pos = pos
