# cli_tetris.py

import random


#
# TETRIS CLASS
#

class Tetris:

    board_size = 6 # Define board size
    board = [["*" for x in range(6)] for x in range(6)] # Create board
    blocks = [] # List of Block objects that can be moved
    obstacles = [] # List of Block objects that cannot be moved  
    turn = 0 #
    points = 0 #

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

    # Method used to print points
    def print_points(self):
        print()
        print(" Score : {} ".center(50).format(self.points))
    #. 
        

    # Method used to change the number of turns that each Block object exists
    def next_turn(self):
       for block in self.blocks:
           block.turns_existing += 1
    #.
           

    # Method used to move blocks
    def move_blocks(self, direction):
        def move_down(sf, bl): # function that moves block down
                sf.board[bl.row][bl.col] = "*"
                sf.board[bl.row + 1][bl.col] = bl.symbol
                bl.row += 1
        def move_right(sf, bl): # function that moves block right
                sf.board[bl.row][bl.col] = "*"
                sf.board[bl.row + 1][bl.col + 1] = bl.symbol
                bl.row += 1
                bl.col += 1
        def move_horizontally_right(sf, bl): # function that moves block horizontally right
                sf.board[bl.row][bl.col] = "*"
                sf.board[bl.row][bl.col + 1] = bl.symbol
                bl.col += 1
                sf.blocks.remove(bl) # if a block has moved horizontally then it must be removed from the list of blocks that can move
                sf.obstacles.append(bl) # and appended to the list of obstacles
        def move_left(sf, bl): # function that moves block left
                sf.board[bl.row][bl.col] = "*"
                sf.board[bl.row + 1][bl.col - 1] = bl.symbol
                bl.row += 1
                bl.col -= 1
        def move_horizontally_left(sf, bl): # function that moves block horizontally left
                sf.board[bl.row][bl.col] = "*"
                sf.board[bl.row][bl.col - 1] = bl.symbol
                bl.col -= 1
                sf.blocks.remove(bl) # if a block has moved horizontally then it must be removed from the list of blocks that can move
                sf.obstacles.append(bl) # and appended to the list of obstacles
    
        for block in self.blocks: # loop that iterates a Tetris.blocks list(containing block objects that can move)
            if block.turns_existing == 0: # IMPORTANT if a block has just appeared, then it can't move
                continue
            else:
                if direction == "d" or direction == "": # Moving down
                    can_mv_d = block.can_move("d")
                    if can_mv_d: # Block method that checks if a block can move
                        move_down(self, block)
                    elif not(can_mv_d): # if block cannot move down
                        self.blocks.remove(block) # remove block from a list of blocks
            
                elif direction == "r": # Moving right
                    can_mv_r = block.can_move("r")
                    if can_mv_r == True: # if block can move right
                        move_right(self, block)
                    elif can_mv_r == "horizontally right": # if block can move horizontally right
                        move_horizontally_right(self, block)
                    elif not(can_mv_r): # if block cannot move right
                        if block.can_move("d"): # if the way below is free then move block down
                            move_down(self, block)
                        else:
                            self.blocks.remove(block) # if inp was r and block cannot move r or d, remove it from a list of blocks
                            self.obstacles.append(block) # add block to a list of blocks that cannot move
                                                       
                elif direction == "l": # Moving left

                    can_mv_l = block.can_move("l")
                    if can_mv_l == True: # if block can move left
                        move_left(self, block)
                    elif can_mv_l == "horizontally left": # if block can move horizontally
                        move_horizontally_left(self, block)
                    elif not(can_mv_l):# if block cannot move left
                        if block.can_move("d"): # if the way below is free then move block down
                            move_down(self, block)
                        else:
                            self.blocks.remove(block) # if inp was r and block cannot move r or d, remove it from a list of blocks
                            self.obstacles.append(block) # add block to a list of blocks that cannot move
    #.

    def earn_score(self):
        for row in self.board:
                                            

    # Method used to print manual
    def print_manual(self):
        print(" Manual ".center(50, "*"))
        print('To move down - "d" or ""')
        print('To move right - "r"')
        print('To move left - "l"')
        print(" Manual ".center(50, "*"))
    #.

        

#
# BLOCK CLASS
#

class Block(Tetris):

    symbol = "■"

    # This method should be called only once, when creating a Block
    def appear(self): 
        self.row = 0 # starting row 
        self.col = random.randint(0, self.board_size - 1) # starting column randomly generated
        self.board[self.row][self.col] = self.symbol # make Block appear
        self.turns_existing = 0 # how many turns a Block exists(used later for allowing Block to move)
        self.blocks.append(self) # append created Block to the blocks list
    #.

    # method used to tell if the block can move
    def can_move(self, direction):
        if direction == "d":
            if (self.row + 1) in range(self.board_size)\
               and self.board[self.row + 1][self.col] != self.symbol:
                return True
            
        elif direction == "r":
            if( (self.col + 1) in range(self.board_size) ):
                if( (self.row + 1) in range(self.board_size) ):
                    if( self.board[self.row + 1][self.col + 1] != self.symbol ):
                        return True
                    elif( self.board[self.row][self.col + 1] != self.symbol ):
                        return("horizontally right")
                elif( self.board[self.row][self.col + 1] != self.symbol ):
                    return("horizontally right")
                 
        elif direction == "l":
            if( (self.col - 1) in range(self.board_size) ):
                if( (self.row + 1) in range(self.board_size) ):
                    if( self.board[self.row + 1][self.col - 1] != self.symbol ):
                        return True
                    elif( self.board[self.row][self.col - 1] != self.symbol ):
                        return "horizontally left"
                elif( self.board[self.row][self.col - 1] != self.symbol ):
                    return "horizontally left"
    #.
        
        
    


Game = Tetris()
Game.print_manual()
Block().appear()
Game.print_points()
Game.show_board()


i = 1
while True:

    Game.print_points()
    print("Turn {}".format(i))
    Game.next_turn()
    Game.move_blocks(direction=input())
    Game.show_board()
    if( len(Game.blocks) == 0 ):
        Block().appear()
        Game.show_board()
    
    i += 1
    
