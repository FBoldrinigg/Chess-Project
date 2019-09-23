from Constants import ChessConstants


class Piece:

    pos = ""
    timesMoved = 0

    def getPos(self):
        x_value = int(ChessConstants.X.index(self.pos[1]))
        y_value = int(ChessConstants.Y.index(self.pos[0]))
        return x_value, y_value

    def returnPos(self, x, y):
        return ChessConstants.Y[y] + ChessConstants.X[x]


class Pawn(Piece):

    def __init__(self, color, pos):
        self.color = color
        if self.color == ChessConstants.COLOR[0]:
            self.moveSet = [(0, 1), (0, 2)]
        else:
            self.moveSet = [(0, -1), (0, -2)]
        self.pos = pos

    def calculateMoves(self, board):
        x, y = self.getPos()
        possibleMoves = []
        if self.timesMoved > 0 and len(self.moveSet) > 1:
            self.moveSet.pop()
        for j in self.moveSet:
            if 0 <= x - j[1] <= 7:
                if board.board[x - j[1]][y] == "#":
                    possibleMoves.append(self.returnPos(x - j[1], y))
                else:
                    break
        if self.color == ChessConstants.COLOR[0]:
            for pos in board.blackPieces:
                if self.returnPos(x - 1, y - 1) in pos.split("."):
                    possibleMoves.append(self.returnPos(x - 1, y - 1))
                if self.returnPos(x - 1, y + 1) in pos.split("."):
                    possibleMoves.append(self.returnPos(x - 1, y + 1))
        if self.color == ChessConstants.COLOR[1]:
            for pos in board.whitePieces:
                if self.returnPos(x + 1, y - 1) in pos.split("."):
                    possibleMoves.append(self.returnPos(x + 1, y - 1))
                if self.returnPos(x + 1, y + 1) in pos.split("."):
                    possibleMoves.append(self.returnPos(x + 1, y + 1))
        return possibleMoves


class Knight(Piece):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-2,-1), (-2,1), (-1, 2), (1, 2), (2,1), (2,-1), (1,-2), (-1,-2)]
        self.pos = pos

    def calculateMoves(self, board):
        x, y = self.getPos()
        possibleMoves = []
        ownPieces = ""
        if self.color == ChessConstants.COLOR[0]:
            for piece in board.whitePieces:
                ownPieces += piece.split(".")[0]
        else:
            for piece in board.blackPieces:
                ownPieces += piece.split(".")[0]
        for j in self.moveSet:
            if 0 <= y + j[0] <= 7 and 0 <= x + j[1] <= 7:
                if self.returnPos(x + j[1], y + j[0]) not in ownPieces:
                    possibleMoves.append(self.returnPos(x + j[1], y + j[0]))
        return possibleMoves


class Bishop(Piece):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-1,-1), (-1,1), (1,1), (1,-1)]
        self.pos = pos

    def calculateMoves(self, board):
        x, y = self.getPos()
        possibleMoves = []
        ownPieces = ""
        if self.color == ChessConstants.COLOR[0]:
            for piece in board.whitePieces:
                ownPieces += piece.split(".")[0]
        else:
            for piece in board.blackPieces:
                ownPieces += piece.split(".")[0]
        for j in self.moveSet:
            for i in range(1, 8):
                if 0 <= y + j[0] * i <= 7 and 0 <= x + j[1] * i <= 7:
                    if board.board[x + j[1] * i][y + j[0] * i] == '#':
                        possibleMoves.append(self.returnPos(x + j[1] * i, y + j[0] * i))
                    elif self.returnPos(x + j[1] * i, y + j[0] * i) not in ownPieces:
                        possibleMoves.append(self.returnPos(x + j[1] * i, y + j[0] * i))
                        break
                    else:
                        break
        return possibleMoves

class Rook(Piece):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-1,0), (0,1), (1,0), (0,-1)]
        self.pos = pos

    def calculateMoves(self, board):
        x, y = self.getPos()
        possibleMoves = []
        ownPieces = ""
        if self.color == ChessConstants.COLOR[0]:
            for piece in board.whitePieces:
                ownPieces += piece.split(".")[0]
        else:
            for piece in board.blackPieces:
                ownPieces += piece.split(".")[0]
        for j in self.moveSet:
            for i in range(1, 8):
                if 0 <= y + j[0] * i <= 7 and 0 <= x + j[1] * i <= 7:
                    if board.board[x + j[1] * i][y + j[0] * i] == '#':
                        possibleMoves.append(self.returnPos(x + j[1] * i, y + j[0] * i))
                    elif self.returnPos(x + j[1] * i, y + j[0] * i) not in ownPieces:
                        possibleMoves.append(self.returnPos(x + j[1] * i, y + j[0] * i))
                        break
                    else:
                        break
        return possibleMoves


class Queen(Piece):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        self.pos = pos

    def calculateMoves(self, board):
        x, y = self.getPos()
        possibleMoves = []
        ownPieces = ""
        if self.color == ChessConstants.COLOR[0]:
            for piece in board.whitePieces:
                ownPieces += piece.split(".")[0]
        else:
            for piece in board.blackPieces:
                ownPieces += piece.split(".")[0]
        for j in self.moveSet:
            for i in range(1, 8):
                if 0 <= y + j[0] * i <= 7 and 0 <= x + j[1] * i <= 7:
                    if board.board[x + j[1] * i][y + j[0] * i] == '#':
                        possibleMoves.append(self.returnPos(x + j[1] * i, y + j[0] * i))
                    elif self.returnPos(x + j[1] * i, y + j[0] * i) not in ownPieces:
                        possibleMoves.append(self.returnPos(x + j[1] * i, y + j[0] * i))
                        break
                    else:
                        break
        return possibleMoves

class King(Piece):

    def __init__(self, color, pos):
        self.color = color
        self.moveSet = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        self.pos = pos

    def calculateMoves(self, board):
        x, y = self.getPos()
        possibleMoves = []
        ownPieces = ""
        if self.color == ChessConstants.COLOR[0]:
            for piece in board.whitePieces:
                ownPieces += piece.split(".")[0]
        else:
            for piece in board.blackPieces:
                ownPieces += piece.split(".")[0]
        for j in self.moveSet:
            if 0 <= x + j[1] <= 7 and 0 <= y + j[0] <= 7:
                if self.returnPos(x + j[1], y + j[0]) not in ownPieces:
                    possibleMoves.append(self.returnPos(x + j[1], y + j[0]))
        return possibleMoves
