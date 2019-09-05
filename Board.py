from Constants import ChessConstants
from Pieces import Piece


class Board:

    def __init__(self, whitePlayer, blackPlayer):
        self.whitePieces, self.blackPieces = self.getSquares(whitePlayer, blackPlayer)
        self.board = self.updateBoard()

    def updateBoard(self):
        newBoard = [["#"] * 8 for _ in range(8)]
        for piece in self.whitePieces:
            y_value = int(ChessConstants.Y.index(piece[0]))
            x_value = int(ChessConstants.X.index(piece[1]))
            newBoard[x_value][y_value] = piece[3]
        for piece in self.blackPieces:
            y_value = int(ChessConstants.Y.index(piece[0]))
            x_value = int(ChessConstants.X.index(piece[1]))
            newBoard[x_value][y_value] = piece[3].lower()
        return newBoard

    def printBoard(self):
        print("\n")
        print(" ", ChessConstants.Y, "\n")
        for x in range(8):
            print(ChessConstants.X[x], self.board[x], ChessConstants.X[x])
        print("\n ", ChessConstants.Y, "\n")

    def getSquares(self, whitePlayer, blackPlayer):
        whitePieces = []
        blackPieces = []
        for piece in whitePlayer:
            whitePieces.append(piece.pos + "." + str(piece.__class__.__name__))
        for piece in blackPlayer:
            blackPieces.append(piece.pos + "." + str(piece.__class__.__name__))
        return whitePieces, blackPieces
