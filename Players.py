from Constants import ChessConstants
from Pieces import Pawn, Knight, Rook, Bishop, Queen, King


class Players:

    def __init__(self, color):
        self.color = color
        self.piecesAlive = self.instantiateAll()

    def instantiateAll(self):
        # Va a instanciar el numero apropiado de piezas
        # (8 peones, 2 caballeros, 1 rey, etc) y devolverlos
        # en una lista.
        piecesList = []
        if self.color == ChessConstants.color[0]:
            for x in range(8):
                newPawn = Pawn(self.color, ChessConstants.white_pawn_pos[x])
                piecesList.append(newPawn)
            for x in range(2):
                newKnight = Knight(self.color, ChessConstants.white_knight_pos[x])
                piecesList.append(newKnight)
                newBishop = Bishop(self.color, ChessConstants.white_bishop_pos[x])
                piecesList.append((newBishop))
                newRook = Rook(self.color, ChessConstants.white_rook_pos[x])
                piecesList.append(newRook)
            newQueen = Queen(self.color, ChessConstants.white_queen_pos)
            piecesList.append(newQueen)
            newKing = King(self.color, ChessConstants.white_king_pos)
            piecesList.append(newKing)
        return piecesList

    def movePiece(self):
        # va a listar las piezas vivas, permitir seleccionar una, pedir la lista
        # de movimientos disponibles de la pieza seleccionada y solicitar al tablero
        # que se actualicen  las posiciones despues de confirmar un movimiento.
        pass
