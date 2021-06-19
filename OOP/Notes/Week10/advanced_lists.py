# Advanced lists
"""
my_list = [ [1,2,3], 
            [4,5,6], 
            [7,8,9] ]

print(my_list[0]) # [1,2,3]
print(my_list[0][1]) # 2 [row][col]
print(my_list[1][1]) # 5
print(my_list[2][2]) # 9
"""

# Tic Tac Toe
"""
    - set up an empty 3x3 board using "."
    - ask the user for a coordinate (e.g 0,0)
    - if that space is free, place an X
    - choose random spot for O and place it there if it is free
    - print board
    - repeat until no more spots are left
"""
def is_full(board):
    """
    I:
        board: a 2d list representing a tic tac toe board
    P:
        determine if the board is full or not
    O:
        return True if the board is full (i.e no empty spaces left)
        otherwise return False
    ([[str]]) -> bool
    """
    for row in board:
        for col in row:
            if col == ".":
                return False
    return True

def print_board(board):
    """
    I:
        a 2d list representing a tic tac toe board
    P:
        iterating over the board to produce a visualization of it
    O:
        the visualization of the board
    ([[str]]) -> None
    """
    print("-------")
    for row in board:
        print('|', end="")
        for col in row:
            print(col, end="|")
        print("\n-------")

import random
board = [   [".", ".", "."], 
            [".", ".", "."],
            [".", ".", "."] ]

while not is_full(board):
    coordinates = input("Please enter a coordinate to place an 'X' (e.g. 0,0): ")
    row = int(coordinates[0])
    col = int(coordinates[2])
    if board[row][col] == '.':
        board[row][col] = 'X'

    row = random.randint(0,2)
    col = random.randint(0,2)
    if board[row][col] == '.':
        board[row][col] = 'O'

    print_board(board)