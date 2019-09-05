from Players import Player
from Board import Board
from Constants import ChessConstants


class Engine:

    def __init__(self):
        self.turn = 1
        self.whitePlayer = Player(ChessConstants.COLOR[0])
        self.blackPlayer = Player(ChessConstants.COLOR[1])
        self.newBoard = Board(self.whitePlayer.piecesAlive, self.blackPlayer.piecesAlive)

    def assignTurn(self):
        if self.turn % 2 == 0:
            self.blackPlayer.movePiece(self.newBoard)
        else:
            self.whitePlayer.movePiece(self.newBoard)
        self.turn += 1
