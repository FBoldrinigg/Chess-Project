from Players import Player
from Board import Board
from Constants import ChessConstants
from Pieces import King

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
        if lastMove:
            self.newBoard.whitePieces, self.newBoard.blackPieces = self.newBoard.getSquares(self.whitePlayer.piecesAlive, self.blackPlayer.piecesAlive)
            self.newBoard.board = self.newBoard.updateBoard()
            self.turn += 1


    def capturePiece(self, lastMove, oponnentPieces, player):
        for index, pos in enumerate(oponnentPieces):
            if lastMove in pos.split("."):
                player.piecesAlive.pop(index)
        self.checkKings(player.piecesAlive)

    def checkKings(self, oppPlayer):
        isKingAlive = False
        for piece in oppPlayer:
            if isinstance(piece, King):
                isKingAlive = True
                break
        self.isGameOver = not isKingAlive

    def debugMode(self):
        localTurn = 0
        exitDebug = False
        while not exitDebug:
            selector = False
            self.newBoard.printBoard()
            print("\t\t ## DEBUG MODE ##")
            if localTurn == 0:
                print("\t## WHITE PLAYER'S TURN ##")
                lastMove = self.whitePlayer.movePiece(self.newBoard)
                self.capturePiece(lastMove, self.newBoard.blackPieces, self.blackPlayer)
                if lastMove == 0:
                    localTurn = 1
            elif localTurn == 1:
                print("\t## BLACK PLAYER'S TURN ##")
                lastMove = self.blackPlayer.movePiece(self.newBoard)
                self.capturePiece(lastMove, self.newBoard.whitePieces, self.whitePlayer)
                if lastMove == 0:
                    localTurn = 0
            if lastMove == 0:
                while isinstance(selector, bool):
                    try:
                        selector = int(input("0) Exit debug mode\n1) Continue\n"))
                        if selector == 0:
                            exitDebug = True
                        elif selector == 1:
                            pass
                        else:
                            raise ValueError
                    except ValueError:
                        print("Wrong input.")
                        selector = False
            self.newBoard.whitePieces, self.newBoard.blackPieces = self.newBoard.getSquares(self.whitePlayer.piecesAlive, self.blackPlayer.piecesAlive)
            self.newBoard.board = self.newBoard.updateBoard()
