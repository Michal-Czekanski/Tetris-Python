# cli_tetris.py

import random


#
# TETRIS CLASS
#

class Tetris:

    board_size = 6 # Define board size
    board = [["*" for x in range(6)] for x in range(6)] # Create board
    blocks = []

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
    def move_blocks(self, direction=""):
        def move_down(sf, bl):
                sf.board[bl.row][bl.col] = "*"
                sf.board[bl.row + 1][bl.col] = bl.symbol
        def move_right(sf, bl):
                sf.board[bl.row][bl.col] = "*"
                sf.board[bl.row + 1][bl.col + 1] = bl.symbol
        def move_left(sf, bl):
                sf.board[bl.row][bl.col] = "*"
                sf.board[bl.row + 1][bl.col - 1] = bl.symbol
        

        
        for block in self.blocks:
            if direction == "":
                move_down(self, block)
                
            elif direction == "right".lower():
                if (block.col + 1) in range(self.board_size):
                    move_right(self, block)
                else:
                    move_down(self, block)

            elif direction == "left".lower():
                if (block.col - 1) in range(self.board_size):
                    move_left(self, block)
                else:
                    move_down(self, block)




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

    


Game = Tetris()

kloc1 = Block()
kloc1.appear()

Game.show_board()
Game.move_blocks(direction="right")
Game.show_board()

