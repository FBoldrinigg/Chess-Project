from Constants import ChessConstants
from Pieces import Pawn


class Board:

    def __init__(self):
        self.board = self.createBoard()
        self.turn = 1

    def createBoard(self):
        newBoard = []
        newBoard.append(["R", "K", "B", "Q", "ⓚ", "B", "K", "R"])
        newBoard.append(["P"] * 8)
        for _ in range(4):
            newBoard.append(["#"] * 8)
        newBoard.append(["P"] * 8)
        newBoard.append(["R", "K", "B", "Q", "ⓚ", "B", "K", "R"])
        return newBoard

    def printBoard(self):
        print("\n")
        print(" ", ChessConstants.Y, "\n")
        for x in range(8):
            print(ChessConstants.X[x], self.board[x], ChessConstants.X[x])
        print("\n ", ChessConstants.Y, "\n")





newBoard = Board()
newBoard.printBoard()
newPawn = Pawn(ChessConstants.color[0])
print(newPawn.color)
newPawn.pos = "c5"
print(newPawn.pos)
print(newPawn.calculateMoves(newBoard.board))
