class Piece:
    def __init__(self, colour, position):
        self.colour = colour
        self.position = position

    def move(self, new_position):
        self.position = new_position

    def valid_moves(self,new_position):
        return []


class Bishop(Piece):
    def __init__(self, colour, position):
        super().__init__(colour, position)

    def valid_moves(self, new_position):
        # Implement logic for valid moves for a bishop
        return []
