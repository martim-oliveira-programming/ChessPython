class Piece:
    def __init__(self, colour, position):
        self.colour = colour
        self.position = position
        self.letter = ""

    def position_to_board(self):
        column = self.position[0]
        line = int(self.position[1]) -1
        return line,column

class Bishop(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        if self.colour == "w":
            self.letter = "B"
        else:
            self.letter = "b"
        

class Pawn(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        if self.colour == "w":
            self.letter = "P"
        else:
            self.letter = "p"


class Knight(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        if self.colour == "w":
            self.letter = "N"
        else:
            self.letter = "n"



class Rook(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        if self.colour == "w":
            self.letter = "R"
        else:
            self.letter = "r"

class Queen(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        if self.colour == "w":
            self.letter = "Q"
        else:
            self.letter = "q"


class King(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)
        if self.colour == "w":
            self.letter = "K"
        else:
            self.letter = "k"

Rook_a = Rook("w","a1")
Knight_b = Knight("w","b1")
Bishop_c = Bishop("w","c1")
Queen_d = Queen("w","d1")
King_e = King("w","e1")
Bishop_f = Bishop("w","f1")
Knight_g = Knight("w","g1")
Rook_h = Rook("w","h1")
Pawn_a = Pawn("w","a2")
Pawn_b = Pawn("w","b2")
Pawn_c = Pawn("w","c2")
Pawn_d = Pawn("w","d2")
Pawn_e = Pawn("w","e2")
Pawn_f = Pawn("w","f2")
Pawn_g = Pawn("w","g2")
Pawn_h = Pawn("w","h2")

rook_a = Rook("b","a8")
knight_b = Knight("b","b8")
bishop_c = Bishop("b","c8")
queen_d = Queen("b","d8")
king_e = King("b","e8")
bishop_f = Bishop("b","f8")
knight_g = Knight("b","g8")
rook_h = Rook("b","h8")
pawn_a = Pawn("b","a7")
pawn_b = Pawn("b","b7")
pawn_c = Pawn("b","c7")
pawn_d = Pawn("b","d7")
pawn_e = Pawn("b","e7")
pawn_f = Pawn("b","f7")
pawn_g = Pawn("b","g7")
pawn_h = Pawn("b","h7")

white_pieces = [Rook_a, Knight_b, Bishop_c, Queen_d, King_e, Bishop_f, Knight_g, Rook_h, Pawn_a, Pawn_b, Pawn_c, Pawn_d, Pawn_e, Pawn_f, Pawn_g, Pawn_h]
black_pieces = [rook_a, knight_b, bishop_c, queen_d, king_e, bishop_f, knight_g, rook_h, pawn_a, pawn_b, pawn_c, pawn_d, pawn_e, pawn_f, pawn_g, pawn_h]
