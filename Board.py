from Constants import ChessConstants


class Board:

    def __init__(self, whitePlayer, blackPlayer):
        self.whitePieces, self.blackPieces = self.getSquares(whitePlayer, blackPlayer)
        self.board = self.updateBoard()

    def updateBoard(self):
        newBoard = [["#"] * 8 for _ in range(8)]
        for piece in self.whitePieces:
            y = int(ChessConstants.Y.index(piece[0]))
            x = int(ChessConstants.X.index(piece[1]))
            newBoard[x][y] = ChessConstants.PIECES_NAMES_DIC[piece[3:5]]
        for piece in self.blackPieces:
            y = int(ChessConstants.Y.index(piece[0]))
            x = int(ChessConstants.X.index(piece[1]))
            newBoard[x][y] =  ChessConstants.PIECES_NAMES_DIC[piece[3:5]].lower()
        return newBoard

    def printBoard(self):
        print("\n")
        print("   \t\t\t\t\t\t\t  ", ChessConstants.Y, "\n")
        for x in range(8):
            print("\t\t\t\t\t\t\t", ChessConstants.X[x], self.board[x], ChessConstants.X[x])
        print("\n   \t\t\t\t\t\t\t  ", ChessConstants.Y, "\n")

    def getSquares(self, whitePlayer, blackPlayer):
        whitePieces = []
        blackPieces = []
        for piece in whitePlayer:
            whitePieces.append(piece.pos + "." + str(piece.__class__.__name__))
        for piece in blackPlayer:
            blackPieces.append(piece.pos + "." + str(piece.__class__.__name__))
        return whitePieces, blackPieces
