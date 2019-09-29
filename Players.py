from Pieces import Rook, King


class Player:

    def __init__(self, color, pieces):
        self.color = color
        self.piecesAlive = pieces
        self.inCheck = False

    def getKing(self):
        for piece in self.piecesAlive:
            if isinstance(piece, King):
                return piece

    def getRooks(self):
        rooks = []
        for piece in self.piecesAlive:
            if isinstance(piece, Rook):
                rooks.append(piece)
        return rooks