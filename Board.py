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
            whitePieces.append(piece.pos)
        for piece in blackPlayer:
            blackPieces.append(piece.pos)
        return whitePieces, blackPieces


whitePlayer = Player(ChessConstants.COLOR[0])
blackPlayer = Player(ChessConstants.COLOR[1])
newBoard = Board(whitePlayer.piecesAlive, blackPlayer.piecesAlive)
newBoard.printBoard()
print("White: ", newBoard.whitePieces, "\nBlack: ", newBoard.blackPieces)
print("black pawn (c7): ", blackPlayer.piecesAlive[2].calculateMoves(newBoard))
print("White pawn (e2): ", whitePlayer.piecesAlive[4].calculateMoves(newBoard))
newBoard.blackPieces.append("d4")
newBoard.blackPieces.append("f3")
newBoard.blackPieces.append("d6")
print("White pawn (e2): ", whitePlayer.piecesAlive[4].calculateMoves(newBoard))
newBoard.whitePieces.append("b6")
newBoard.whitePieces.append("d5")
print("black pawn (c7): ", blackPlayer.piecesAlive[2].calculateMoves(newBoard))