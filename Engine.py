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
            currentPlayer = self.blackPlayer
            opponentPlayer = self.whitePlayer
        else:
            currentPlayer = self.whitePlayer
            opponentPlayer = self.blackPlayer
        print(" ## BLACK PLAYER'S TURN ##" if self.turn % 2 == 0 else " ## WHITE PLAYER'S TURN ##")
        print(" ## KING IS IN CHECK ## " if currentPlayer.inCheck else "")
        select = self.turnMenu(currentPlayer)
        if select == 1:
            newPos, selectedPiece, oldPos = self.movePiece(currentPlayer)
            capturedPiece = self.capturePiece(newPos, opponentPlayer)
            if self.isKingInCheck(currentPlayer.getKing().pos, opponentPlayer.piecesAlive) and newPos:
                print("\n\n### INVALID MOVE. OWN KING WILL BE / IS IN CHECK ###\n\n")
                if capturedPiece:
                        opponentPlayer.piecesAlive.append(capturedPiece)
                selectedPiece.pos = oldPos
                selectedPiece.timesMoved -= 1
                newPos = ""
            self.newBoard.whitePieces, self.newBoard.blackPieces = self.newBoard.getSquares(
                self.whitePlayer.piecesAlive,
                self.blackPlayer.piecesAlive
            )
            self.newBoard.board = self.newBoard.updateBoard()
            if newPos:
                self.check(currentPlayer, opponentPlayer)
                self.checkPromotion(selectedPiece, currentPlayer)
                if opponentPlayer.inCheck:
                    self.checkMate(currentPlayer, opponentPlayer)
                self.turn += 1
        if select == 2:
            rooks = self.checkCastle(currentPlayer)
            oldRookPos, selectedRook, oldKingPos = self.castle(rooks, currentPlayer)
            if self.isKingInCheck(currentPlayer.getKing().pos, opponentPlayer.piecesAlive):
                print("\n\n### INVALID MOVE. OWN KING WILL BE / IS IN CHECK ###\n\n")
                selectedRook.pos = oldRookPos
                currentPlayer.getKing().pos = oldKingPos
                self.newBoard.whitePieces, self.newBoard.blackPieces = self.newBoard.getSquares(self.whitePlayer.piecesAlive, self.blackPlayer.piecesAlive)
                self.newBoard.board = self.newBoard.updateBoard()
            else:
                self.check(currentPlayer, opponentPlayer)
                if opponentPlayer.inCheck:
                    self.checkMate(currentPlayer, opponentPlayer)
                selectedRook.timesMoved += 1
                currentPlayer.getKing().timesMoved += 1
                currentPlayer.hasCastled = True
                self.turn += 1

    def capturePiece(self, lastMove, oppPlayer):
        for index, piece in enumerate(oppPlayer.piecesAlive):
            if lastMove == piece.pos:
                return oppPlayer.piecesAlive.pop(index)

    def debugMode(self):
        exitDebug = False
        self.turn = 1
        while not exitDebug:
            selector = False
            self.newBoard.printBoard()
            print(" ## DEBUG MODE ##")
            self.newBoard.printBoard()
            if self.turn % 2 == 0:
                currentPlayer = self.blackPlayer
                opponentPlayer = self.whitePlayer
            else:
                currentPlayer = self.whitePlayer
                opponentPlayer = self.blackPlayer
            print(" ## BLACK PLAYER'S TURN ##" if self.turn % 2 == 0 else " ## WHITE PLAYER'S TURN ##")
            print(" ## KING IS IN CHECK ## " if currentPlayer.inCheck else "")
            select = self.turnMenu(currentPlayer)
            if select == 1:
                newPos, selectedPiece, oldPos = self.movePiece(currentPlayer)
                capturedPiece = self.capturePiece(newPos, opponentPlayer)
                if self.isKingInCheck(currentPlayer.getKing().pos, opponentPlayer.piecesAlive) and newPos:
                    if capturedPiece:
                        opponentPlayer.piecesAlive.append(capturedPiece)
                    selectedPiece.pos = oldPos
                    selectedPiece.timesMoved -= 1
                    newPos = ""
                self.newBoard.whitePieces, self.newBoard.blackPieces = self.newBoard.getSquares(
                    self.whitePlayer.piecesAlive, self.blackPlayer.piecesAlive)
                self.newBoard.board = self.newBoard.updateBoard()
                if newPos:
                    self.check(currentPlayer, opponentPlayer)
                    self.checkPromotion(selectedPiece, currentPlayer)
            if select == 2:
                rooks = self.checkCastle(currentPlayer.getRooks())
                oldRookPos, selectedRook, oldKingPos = self.castle(rooks, currentPlayer)
                if self.isKingInCheck(currentPlayer.getKing().pos, opponentPlayer.piecesAlive):
                    selectedRook.pos = oldRookPos
                    currentPlayer.getKing().pos = oldKingPos
                    self.newBoard.whitePieces, self.newBoard.blackPieces = self.newBoard.getSquares(
                        self.whitePlayer.piecesAlive, self.blackPlayer.piecesAlive)
                    self.newBoard.board = self.newBoard.updateBoard()
                else:
                    self.check(currentPlayer, opponentPlayer)
            if newPos == 0:
                while isinstance(selector, bool):
                    try:
                        selector = int(input("0) Exit debug mode\n1) Continue\n"))
                        if selector == 0:
                            exitDebug = True
                        elif selector == 1:
                            self.turn += 1
                        else:
                            raise ValueError
                    except ValueError:
                        print("Wrong input.")
                        selector = False
            self.newBoard.whitePieces, self.newBoard.blackPieces = self.newBoard.getSquares(self.whitePlayer.piecesAlive, self.blackPlayer.piecesAlive)
            self.newBoard.board = self.newBoard.updateBoard()

    def winningScreen(self):
        print("\n", ["#"] * 30)
        print("\n### CHECKMATE ###\n### GAME OVER ###")
        if self.loser == ChessConstants.COLOR[0]:
            print("\nBLACK PLAYER WINS")
        else:
            print("\nWHITE PLAYER WINS")
        print("### Turns played:", self.turn - 1)
        print("\n ### Last board state:")
        self.newBoard.printBoard()
        print("\n", ["#"] * 30)

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

    def selectPiece(self, piecesCoord, unitType, pieces):
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
                selectedPiece = self.selectPiece(ownCoords, unitTypes[0], player.piecesAlive)
                print(self.calculateMoves(selectedPiece) if selectedPiece else "")
                select, newPos = self.selectNewPos(selectedPiece, select)
            if select == 2:
                print(self.getPiecesAndPosition(unitTypes[1], player.piecesAlive), "\n\n0) to return\n")
                selectedPiece = self.selectPiece(ownCoords, unitTypes[1], player.piecesAlive)
                print(self.calculateMoves(selectedPiece) if selectedPiece else "")
                select, newPos = self.selectNewPos(selectedPiece, select)
            if select == 3:
                print(self.getPiecesAndPosition(unitTypes[2], player.piecesAlive), "\n\n0) to return\n")
                selectedPiece = self.selectPiece(ownCoords, unitTypes[2], player.piecesAlive)
                print(self.calculateMoves(selectedPiece) if selectedPiece else "")
                select, newPos = self.selectNewPos(selectedPiece, select)
            if select == 4:
                print(self.getPiecesAndPosition(unitTypes[3], player.piecesAlive), "\n\n0) to return\n")
                selectedPiece = self.selectPiece(ownCoords, unitTypes[3], player.piecesAlive)
                print(self.calculateMoves(selectedPiece) if selectedPiece else "")
                select, newPos = self.selectNewPos(selectedPiece, select)
            if select == 5:
                print(self.getPiecesAndPosition(unitTypes[4], player.piecesAlive), "\n\n0) to return\n")
                selectedPiece = self.selectPiece(ownCoords, unitTypes[4], player.piecesAlive)
                print(self.calculateMoves(selectedPiece) if selectedPiece else "")
                select, newPos = self.selectNewPos(selectedPiece, select)
            if select == 6:
                print(self.getPiecesAndPosition(unitTypes[5], player.piecesAlive), "\n\n0) to return\n")
                selectedPiece = self.selectPiece(ownCoords, unitTypes[5], player.piecesAlive)
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

    def isKingInCheck(self, ownKingPos, oppPieces):
        self.newBoard.whitePieces, self.newBoard.blackPieces = self.newBoard.getSquares(self.whitePlayer.piecesAlive,
                                                                                        self.blackPlayer.piecesAlive)
        self.newBoard.board = self.newBoard.updateBoard()
        for piece in oppPieces:
            if ownKingPos in self.calculateMoves(piece):
                return True
        return False

    def check(self, currentPlayer, opponentPlayer):
        oppKing = opponentPlayer.getKing().pos
        for piece in currentPlayer.piecesAlive:
            if oppKing in self.calculateMoves(piece):
                opponentPlayer.inCheck = True
                return
        opponentPlayer.inCheck = False

    def checkPromotion(self, selectedPiece, currentPlayer):
        if isinstance(selectedPiece, Pawn):
            if selectedPiece.color == ChessConstants.COLOR[0]:
                if selectedPiece.pos[-1] == ChessConstants.X[0]:
                    self.promote(selectedPiece, currentPlayer)
            else:
                if selectedPiece.pos[-1] == ChessConstants.X[-1]:
                    self.promote(selectedPiece, currentPlayer)

    def promote(self, selectedPiece, currentPlayer):
        select = ""
        print("\nPromoting", selectedPiece.pos, "Pawn:")
        print("1) Promote to Knight.\n2) Promote to Bishop\n3) Promote to Rook\n4) Promote to Queen")
        while not select:
            try:
                select = int(input(": "))
                if not 1 <= select <= 4:
                    raise ValueError
            except ValueError:
                print("Invalid input. Must be an integer between 1 and 4.\n")
                select = ""
        if select == 1:
            newPiece = Knight(selectedPiece.color, selectedPiece.pos)
            newPiece.timesMoved = selectedPiece.timesMoved
        elif select == 2:
            newPiece = Bishop(selectedPiece.color, selectedPiece.pos)
            newPiece.timesMoved = selectedPiece.timesMoved
        elif select == 3:
            newPiece = Rook(selectedPiece.color, selectedPiece.pos)
            newPiece.timesMoved = selectedPiece.timesMoved
        else:
            newPiece = Queen(selectedPiece.color, selectedPiece.pos)
            newPiece.timesMoved = selectedPiece.timesMoved
        currentPlayer.piecesAlive.remove(selectedPiece)
        currentPlayer.piecesAlive.append(newPiece)

    def checkCastle(self, currentPlayer):
        rooks = currentPlayer.getRooks()
        validRooks = currentPlayer.getRooks()
        for rook in rooks:
            if rook.timesMoved == 0 and currentPlayer.getKing().timesMoved == 0:
                for pos in ChessConstants.CASTLE_DIC[rook.pos]:
                    x = int(ChessConstants.X.index(pos[1]))
                    y = int(ChessConstants.Y.index(pos[0]))
                    if not self.newBoard.board[x][y] == "#":
                        validRooks.remove(rook)
                        break
            else:
                validRooks.remove(rook)
        return validRooks

    def castle(self, rooks, currentPlayer):
        select = False
        selectedRookPos, selectedRook, oldKingPos = "", "", ""
        for index, rook in enumerate(rooks):
            print(str(index + 1) + ")", rook.pos)
        while not select:
            try:
                select = int(input("Select rook: "))
                if not 1 <= select <= len(rooks):
                    raise ValueError
            except ValueError:
                print("Invalid input.")
                select = False
        if select == 1:
            selectedRook = rooks[0]
            selectedRookPos = rooks[0].pos
            rooks[0].pos = ChessConstants.CASTLE_DIC[selectedRookPos][-1]
            oldKingPos = currentPlayer.getKing().pos
            currentPlayer.getKing().pos = ChessConstants.CASTLE_DIC[selectedRookPos][-2]
        if select == 2:
            selectedRook = rooks[1]
            selectedRookPos = rooks[1].pos
            rooks[1].pos = ChessConstants.CASTLE_DIC[selectedRookPos][-1]
            oldKingPos = currentPlayer.getKing().pos
            currentPlayer.getKing().pos = ChessConstants.CASTLE_DIC[selectedRookPos][-2]
        return selectedRookPos, selectedRook, oldKingPos

    def checkMate(self, currentPlayer, opponentPlayer):
        validMoves = []
        for piece in opponentPlayer.piecesAlive:
            originalPosition = piece.pos
            availableMoves = self.calculateMoves(piece)
            if availableMoves:
                for move in availableMoves:
                    piece.pos = move
                    piece.timesMoved += 1
                    capturedPiece = self.capturePiece(move, currentPlayer)
                    if self.isKingInCheck(opponentPlayer.getKing().pos, currentPlayer.piecesAlive):
                        if capturedPiece:
                            currentPlayer.piecesAlive.append(capturedPiece)
                        piece.pos = originalPosition
                        piece.timesMoved -= 1
                    else:
                        validMoves.append(piece.__class__.__name__ + "." + originalPosition + " to " + move)
                        if capturedPiece:
                            currentPlayer.piecesAlive.append(capturedPiece)
                        piece.pos = originalPosition
                        piece.timesMoved -= 1
                        break

        self.newBoard.whitePieces, self.newBoard.blackPieces = self.newBoard.getSquares(self.whitePlayer.piecesAlive,
                                                                                        self.blackPlayer.piecesAlive)
        self.newBoard.board = self.newBoard.updateBoard()
        if not validMoves:
            self.isGameOver = True
            self.loser = opponentPlayer.color

    def turnMenu(self, currentPlayer):
        menu = ["Move piece"]
        select = False
        if not currentPlayer.hasCastled:
            if self.checkCastle(currentPlayer):
                menu.append("Castle")
        for index, option in enumerate(menu):
            print(str(index + 1) + ")", option)
        while not select:
            try:
                select = int(input(": "))
                if not 1 <= select <= len(menu):
                    raise ValueError
            except ValueError:
                print("Wrong input. Must enter a valid index.")
                select = False
        return select
