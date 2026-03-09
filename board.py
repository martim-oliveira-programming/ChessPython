letters_1 = [{"a":"R", "b":"N", "c":"B", "d":"Q", "e":"K", "f":"B", "g":"N", "h":"R"},{"a":"P", "b":"P", "c":"P", "d":"P", "e":"P", "f":"P", "g":"P", "h":"P"},{"a":" ", "b":" ", "c":" ", "d":" ", "e":" ", "f":" ", "g":" ", "h":" "},{"a":" ", "b":" ", "c":" ", "d":" ", "e":" ", "f":" ", "g":" ", "h":" "},{"a":" ", "b":" ", "c":" ", "d":" ", "e":" ", "f":" ", "g":" ", "h":" "},{"a":" ", "b":" ", "c":" ", "d":" ", "e":" ", "f":" ", "g":" ", "h":" "},{"a":"p", "b":"p", "c":"p", "d":"p", "e":"p", "f":"p", "g":"p", "h":"p"},{"a":"r", "b":"n", "c":"b", "d":"q", "e":"k", "f":"b", "g":"n", "h":"r"}]
letters_2 = reversed(letters_1)


def change_board(position,letter):
    letters_1[position[0]][position[1]] = letter
    return letters_1


letters_1 = change_board((0,"a"),"M")

def print_board_black()->None:
    board = letters_1
    print("  +---+---+---+---+---+---+---+---+")
    for i, line in enumerate(board, start=1):
        row = " | ".join(reversed(list(line.values())))
        print(f"{i} | {row} |")
        print("  +---+---+---+---+---+---+---+---+")
    print("    h   g   f   e   d   c   b   a\n")


def print_board_white()->None:
    board = letters_2
    print("  +---+---+---+---+---+---+---+---+")
    for i, line in enumerate(board, start=1):
        row = " | ".join(line.values())
        print(f"{9-i} | {row} |")
        print("  +---+---+---+---+---+---+---+---+")
    print("    a   b   c   d   e   f   g   h\n")

print_board_white()
print_board_black()

