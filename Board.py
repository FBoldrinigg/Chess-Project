from Constants import ChessConstants
from Players import Player


class Board:

    def __init__(self, whitePlayer, blackPlayer):
        self.board = self.createBoard()
        self.whitePieces, self.blackPieces = self.getSquares(whitePlayer, blackPlayer)

    def createBoard(self):
        newBoard = []
        newBoard.append(["r", "n", "b", "q", "k", "b", "n", "r"])
        newBoard.append(["p"] * 8)
        for _ in range(4):
            newBoard.append(["#"] * 8)
        newBoard.append(["P"] * 8)
        newBoard.append(["R", "N", "B", "Q", "K", "B", "N", "R"])
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
            whitePieces.append(piece.pos+"." + str(piece.__class__.__name__))
        for piece in blackPlayer:
            blackPieces.append(piece.pos)
        return whitePieces, blackPieces


whitePlayer = Player(ChessConstants.COLOR[0])
blackPlayer = Player(ChessConstants.COLOR[1])
print("test2")
newBoard = Board(whitePlayer.piecesAlive, blackPlayer.piecesAlive)
print(newBoard.whitePieces)
whitePlayer.movePiece(newBoard.whitePieces)