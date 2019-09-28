from Players import Player
from Board import Board
from Constants import ChessConstants
from Pieces import Pawn, Knight, Bishop, Rook, Queen, King

class Engine:

    def __init__(self):
        self.turn = 1
        self.whitePlayer = Player(ChessConstants.COLOR[0], self.instantiateAll(ChessConstants.COLOR[0]))
        self.blackPlayer = Player(ChessConstants.COLOR[1], self.instantiateAll(ChessConstants.COLOR[1]))
        self.newBoard = Board(self.whitePlayer.piecesAlive, self.blackPlayer.piecesAlive)
        self.isGameOver = False
        self.loser = ""

    def assignTurn(self):
        self.newBoard.printBoard()
        if self.turn % 2 == 0:
            print(" ## BLACK PLAYER'S TURN ##")
            newPos, selectedPiece, oldPos = self.movePiece(self.blackPlayer)
            capturedPiece = self.capturePiece(newPos, self.newBoard.whitePieces, self.whitePlayer)
            if self.isKingInCheck(self.blackPlayer.piecesAlive, self.whitePlayer.piecesAlive) and newPos:
                if capturedPiece:
                    self.whitePlayer.piecesAlive.append(capturedPiece)
                selectedPiece.pos = oldPos
                selectedPiece.timesMoved -= 1
                newPos = ""
        else:
            print(" ## WHITE PLAYER'S TURN ##")
            newPos, selectedPiece, oldPos = self.movePiece(self.whitePlayer)
            capturedPiece = self.capturePiece(newPos, self.newBoard.blackPieces, self.blackPlayer)
            if self.isKingInCheck(self.whitePlayer.piecesAlive, self.blackPlayer.piecesAlive) and newPos:
                if capturedPiece:
                    self.blackPlayer.piecesAlive.append(capturedPiece)
                selectedPiece.pos = oldPos
                selectedPiece.timesMoved -= 1
                newPos = ""
        self.newBoard.whitePieces, self.newBoard.blackPieces = self.newBoard.getSquares(self.whitePlayer.piecesAlive, self.blackPlayer.piecesAlive)
        self.newBoard.board = self.newBoard.updateBoard()
        if newPos:
            self.turn += 1

    def capturePiece(self, lastMove, oponnentPieces, player):
        for index, pos in enumerate(oponnentPieces):
            if lastMove in pos.split("."):
                return player.piecesAlive.pop(index)

    def debugMode(self):
        localTurn = 0
        exitDebug = False
        while not exitDebug:
            selector = False
            self.newBoard.printBoard()
            print(" ## DEBUG MODE ##")
            if localTurn == 0:
                print(" ## WHITE PLAYER'S TURN ##")
                lastMove = self.movePiece(self.newBoard, self.whitePlayer)
                self.capturePiece(lastMove, self.newBoard.blackPieces, self.blackPlayer)
                if lastMove == 0:
                    localTurn = 1
            elif localTurn == 1:
                print(" ## BLACK PLAYER'S TURN ##")
                lastMove = self.movePiece(self.newBoard, self.blackPlayer)
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

    def winningScreen(self):
        print("## GAME OVER ##")
        if self.loser == ChessConstants.COLOR[0]:
            print("\nBLACK PLAYER WINS")
        else:
            print("\nWHITE PLAYER WINS")
        print("## Turns played:", self.turn - 1)

    def instantiateAll(self, color):
        piecesAlive = []
        if color == ChessConstants.COLOR[0]:
            for x in range(8):
                newPawn = Pawn(color, ChessConstants.WHITE_PAWN_POS[x])
                piecesAlive.append(newPawn)
            for x in range(2):
                newKnight = Knight(color, ChessConstants.WHITE_KNIGHT_POS[x])
                piecesAlive.append(newKnight)
                newBishop = Bishop(color, ChessConstants.WHITE_BISHOP_POS[x])
                piecesAlive.append((newBishop))
                newRook = Rook(color, ChessConstants.WHITE_ROOK_POS[x])
                piecesAlive.append(newRook)
            newQueen = Queen(color, ChessConstants.WHITE_QUEEN_POS)
            piecesAlive.append(newQueen)
            newKing = King(color, ChessConstants.WHITE_KING_POS)
            piecesAlive.append(newKing)
        elif color == ChessConstants.COLOR[1]:
            for x in range(8):
                newPawn = Pawn(color, ChessConstants.BLACK_PAWN_POS[x])
                piecesAlive.append(newPawn)
            for x in range(2):
                newKnight = Knight(color, ChessConstants.BLACK_KNIGHT_POS[x])
                piecesAlive.append(newKnight)
                newBishop = Bishop(color, ChessConstants.BLACK_BISHOP_POS[x])
                piecesAlive.append(newBishop)
                newRook = Rook(color, ChessConstants.BLACK_ROOK_POS[x])
                piecesAlive.append(newRook)
            newQueen = Queen(color, ChessConstants.BLACK_QUEEN_POS)
            piecesAlive.append(newQueen)
            newKing = King(color, ChessConstants.BLACK_KING_POS)
            piecesAlive.append(newKing)
        return piecesAlive

    def displayPiecesType(self, player):
        unitTypes = []
        for piece in player.piecesAlive:
            if type(piece) == Pawn and ChessConstants.PIECES_NAMES[0] not in unitTypes:
                unitTypes.append(ChessConstants.PIECES_NAMES[0])
            if type(piece) == Knight and ChessConstants.PIECES_NAMES[1] not in unitTypes:
                unitTypes.append(ChessConstants.PIECES_NAMES[1])
            if type(piece) == Bishop and ChessConstants.PIECES_NAMES[2] not in unitTypes:
                unitTypes.append(ChessConstants.PIECES_NAMES[2])
            if type(piece) == Rook and ChessConstants.PIECES_NAMES[3] not in unitTypes:
                unitTypes.append(ChessConstants.PIECES_NAMES[3])
            if type(piece) == Queen and ChessConstants.PIECES_NAMES[4] not in unitTypes:
                unitTypes.append(ChessConstants.PIECES_NAMES[4])
            if type(piece) == King and ChessConstants.PIECES_NAMES[5] not in unitTypes:
                unitTypes.append(ChessConstants.PIECES_NAMES[5])
        return unitTypes

    def getPiecesAndPosition(self, unitTypes, pieces):
        tempUnitStrings = ""
        index = 1
        print("\nNow displaying", unitTypes + "s:\n")
        for piece in pieces:
            if type(piece) == globals()[unitTypes]:
                tempUnitStrings = tempUnitStrings + unitTypes[0] + str(index) + ":" + piece.pos + "  "
                index += 1
        return tempUnitStrings

    def selectApiece(self, piecesCoord, unitType, pieces):
        selectPos = ""
        pieceIndex = False
        while not selectPos:
            try:
                selectPos = input(":").lower()
                if selectPos == "0":
                    return 0
                elif selectPos + "." + unitType not in piecesCoord:
                    raise ValueError
            except ValueError:
                print("Error. No ", unitType, " in that position")
                selectPos = ""
        for x, piece in enumerate(pieces):
            if selectPos == piece.pos:
                pieceIndex = x
                print(selectPos, unitType, "selected.")
        return pieces[pieceIndex]

    def selectNewPos(self, selectPiece, select):
        newPos = ""
        if not selectPiece:
            select = -1
        else:
            print("\n0) to cancel selection.\n")
            while not newPos:
                try:
                    newPos = input("Where to move: ")
                    if newPos == "0":
                        return 0, False
                    elif newPos not in self.calculateMoves(selectPiece):
                        raise ValueError
                except ValueError:
                    print("Wrong input. Invalid move.")
                    newPos = ""
            if not newPos:
                select = -1
        return select, newPos

    def movePiece(self, player):
        select = -1
        unitTypes = self.displayPiecesType(player)
        selectedPiece = False
        newPos = ""
        if player.color == ChessConstants.COLOR[0]:
            ownCoords = self.newBoard.whitePieces
        else:
            ownCoords = self.newBoard.blackPieces
        while select == -1:
            print("\n")
            for index, unit in enumerate(unitTypes):
                print(str(index + 1) + ")", unit)
            try:
                select = int(input("\nSelect type to list all it's remaining pieces: "))
                if not 0 <= select <= len(unitTypes):
                    raise ValueError
            except ValueError:
                print("Wrong input, must enter a valid index.")
                select = -1
            if select == 1:
                print(self.getPiecesAndPosition(unitTypes[0], player.piecesAlive), "\n\n0) to return\n")
                selectedPiece = self.selectApiece(ownCoords, unitTypes[0], player.piecesAlive)
                print(self.calculateMoves(selectedPiece) if selectedPiece else "")
                select, newPos = self.selectNewPos(selectedPiece, select)
            if select == 2:
                print(self.getPiecesAndPosition(unitTypes[1], player.piecesAlive), "\n\n0) to return\n")
                selectedPiece = self.selectApiece(ownCoords, unitTypes[1], player.piecesAlive)
                print(self.calculateMoves(selectedPiece) if selectedPiece else "")
                select, newPos = self.selectNewPos(selectedPiece, select)
            if select == 3:
                print(self.getPiecesAndPosition(unitTypes[2], player.piecesAlive), "\n\n0) to return\n")
                selectedPiece = self.selectApiece(ownCoords, unitTypes[2], player.piecesAlive)
                print(self.calculateMoves(selectedPiece) if selectedPiece else "")
                select, newPos = self.selectNewPos(selectedPiece, select)
            if select == 4:
                print(self.getPiecesAndPosition(unitTypes[3], player.piecesAlive), "\n\n0) to return\n")
                selectedPiece = self.selectApiece(ownCoords, unitTypes[3], player.piecesAlive)
                print(self.calculateMoves(selectedPiece) if selectedPiece else "")
                select, newPos = self.selectNewPos(selectedPiece, select)
            if select == 5:
                print(self.getPiecesAndPosition(unitTypes[4], player.piecesAlive), "\n\n0) to return\n")
                selectedPiece = self.selectApiece(ownCoords, unitTypes[4], player.piecesAlive)
                print(self.calculateMoves(selectedPiece) if selectedPiece else "")
                select, newPos = self.selectNewPos(selectedPiece, select)
            if select == 6:
                print(self.getPiecesAndPosition(unitTypes[5], player.piecesAlive), "\n\n0) to return\n")
                selectedPiece = self.selectApiece(ownCoords, unitTypes[5], player.piecesAlive)
                print(self.calculateMoves(selectedPiece) if selectedPiece else "")
                select, newPos = self.selectNewPos(selectedPiece, select)
            if select == 0:
                return 0, 0, 0
        oldPos = selectedPiece.pos
        selectedPiece.pos = newPos
        selectedPiece.timesMoved += 1
        return newPos, selectedPiece, oldPos

    def getPos(self, piece):
        x_value = int(ChessConstants.X.index(piece.pos[1]))
        y_value = int(ChessConstants.Y.index(piece.pos[0]))
        return x_value, y_value

    def returnPos(self, x, y):
        return ChessConstants.Y[y] + ChessConstants.X[x]

    def calculateMoves(self, selPiece):
        x, y = self.getPos(selPiece)
        possibleMoves = []
        ownPieces = ""
        if selPiece.color == ChessConstants.COLOR[0]:
            for piece in self.newBoard.whitePieces:
                ownPieces += piece.split(".")[0]
        else:
            for piece in self.newBoard.blackPieces:
                ownPieces += piece.split(".")[0]
        if isinstance(selPiece, Pawn):
            if selPiece.timesMoved > 0 and len(selPiece.moveSet) > 1:
                selPiece.moveSet.pop()
            for j in selPiece.moveSet:
                if 0 <= x - j[1] <= 7:
                    if self.newBoard.board[x - j[1]][y] == "#":
                        possibleMoves.append(self.returnPos(x - j[1], y))
                    else:
                        break
            if selPiece.color == ChessConstants.COLOR[0]:
                for pos in self.newBoard.blackPieces:
                    if 0 <= x - 1 <= 7 and 0 <= y - 1 <= 7:
                        if self.returnPos(x - 1, y - 1) in pos.split("."):
                            possibleMoves.append(self.returnPos(x - 1, y - 1))
                    if 0 <= x - 1 <= 7 and 0 <= y + 1 <= 7:
                        if self.returnPos(x - 1, y + 1) in pos.split("."):
                            possibleMoves.append(self.returnPos(x - 1, y + 1))
            else:
                for pos in self.newBoard.whitePieces:
                    if 0 <= x + 1 <= 7 and 0 <= y - 1 <= 7:
                        if self.returnPos(x + 1, y - 1) in pos.split("."):
                            possibleMoves.append(self.returnPos(x + 1, y - 1))
                    if 0 <= x + 1 <= 7 and 0 <= y + 1 <= 7:
                        if self.returnPos(x + 1, y + 1) in pos.split("."):
                            possibleMoves.append(self.returnPos(x + 1, y + 1))
        elif isinstance(selPiece, Knight):
            for j in selPiece.moveSet:
                if 0 <= y + j[0] <= 7 and 0 <= x + j[1] <= 7:
                    if self.returnPos(x + j[1], y + j[0]) not in ownPieces:
                        possibleMoves.append(self.returnPos(x + j[1], y + j[0]))
        elif isinstance(selPiece, Bishop) or isinstance(selPiece, Rook) or isinstance(selPiece, Queen):
            for j in selPiece.moveSet:
                for i in range(1, 8):
                    if 0 <= y + j[0] * i <= 7 and 0 <= x + j[1] * i <= 7:
                        if self.newBoard.board[x + j[1] * i][y + j[0] * i] == '#':
                            possibleMoves.append(self.returnPos(x + j[1] * i, y + j[0] * i))
                        elif self.returnPos(x + j[1] * i, y + j[0] * i) not in ownPieces:
                            possibleMoves.append(self.returnPos(x + j[1] * i, y + j[0] * i))
                            break
                        else:
                            break
        else:
            for j in selPiece.moveSet:
                if 0 <= x + j[1] <= 7 and 0 <= y + j[0] <= 7:
                    if self.returnPos(x + j[1], y + j[0]) not in ownPieces:
                        possibleMoves.append(self.returnPos(x + j[1], y + j[0]))
        return possibleMoves

    def isKingInCheck(self, pieces, oppPieces):
        self.newBoard.whitePieces, self.newBoard.blackPieces = self.newBoard.getSquares(self.whitePlayer.piecesAlive,
                                                                                        self.blackPlayer.piecesAlive)
        self.newBoard.board = self.newBoard.updateBoard()
        ownKingPos = False
        for piece in pieces:
            if isinstance(piece, King):
                ownKingPos = piece.pos
        for piece in oppPieces:
            if ownKingPos in self.calculateMoves(piece):
                print("####### INVALID MOVE. OWN KING IS IN CHECK #######")
                return True
        return False

