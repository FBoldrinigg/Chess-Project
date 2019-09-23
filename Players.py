from Constants import ChessConstants
from Pieces import Pawn, Knight, Rook, Bishop, Queen, King


class Player:

    def __init__(self, color):
        self.color = color
        self.piecesAlive = self.instantiateAll()

    def instantiateAll(self):
        piecesAlive = []
        if self.color == ChessConstants.COLOR[0]:
            for x in range(8):
                newPawn = Pawn(self.color, ChessConstants.WHITE_PAWN_POS[x])
                piecesAlive.append(newPawn)
            for x in range(2):
                newKnight = Knight(self.color, ChessConstants.WHITE_KNIGHT_POS[x])
                piecesAlive.append(newKnight)
                newBishop = Bishop(self.color, ChessConstants.WHITE_BISHOP_POS[x])
                piecesAlive.append((newBishop))
                newRook = Rook(self.color, ChessConstants.WHITE_ROOK_POS[x])
                piecesAlive.append(newRook)
            newQueen = Queen(self.color, ChessConstants.WHITE_QUEEN_POS)
            piecesAlive.append(newQueen)
            newKing = King(self.color, ChessConstants.WHITE_KING_POS)
            piecesAlive.append(newKing)
        elif self.color == ChessConstants.COLOR[1]:
            for x in range(8):
                newPawn = Pawn(self.color, ChessConstants.BLACK_PAWN_POS[x])
                piecesAlive.append(newPawn)
            for x in range(2):
                newKnight = Knight(self.color, ChessConstants.BLACK_KNIGHT_POS[x])
                piecesAlive.append(newKnight)
                newBishop = Bishop(self.color, ChessConstants.BLACK_BISHOP_POS[x])
                piecesAlive.append(newBishop)
                newRook = Rook(self.color, ChessConstants.BLACK_ROOK_POS[x])
                piecesAlive.append(newRook)
            newQueen = Queen(self.color, ChessConstants.BLACK_QUEEN_POS)
            piecesAlive.append(newQueen)
            newKing = King(self.color, ChessConstants.BLACK_KING_POS)
            piecesAlive.append(newKing)
        return piecesAlive

    def displayPiecesType(self):
        unitTypes = set()
        for piece in self.piecesAlive:
            if type(piece) == Pawn:
                unitTypes.add(ChessConstants.PIECES_NAMES[0])
            if type(piece) == Knight:
                unitTypes.add(ChessConstants.PIECES_NAMES[1])
            if type(piece) == Bishop:
                unitTypes.add(ChessConstants.PIECES_NAMES[2])
            if type(piece) == Rook:
                unitTypes.add(ChessConstants.PIECES_NAMES[3])
            if type(piece) == Queen:
                unitTypes.add(ChessConstants.PIECES_NAMES[4])
            if type(piece) == King:
                unitTypes.add(ChessConstants.PIECES_NAMES[5])
        return list(unitTypes)

    def getPiecesAndPosition(self, unitTypes):
        tempUnitStrings = ""
        index = 1
        print("\nNow displaying", unitTypes + "s:\n")
        for piece in self.piecesAlive:
            if type(piece) == globals()[unitTypes]:
                tempUnitStrings = tempUnitStrings + unitTypes[0] + str(index) + ":" + piece.pos + "  "
                index += 1
        return tempUnitStrings

    def selectApiece(self, piecesCoord, unitType):
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
        for x, piece in enumerate(self.piecesAlive):
            if selectPos == piece.pos:
                pieceIndex = x
        print(selectPos, unitType, "selected.")
        if type(pieceIndex) == bool:
            print("Error, failed to select a piece. Defaulting to first piece in array")
            pieceIndex = 0
        return self.piecesAlive[pieceIndex]

    def getNewPosition(self, board, piece):
        pos = ""
        print("\n0) to cancel selection.\n")
        while not pos:
            try:
                pos = input("Where to move: ")
                if pos == "0":
                    return 0
                elif pos not in piece.calculateMoves(board):
                    raise ValueError
            except ValueError:
                print("Wrong input. Invalid move.")
                pos = ""
        return pos

    def allowReturnMenu(self, selectPiece, select, board):
        newPos = 0
        if not selectPiece:
            select = -1
        else:
            newPos = self.getNewPosition(board, selectPiece)
            if not newPos:
                select = -1
        return select, newPos

    def movePiece(self, board):
        select = -1
        unitTypes = self.displayPiecesType()
        selectPiece = False
        if self.color == ChessConstants.COLOR[0]:
            ownCoords = board.whitePieces
        else:
            ownCoords = board.blackPieces
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
                print(self.getPiecesAndPosition(unitTypes[0]), "\n\n0) to return\n")
                selectPiece = self.selectApiece(ownCoords, unitTypes[0])
                print(selectPiece.calculateMoves(board))
                select, newPos = self.allowReturnMenu(selectPiece, select, board)
            if select == 2:
                print(self.getPiecesAndPosition(unitTypes[1]), "\n\n0) to return\n")
                selectPiece = self.selectApiece(ownCoords, unitTypes[1])
                print(selectPiece.calculateMoves(board))
                select, newPos = self.allowReturnMenu(selectPiece, select, board)
            if select == 3:
                print(self.getPiecesAndPosition(unitTypes[2]), "\n\n0) to return\n")
                selectPiece = self.selectApiece(ownCoords, unitTypes[2])
                print(selectPiece.calculateMoves(board))
                select, newPos = self.allowReturnMenu(selectPiece, select, board)
            if select == 4:
                print(self.getPiecesAndPosition(unitTypes[3]), "\n\n0) to return\n")
                selectPiece = self.selectApiece(ownCoords, unitTypes[3])
                print(selectPiece.calculateMoves(board))
                select, newPos = self.allowReturnMenu(selectPiece, select, board)
            if select == 5:
                print(self.getPiecesAndPosition(unitTypes[4]), "\n\n0) to return\n")
                selectPiece = self.selectApiece(ownCoords, unitTypes[4])
                print(selectPiece.calculateMoves(board))
                select, newPos = self.allowReturnMenu(selectPiece, select, board)
            if select == 6:
                print(self.getPiecesAndPosition(unitTypes[5]), "\n\n0) to return\n")
                selectPiece = self.selectApiece(ownCoords, unitTypes[5])
                print(selectPiece.calculateMoves(board))
                select, newPos = self.allowReturnMenu(selectPiece, select, board)
            if select == 0:
                return 0
        selectPiece.pos = newPos
        selectPiece.timesMoved += 1
        return newPos
