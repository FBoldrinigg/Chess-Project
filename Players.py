from Constants import ChessConstants
from Pieces import Pawn, Knight, Rook, Bishop, Queen, King


class Player:

    def __init__(self, color):
        self.color = color
        self.piecesAlive = self.instantiateAll()

    def instantiateAll(self):
        piecesList = []
        if self.color == ChessConstants.COLOR[0]:
            for x in range(8):
                newPawn = Pawn(self.color, ChessConstants.WHITE_PAWN_POS[x])
                piecesList.append(newPawn)
            for x in range(2):
                newKnight = Knight(self.color, ChessConstants.WHITE_KNIGHT_POS[x])
                piecesList.append(newKnight)
                newBishop = Bishop(self.color, ChessConstants.WHITE_BISHOP_POS[x])
                piecesList.append((newBishop))
                newRook = Rook(self.color, ChessConstants.WHITE_ROOK_POS[x])
                piecesList.append(newRook)
            newQueen = Queen(self.color, ChessConstants.WHITE_QUEEN_POS)
            piecesList.append(newQueen)
            newKing = King(self.color, ChessConstants.WHITE_KING_POS)
            piecesList.append(newKing)
        elif self.color == ChessConstants.COLOR[1]:
            for x in range(8):
                newPawn = Pawn(self.color, ChessConstants.BLACK_PAWN_POS[x])
                piecesList.append(newPawn)
            for x in range(2):
                newKnight = Knight(self.color, ChessConstants.BLACK_KNIGHT_POS[x])
                piecesList.append(newKnight)
                newBishop = Bishop(self.color, ChessConstants.BLACK_BISHOP_POS[x])
                piecesList.append(newBishop)
                newRook = Rook(self.color, ChessConstants.BLACK_ROOK_POS[x])
                piecesList.append(newRook)
            newQueen = Queen(self.color, ChessConstants.BLACK_QUEEN_POS)
            piecesList.append(newQueen)
            newKing = King(self.color, ChessConstants.BLACK_KING_POS)
            piecesList.append(newKing)
        return piecesList

    def movePiece(self):
        # va a listar las piezas vivas, permitir seleccionar una, ingresar un movimiento,
        # comparar el movimiento ingresado con la lista de movimientos posibles, y si es
        # valido pasarle los valores al tablero
        pass
