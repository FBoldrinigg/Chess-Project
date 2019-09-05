from Players import Player
from Board import Board
from Constants import ChessConstants


class Engine:

    def __init__(self):
        self.turn = 1
        self.whitePlayer = Player(ChessConstants.COLOR[0])
        self.blackPlayer = Player(ChessConstants.COLOR[1])
        self.newBoard = Board(self.whitePlayer.piecesAlive, self.blackPlayer.piecesAlive)
        self.isGameOver = False

    def assignTurn(self):
        self.newBoard.printBoard()
        if self.turn % 2 == 0:
            lastMove = self.blackPlayer.movePiece(self.newBoard)
            self.capturePiece(lastMove, self.newBoard.whitePieces, self.whitePlayer)
        else:
            lastMove = self.whitePlayer.movePiece(self.newBoard)
            self.capturePiece(lastMove, self.newBoard.blackPieces, self.blackPlayer)
        self.newBoard.whitePieces, self.newBoard.blackPieces= self.newBoard.getSquares(self.whitePlayer.piecesAlive,
                                                                                       self.blackPlayer.piecesAlive)
        self.newBoard.board = self.newBoard.updateBoard()
        self.turn += 1

    def capturePiece(self, lastMove, oponnentPieces, player):
        for index, pos in enumerate(oponnentPieces):
            if lastMove in pos.split("."):
                player.piecesAlive.pop(index)

