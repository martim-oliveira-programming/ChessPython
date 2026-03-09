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

