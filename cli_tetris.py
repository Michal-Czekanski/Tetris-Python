# cli_tetris.py

import random


#
# TETRIS CLASS
#

class Tetris:

    board_size = 6 # Define board size
    board = [["*" for x in range(6)] for x in range(6)] # Create board
    blocks = [] # List of Blocks objects

    # Initialise
    def __init__(self): 
        pass
    #.
                     

    # Method used to print board to the screen
    def show_board(self):
        print()
        for row in self.board:
            print(" ".join(row))
        print()
    #.



    # Method used to move blocks
    def move_blocks(self, direction="down"):
        def move_down(sf, bl):
                sf.board[bl.row][bl.col] = "*"
                sf.board[bl.row + 1][bl.col] = bl.symbol
                bl.row += 1
        def move_right(sf, bl):
                sf.board[bl.row][bl.col] = "*"
                sf.board[bl.row + 1][bl.col + 1] = bl.symbol
                bl.row += 1
                bl.col += 1
        def move_left(sf, bl):
                sf.board[bl.row][bl.col] = "*"
                sf.board[bl.row + 1][bl.col - 1] = bl.symbol
                bl.row += 1
                bl.col -= 1
    
        for block in self.blocks:
            if direction == "down":
                if block.can_move("down"):
                    move_down(self, block)
                
            elif direction == "right":
                if block.can_move("right"):
                    move_right(self, block)
                elif block.can_move("down"):
                    move_down(self, block)

            elif direction == "left":
                if block.can_move("left"):
                    move_left(self, block)
                elif block.can_move("down"):
                    move_down(self, block)
    #.




#
# OBSTACLE CLASS
#

class Block(Tetris):

    symbol = "■"

    # this method should be called only once, when creating a Block
    def appear(self): 
        self.row = 0 # starting row 
        self.col = random.randint(0, self.board_size - 1) # starting column randomly generated
        self.board[self.row][self.col] = self.symbol # make Block appear
        self.blocks.append(self) # append created Block to the blocks list
    #.

    # this method is used to tell if the block can move
    def can_move(self, direction):
        if direction == "down":
            if (self.row + 1) in range(self.board_size)\
               and self.board[self.row + 1][self.col] != self.symbol:
                return True
            
        elif direction == "right":
            if (self.row + 1) in range(self.board_size) and\
               (self.col + 1) in range(self.board_size) and\
                self.board[self.row + 1][self.col + 1] != self.symbol:
                return True
            
        elif direction == "left":
            if (self.row + 1) in range(self.board_size) and\
               (self.col - 1) in range(self.board_size) and\
               self.board[self.row + 1][self.col - 1] != self.symbol:
                return True
    #.
        
        
    


Game = Tetris()
Game.show_board()

for i in range(12):
    print("Turn {}".format(i+1))
    if i == 0 or i == 5:
        Block().appear()
    Game.move_blocks(direction=input())
    Game.show_board()

