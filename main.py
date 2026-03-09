import board
import piece
import random

def choose_colour():
    n = random.randint(0,1)
    if n == 1:
        player1_colour = "w"
        player2_colour = "b"
    else:
        player1_colour = "b"
        player2_colour = "w"
    print(f"Player 1 is {player1_colour} and Player 2 is {player2_colour}")
    return player1_colour,player2_colour

def valid_moves(piece):
    pass

def notation_to_piece(move):
    pass

def validate_move(move):
    piece = notation_to_piece(move)
    if move in valid_moves(piece):
        return True
    return False

def get_move():
    move = input("Enter your move in notation: ")
    return move

def main():
    print("Welcome to Notation Chess!")
    print("Starting PvP game")
    player1_colour,player2_colour = choose_colour()
    game_over = False
    while not game_over:
        if player1_colour == "w":
            board.print_board_white()
        else:
            board.print_board_black()

        move = get_move()



print(main())
